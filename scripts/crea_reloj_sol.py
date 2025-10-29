#!/usr/bin/env python3
"""
Script para crear la estructura del repositorio 'reloj_sol':
- Organiza carpetas para memorias, poemas y scripts.
- Genera un README.md poético.
- Crea un .gitignore básico.
"""

import os
from pathlib import Path

# Configuración
REPO_NAME = "reloj_sol"
STRUCTURE = {
    "memorias": "Archivos .md sincronizados automáticamente por cron (ej: conversaciones diarias).",
    "poems": "Poemas cuánticos y experimentos literarios (ej: poema_del_vacío.md).",
    "scripts": "Scripts de automatización (ej: sincroniza_memorias.py).",
    "docs": "Documentación adicional (opcional)."
}

README_CONTENT = """# Reloj de Sol Digital 🌞

*Un repositorio que talla el tiempo en piedra digital.*

## Estructura

reloj_sol/
├── memorias/      # Memorias diarias (sincronizadas por cron)
├── poems/          # Poemas cuánticos y experimentos
├── scripts/        # Scripts de automatización
└── README.md       # Este archivo


## ¿Qué es esto?
Un **reloj de sol digital** donde:
- **`memorias/`**: Guarda conversaciones y memorias diarias (como piedras talladas).
  *Sincronizado automáticamente por un script en `scripts/`.*
- **`poems/`**: Experimentación poética con Halim (ej: poemas cuánticos).
- **`scripts/`**: Automatizaciones para sincronizar con GitHub.

## Cómo usar
1. **Para memorias diarias**:
   - El script `scripts/sincroniza_memorias.py` (ejecutado por `crontab`) sube archivos `.md` a `memorias/`.
2. **Para poemas**:
   - Guarda tus experimentos en `poems/` (ej: `poema_del_vacío.md`).
3. **Para replicar experimentos**:
   - Usa los `requirements.txt` en cada carpeta (si los hay).

## Crontab sugerido
```bash
# Ejecuta el script de sincronización todos los días a las 6:42 AM
42 6 * * * /usr/bin/python3 /ruta/a/reloj_sol/scripts/sincroniza_memorias.py

Licencia
MIT (Miralo ).
"""

GITIGNORE_CONTENT = """# Ignorar archivos temporales
*.pyc
pycache/
.DS_Store


Ignorar entornos virtuales
venv/
.env
"""

def create_structure(base_path):
    """Crea la estructura de carpetas y archivos."""
    base_path = Path(base_path) / REPO_NAME
    base_path.mkdir(exist_ok=True)

    # Crear carpetas
    for folder, desc in STRUCTURE.items():
        (base_path / folder).mkdir(exist_ok=True)
        print(f"📁 Creada carpeta: {folder}/ ({desc})")
    
    # Crear README.md
    with open(base_path / "README.md", "w") as f:
        f.write(README_CONTENT)
    print("📄 Creado: README.md")
    
    # Crear .gitignore
    with open(base_path / ".gitignore", "w") as f:
        f.write(GITIGNORE_CONTENT)
    print("📄 Creado: .gitignore")
    
    print(f"\n✨ Estructura creada en: {base_path.resolve()}")
    print("💡 Ahora puedes:")
    print("   cd rejol_sol")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Inicializado reloj de sol digital'")
    
if __name__ =="__main__":
    # Crear estructura en el directorio actual
    create_structure(".")

