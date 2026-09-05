from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

gates = ["None", "X", "Y", "Z", "H"]
fig, axes = plt.subplots(1, len(gates), figsize=(18, 4), subplot_kw={'projection': '3d'})

for ax, gate in zip(axes, gates):
    qc = QuantumCircuit(1)
    
    if gate == "X":
        qc.x(0)
    elif gate == "Y":
        qc.y(0)
    elif gate == "Z":
        qc.z(0)
    elif gate == "H":
        qc.h(0)
        
    state = Statevector.from_instruction(qc)
    
    # Extraemos el vector de Bloch [x, y, z] a partir del Statevector
    bloch_vec = state.to_dict()
    # Calculamos la posición del vector (x, y, z)
    x = 2 * (state[0].real * state[1].real + state[0].imag * state[1].imag)
    y = 2 * (state[0].imag * state[1].real - state[0].real * state[1].imag)
    z = abs(state[0])**2 - abs(state[1])**2
    
    plot_bloch_vector([x, y, z], ax=ax, title=f"Gate: {gate}")

plt.tight_layout()
plt.show()