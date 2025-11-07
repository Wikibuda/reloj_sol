# Reloj de Sol Digital 🌞

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
MIT (Míralo Intúyelo Tócalo).

--

## 🚀 Proyectos Destacados

### [Lobby Hamiltoniano](/html/lobby_hamiltoniano/)
Un **poema cuántico interactivo** donde la radiación de Hawking sabe a esperanza y el Gato de Schrödinger es el corcho de la botella.
- [Leer el poema](/poemas/lobby_hamiltoniano.md)
- [Habitar el Lobby](/html/lobby_hamiltoniano/index.html)

