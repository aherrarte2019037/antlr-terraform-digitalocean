import sys
import time
import json
import argparse
import requests
from antlr4 import *
from TerraformSubsetLexer import TerraformSubsetLexer
from TerraformSubsetParser import TerraformSubsetParser
from TerraformSubsetListener import TerraformSubsetListener

class TerraformListener(TerraformSubsetListener):
    def __init__(self):
        self.variables = {}
        self.provider_token_expr = None
        self.droplet_config = {}

    def enterVariable(self, ctx):
        var_name = ctx.STRING().getText().strip('"')
        for kv in ctx.body().keyValue():
            key = kv.IDENTIFIER().getText()
            if key == "default":
                value = kv.expr().getText().strip('"')
                self.variables[var_name] = value
                print(f"[var] {var_name} = {value}")

    def enterProvider(self, ctx):
        provider_name = ctx.STRING().getText().strip('"')
        if provider_name != "digitalocean":
            raise Exception("Only 'digitalocean' provider is supported.")

        for kv in ctx.body().keyValue():
            key = kv.IDENTIFIER().getText()
            expr = kv.expr().getText()
            if key == "token":
                self.provider_token_expr = expr

    def enterResource(self, ctx):
        type_ = ctx.STRING(0).getText().strip('"')
        name = ctx.STRING(1).getText().strip('"')
        if type_ != "digitalocean_droplet":
            return

        for kv in ctx.body().keyValue():
            key = kv.IDENTIFIER().getText()
            val = kv.expr().getText().strip('"')
            self.droplet_config[key] = val

    def resolve_token(self):
        if not self.provider_token_expr:
            raise Exception("No token specified in provider block.")
        if self.provider_token_expr.startswith("var."):
            var_name = self.provider_token_expr.split(".")[1]
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Undefined variable '{var_name}' used in provider block.")
        return self.provider_token_expr.strip('"')

def create_droplet(api_token, config):
    url = "https://api.digitalocean.com/v2/droplets"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    payload = {
        "name": config["name"],
        "region": config["region"],
        "size": config["size"],
        "image": config["image"],
        "ssh_keys": [],
        "backups": False,
        "ipv6": False,
        "user_data": None,
        "private_networking": None,
        "volumes": None,
        "tags": []
    }

    print("[*] Creating droplet...")
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    droplet = response.json()["droplet"]
    droplet_id = droplet["id"]
    print(f"[+] Droplet created with ID: {droplet_id}")

    print("[*] Waiting for droplet to become active and assigned an IP...")
    while True:
        resp = requests.get(f"https://api.digitalocean.com/v2/droplets/{droplet_id}", headers=headers)
        droplet_info = resp.json()["droplet"]
        networks = droplet_info["networks"]["v4"]
        public_ips = [n["ip_address"] for n in networks if n["type"] == "public"]
        if public_ips:
            ip = public_ips[0]
            break
        time.sleep(5)

    return droplet_id, ip

def save_state_file(droplet_config, droplet_id, ip):
    """Save terraform state file"""
    state = {
        "version": 4,
        "terraform_version": "custom",
        "resources": [
            {
                "mode": "managed",
                "type": "digitalocean_droplet",
                "name": "web",
                "provider": "digitalocean",
                "instances": [
                    {
                        "attributes": {
                            "id": str(droplet_id),
                            "name": droplet_config["name"],
                            "region": droplet_config["region"],
                            "size": droplet_config["size"],
                            "image": droplet_config["image"],
                            "ipv4_address": ip
                        }
                    }
                ]
            }
        ]
    }

    with open("terraform.tfstate", "w") as f:
        json.dump(state, f, indent=2)
    
    print(f"[✓] State file saved: terraform.tfstate")

def load_state_file():
    """Load terraform state file"""
    try:
        with open("terraform.tfstate", "r") as f:
            state = json.load(f)
        
        # Extract droplet info from state
        for resource in state.get("resources", []):
            if resource.get("type") == "digitalocean_droplet":
                instance = resource["instances"][0]
                attrs = instance["attributes"]
                return {
                    "id": attrs["id"],
                    "name": attrs["name"],
                    "ip": attrs["ipv4_address"]
                }
        return None
    except FileNotFoundError:
        print("[!] No terraform.tfstate file found")
        return None

def destroy_droplet(api_token, droplet_id):
    """Destroy droplet using API"""
    url = f"https://api.digitalocean.com/v2/droplets/{droplet_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    print(f"[*] Destroying droplet with ID: {droplet_id}")
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    print(f"[✓] Droplet {droplet_id} destroyed successfully")

def terraform_apply(terraform_file):
    """Simulate terraform apply"""
    input_stream = FileStream(terraform_file)
    lexer = TerraformSubsetLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TerraformSubsetParser(stream)
    tree = parser.terraform()

    listener = TerraformListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    token = listener.resolve_token()
    if not listener.droplet_config:
        raise Exception("Missing digitalocean_droplet resource.")

    droplet_id, ip = create_droplet(token, listener.droplet_config)
    save_state_file(listener.droplet_config, droplet_id, ip)
    
    print(f"[✓] Droplet available at IP: {ip}")
    print(f"[✓] Apply complete! Resources: 1 added, 0 changed, 0 destroyed.")

def terraform_destroy(terraform_file):
    """Simulate terraform destroy"""
    # Load state file to get droplet ID
    state_info = load_state_file()
    if not state_info:
        print("[!] No state file found. Nothing to destroy.")
        return

    # Parse terraform file to get token
    input_stream = FileStream(terraform_file)
    lexer = TerraformSubsetLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TerraformSubsetParser(stream)
    tree = parser.terraform()

    listener = TerraformListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    token = listener.resolve_token()
    
    # Destroy the droplet
    destroy_droplet(token, state_info["id"])
    
    # Remove state file
    import os
    try:
        os.remove("terraform.tfstate")
        print("[✓] State file removed")
    except FileNotFoundError:
        pass
    
    print(f"[✓] Destroy complete! Resources: 0 added, 0 changed, 1 destroyed.")

def main():
    parser = argparse.ArgumentParser(description='Terraform subset parser')
    parser.add_argument('terraform_file', help='Terraform file to parse')
    parser.add_argument('--apply', action='store_true', help='Apply terraform configuration')
    parser.add_argument('--destroy', action='store_true', help='Destroy terraform resources')
    
    args = parser.parse_args()

    if args.apply:
        terraform_apply(args.terraform_file)
    elif args.destroy:
        terraform_destroy(args.terraform_file)
    else:
        # Default behavior (backward compatibility)
        terraform_apply(args.terraform_file)

if __name__ == "__main__":
    main()