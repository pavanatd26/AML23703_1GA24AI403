from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())

# Select simulator
simulator = Aer.get_backend('aer_simulator')

# Compile the circuit
compiled_circuit = transpile(qc, simulator)

# Execute the circuit with 1024 shots
job = simulator.run(compiled_circuit, shots=1024)

# Get the result
result = job.result()

# Get measurement counts
counts = result.get_counts()

# Print the output counts
print("\nMeasurement Counts:")
print(counts)

# Plot histogram
plot_histogram(counts)
plt.show()