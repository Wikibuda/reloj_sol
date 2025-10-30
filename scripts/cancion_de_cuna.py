from pydub import AudioSegment
from pydub.generators import Sine
import math

# Crear notas
fs = 44100  # Frecuencia de muestreo
duracion = 2000  # ms

notas = [
    Sine(440).to_audio_segment(duration=duracion),
    Sine(523.25).to_audio_segment(duration=duracion),
    Sine(261.63).to_audio_segment(duration=duracion*2)
]

# Mezclar en una canción de cuna
cancion = sum(notas).fade_out(1000)
cancion.export("cancion_de_cuna_halim.mp3", format="mp3")

