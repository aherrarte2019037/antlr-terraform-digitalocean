# 🐳 Guía Rápida: Configuración de Docker

## 🧭 Propósito

Este documento explica cómo instalar y configurar Docker en **Linux**, **macOS** y **Windows**. También se sugiere **Rancher Desktop** como una alternativa ligera y práctica.

---

## 🐧 Linux

### 🔧 Instalación Básica

1. Actualizar paquetes:

   ```bash
   sudo apt update
   ```
2. Instalar Docker:

   ```bash
   sudo apt install docker.io
   ```
3. Habilitar e iniciar el servicio:

   ```bash
   sudo systemctl enable docker
   sudo systemctl start docker
   ```
4. Verificar instalación:

   ```bash
   docker --version
   ```

📖 Documentación oficial: [Docker en Linux](https://docs.docker.com/engine/install/#server)

---

## 🍎 macOS

### 🔧 Instalación con Docker Desktop

1. Descargar desde la web oficial:[Docker para macOS](https://docs.docker.com/desktop/install/mac-install/)
2. Seguir el asistente de instalación.
3. Verificar con:

   ```bash
   docker --version
   ```

---

## 🪟 Windows

### 🔧 Instalación con Docker Desktop

1. Descargar desde:[Docker para Windows](https://docs.docker.com/desktop/install/windows-install/)
2. Habilitar WSL2 si es necesario.
3. Reiniciar el sistema tras la instalación.
4. Verificar con:

   ```powershell
   docker --version
   ```

---

## 🌿 Alternativa: Rancher Desktop

**Rancher Desktop** ofrece una interfaz gráfica y soporte para containerd o dockerd.

✅ Ventajas:

- Código abierto
- Configuración simple
- Compatible con WSL, macOS y Linux

🔗 Sitio oficial: [rancherdesktop.io](https://rancherdesktop.io/)

---

## 🧪 Verificación Final

Para confirmar que Docker está activo:

```bash
docker run hello-world
```

Esto descargará una imagen de prueba y mostrará un mensaje de éxito si todo está bien.

---

## 🧱 Recomendación

Se sugiere usar Docker Desktop o Rancher Desktop en entornos de desarrollo. Ambos permiten controlar versiones y recursos con facilidad.
