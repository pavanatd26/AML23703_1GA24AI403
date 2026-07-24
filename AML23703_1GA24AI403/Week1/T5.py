from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

print("Quantum Circuit:")
print(qc.draw())

# -----------------------------
# Ideal Simulator
# -----------------------------
ideal_sim = Aer.get_backend("aer_simulator")

compiled = transpile(qc, ideal_sim)

job = ideal_sim.run(compiled, shots=1024)

ideal_counts = job.result().get_counts()

print("\nIdeal Simulator Output:")
print(ideal_counts)

# -----------------------------
# Noise Model Simulator
# -----------------------------
noise_model = NoiseModel()

# Add a small depolarizing error
error = depolarizing_error(0.05, 1)

noise_model.add_all_qubit_quantum_error(error, ['h'])

noisy_sim = Aer.get_backend("aer_simulator")

job = noisy_sim.run(
    compiled,
    noise_model=noise_model,
    shots=1024
)

noisy_counts = job.result().get_counts()

print("\nNoise Simulator Output:")
print(noisy_counts)

# -----------------------------
# Plot Results
# -----------------------------
fig, ax = plt.subplots(1, 2, figsize=(10,4))

plot_histogram(ideal_counts, ax=ax[0])
ax[0].set_title("Ideal Simulator")

plot_histogram(noisy_counts, ax=ax[1])
ax[1].set_title("Noise Simulator")

plt.tight_layout()
plt.show()