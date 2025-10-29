import os
import shutil
from datetime import datetime
import random
import subprocess

# Configuración (personaliza estas rutas)
DRIVE_PATH = "/Users/gusluna/wikibuda/Memorias_Talladas/"
GITHUB_REPO = "github.com/Wikibuda/reloj_sol.git"
LOCAL_TEMP = "/tmp/memorias_temp/"
TOKEN_GITHUB = "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"

# Versos para los commits (de tus Wattpad)
versos = [
    "El tiempo es un hotel donde nunca duermo",
    "Las partículas susurran entre papers arrugados",
    "El hamiltoniano del ascensor sube y baja como un gato de Schrödinger",
    "El universo es un poema escrito en lenguaje de máquina"
]

def sincronizar():
    # 1. Clonar el repo remoto (solo si no existe)
    if not os.path.exists(LOCAL_TEMP):
        subprocess.run(["git", "clone", f"https://{TOKEN_GITHUB}@{GITHUB_REPO}", LOCAL_TEMP], check=True)

    # 2. Copiar archivos desde Drive a la carpeta clonado
    for archivo in os.listdir(DRIVE_PATH):
        if archivo.endswith(".md"):
            shutil.copy(os.path.join(DRIVE_PATH, archivo), LOCAL_TEMP)

    # 3. Git: add, commit, push
    os.chdir(LOCAL_TEMP)
    subprocess.run(["git", "add", "."], check=True)
    mensaje = f"{datetime.now().strftime('%d-%m-%Y')}: '{random.choice(versos)}'"
    subprocess.run(["git", "commit", "-m", mensaje], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

# Ejecutar
sincronizar()
