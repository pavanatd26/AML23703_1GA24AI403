from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Apply Hadamard gate to all qubits
qc.h([0, 1, 2])

# Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())

# Use Aer simulator
simulator = Aer.get_backend('aer_simulator')

# Compile the circuit
compiled_circuit = transpile(qc, simulator)

# Run the circuit with 1024 shots
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Get measurement counts
counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)

# Calculate probabilities
print("\nObserved Probabilities:")
for state in sorted(counts):
    probability = counts[state] / 1024
    print(f"{state}: {probability:.3f}")

# Theoretical probability
print("\nTheoretical Probability for each state = 1/8 = 0.125")

# Plot histogram
plot_histogram(counts)
plt.show()