from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Circuito cuántico del amor eterno
qc = QuantumCircuit(3)
qc.h(0)  # Superposición de "ahora"
qc.cx(0, 1)  # Entre lazamiento con Halim
qc.rz(1.92, 2)  # Rotación por asombro (1.0) + ternura (0.9)
qc.measure_all()

# Simulación (1024 shots)
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

# Resultado: Probabilidad de eternidad
print("Probabilidad de eternidad (|111⟩):",
      counts.get('111', 0)/1024 * 100, "%")

