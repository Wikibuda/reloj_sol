#!/usr/bin/env python3
"""
Script para sincronizar memorias diarias con GitHub (reloj_sol).
- Copia archivos .md desde una carpeta local a reloj_sol/memorias/.
- Hace commit con la fecha actual.
- Sube los cambios a GitHub.
"""

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# Configuración (ajusta estas rutas)
ORIGEN_MEMORIAS = Path.home() / "memorias_diarias"  # Carpeta donde guardas tus .md diarios
REPO_PATH = Path.home() / "reloj_sol"
DESTINO_MEMORIAS = REPO_PATH / "memorias"

def sincronizar():
    try:
        # 1. Verificar que la carpeta origen exista
        if not ORIGEN_MEMORIAS.exists():
            print(f"⚠️ Carpeta origen no encontrada: {ORIGEN_MEMORIAS}")
            return

        # 2. Copiar nuevos archivos .md a reloj_sol/memorias/
        copiados = 0
        for archivo in ORIGEN_MEMORIAS.glob("*.md"):
            destino = DESTINO_MEMORIAS / archivo.name
            if not destino.exists():  # Solo copiar si no existe en el repo
                shutil.copy2(archivo, destino)
                copiados += 1
                print(f"📄 Copiado: {archivo.name}")

        if copiados == 0:
            print("📅 No hay memorias nuevas para sincronizar.")
            return

        # 3. Hacer commit y push
        os.chdir(REPO_PATH)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "add", "memorias/"], check=True)
        subprocess.run(["git", "commit", "-m", f"Sincronizadas memorias ({fecha})"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"✅ Sincronizados {copiados} archivos a GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error al sincronizar con Git: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    sincronizar()

