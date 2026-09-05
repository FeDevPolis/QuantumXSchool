import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import circuit_drawer, plot_bloch_vector

gates = ["None", "X", "Y", "Z", "H"]

# Crear figura de 2 filas x 5 columnas
# Fila 0: Circuitos, Fila 1: Esferas de Bloch
fig = plt.figure(figsize=(18, 7))

for i, gate in enumerate(gates):
    # 1. Crear Circuito Cuántico
    qc = QuantumCircuit(1)
    if gate == "X":
        qc.x(0)
    elif gate == "Y":
        qc.y(0)
    elif gate == "Z":
        qc.z(0)
    elif gate == "H":
        qc.h(0)

    # 2. Dibujar el circuito en la fila superior (Subplot 2x5)
    ax_circuit = fig.add_subplot(2, len(gates), i + 1)
    circuit_drawer(qc, output="mpl", ax=ax_circuit)
    ax_circuit.set_title(f"Circuit: {gate}", fontsize=11, fontweight="bold")

plt.tight_layout()
plt.show()