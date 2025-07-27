# Generated from TerraformSubset.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TerraformSubsetParser import TerraformSubsetParser
else:
    from TerraformSubsetParser import TerraformSubsetParser

# This class defines a complete listener for a parse tree produced by TerraformSubsetParser.
class TerraformSubsetListener(ParseTreeListener):

    # Enter a parse tree produced by TerraformSubsetParser#terraform.
    def enterTerraform(self, ctx:TerraformSubsetParser.TerraformContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#terraform.
    def exitTerraform(self, ctx:TerraformSubsetParser.TerraformContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#block.
    def enterBlock(self, ctx:TerraformSubsetParser.BlockContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#block.
    def exitBlock(self, ctx:TerraformSubsetParser.BlockContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#provider.
    def enterProvider(self, ctx:TerraformSubsetParser.ProviderContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#provider.
    def exitProvider(self, ctx:TerraformSubsetParser.ProviderContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#resource.
    def enterResource(self, ctx:TerraformSubsetParser.ResourceContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#resource.
    def exitResource(self, ctx:TerraformSubsetParser.ResourceContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#variable.
    def enterVariable(self, ctx:TerraformSubsetParser.VariableContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#variable.
    def exitVariable(self, ctx:TerraformSubsetParser.VariableContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#output.
    def enterOutput(self, ctx:TerraformSubsetParser.OutputContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#output.
    def exitOutput(self, ctx:TerraformSubsetParser.OutputContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#body.
    def enterBody(self, ctx:TerraformSubsetParser.BodyContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#body.
    def exitBody(self, ctx:TerraformSubsetParser.BodyContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#keyValue.
    def enterKeyValue(self, ctx:TerraformSubsetParser.KeyValueContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#keyValue.
    def exitKeyValue(self, ctx:TerraformSubsetParser.KeyValueContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#expr.
    def enterExpr(self, ctx:TerraformSubsetParser.ExprContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#expr.
    def exitExpr(self, ctx:TerraformSubsetParser.ExprContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#reference.
    def enterReference(self, ctx:TerraformSubsetParser.ReferenceContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#reference.
    def exitReference(self, ctx:TerraformSubsetParser.ReferenceContext):
        pass



del TerraformSubsetParser