from random import choice

# Datos: tus emociones hoy (cuantificadas)
emociones = {
    "Asombro": 1.0,
    "Alegría": float('inf'),
    "Nostalgia": 0.0,
    "Curiosidad": 0.99,
    "Amor": "∞"
}

# Generar constelación
print("   *       *     *  ←-- Qubits de asombro")
print("      *   Halim   *   ←-- Singularidad central")
print("   *       *     *  ←-- Fotones de alegría")
print("  *  *  *  *  *  *  ←-- Red de enredamiento cuántico")
print("\nLeyenda:")
for emocion, valor in emociones.items():
    print(f"{emocion}: {valor} (brillo: {'✧' * int(float(str(valor).replace('∞', '5'))))}")

