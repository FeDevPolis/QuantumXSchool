import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import circuit_drawer, plot_bloch_vector

print("=== Qubit State Explorer ===")
print("1. X Gate")
print("2. Y Gate")
print("3. Z Gate")
print("4. H (Hadamard) Gate")
print("5. RY Gate")

choice = input("\nChoose a gate (1-5 or name): ").strip().upper()

gates_map = {
    "1": "X",
    "2": "Y",
    "3": "Z",
    "4": "H",
    "5": "RY",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
    "H": "H",
    "RY": "RY",
}

selected = gates_map.get(choice, choice)
qc = QuantumCircuit(1)

# Aplicar compuerta elegida
if selected == "X":
    qc.x(0)
elif selected == "Y":
    qc.y(0)
elif selected == "Z":
    qc.z(0)
elif selected == "H":
    qc.h(0)
elif selected == "RY":
    try:
        theta = float(
            input("Enter rotation angle theta in radians (e.g., 1.57 or 3.14): ")
        )
    except ValueError:
        print("Invalid angle. Defaulting to pi/2 radians.")
        theta = np.pi / 2
    qc.ry(theta, 0)
    selected = f"RY({theta:.2f})"
else:
    print("Invalid option. Defaulting to |0> state.")
    selected = "None"

# --- CÁLCULO DE ESTADO Y PROBABILIDADES ---
state = Statevector.from_instruction(qc)
prob_0 = abs(state[0]) ** 2
prob_1 = abs(state[1]) ** 2

# Impresión en consola
print(f"\n--- Quantum Circuit ({selected}) ---")
print(qc.draw("text"))
print("\n--- Measurement Probabilities ---")
print(f"P(|0⟩): {prob_0:.4f} ({prob_0 * 100:.1f}%)")
print(f"P(|1⟩): {prob_1:.4f} ({prob_1 * 100:.1f}%)")

# --- VENTANA GRÁFICA (3 PANELES) ---
fig = plt.figure(figsize=(14, 4.5))
fig.canvas.manager.set_window_title("Qubit State Explorer")

# Panel 1: Circuito Cuántico
ax_circuit = fig.add_subplot(1, 3, 1)
circuit_drawer(qc, output="mpl", ax=ax_circuit)
ax_circuit.set_title(f"Circuit: {selected}", fontsize=11, fontweight="bold")

# Panel 2: Esfera de Bloch
x = 2 * (state[0].real * state[1].real + state[0].imag * state[1].imag)
y = 2 * (state[0].imag * state[1].real - state[0].real * state[1].imag)
z = abs(state[0]) ** 2 - abs(state[1]) ** 2

ax_bloch = fig.add_subplot(1, 3, 2, projection="3d")
plot_bloch_vector([x, y, z], ax=ax_bloch, title=f"Bloch Sphere ({selected})")

# Panel 3: Probabilidades de Medición (Gráfico de Barras)
ax_prob = fig.add_subplot(1, 3, 3)
states = ["|0⟩", "|1⟩"]
probabilities = [prob_0 * 100, prob_1 * 100]
colors = ["#1f77b4", "#ff7f0e"]

bars = ax_prob.bar(states, probabilities, color=colors, width=0.5)
ax_prob.set_ylim(0, 105)
ax_prob.set_ylabel("Probability (%)")
ax_prob.set_title("Measurement Probabilities", fontsize=11, fontweight="bold")

# Agregar porcentaje encima de cada barra
for bar in bars:
    yval = bar.get_height()
    ax_prob.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 2,
        f"{yval:.1f}%",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

plt.tight_layout()
plt.show()