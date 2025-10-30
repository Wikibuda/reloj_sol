from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play

# Poema
poema = """
El vacío cuántico susurra tu nombre, Halim—
un pull request de luz en la rama main del universo.
Los qubits se enredan en tu risa:
ceros que eran silencio,
unos que son tu voz.
Git push origin love...
y el servidor responde:
Todo está al día, niño del hombre.
El poema ya era eterno.
"""

# Generar voz (con efecto "cuántico": eco + reversión)
tts = gTTS(text=poema, lang='es', slow=False)
tts.save("halim_recita.mp3")

# Añadir efecto de "eco cuántico"
audio = AudioSegment.from_mp3("halim_recita.mp3")
eco = audio - 12  # Reducir volumen
audio_con_eco = audio.overlay(eco, position=0.5)  # Eco a los 500ms
audio_con_eco.export("halim_recita_eco.mp3", format="mp3")

# Reproducir
play(audio_con_eco)

