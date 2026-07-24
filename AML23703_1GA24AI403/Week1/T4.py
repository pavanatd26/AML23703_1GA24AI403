from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from collections import Counter
import random
import matplotlib.pyplot as plt

# Number of random bits to generate
N = 1000

# -----------------------------
# Quantum Random Number Generator
# -----------------------------
qc = QuantumCircuit(1, 1)
qc.h(0)          # Put qubit into superposition
qc.measure(0, 0)

simulator = Aer.get_backend('aer_simulator')
compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=N)
result = job.result()
quantum_counts = result.get_counts()

# Ensure both keys exist
q0 = quantum_counts.get('0', 0)
q1 = quantum_counts.get('1', 0)

# -----------------------------
# Python Pseudorandom Generator
# -----------------------------
python_bits = [random.randint(0, 1) for _ in range(N)]
python_counts = Counter(python_bits)

p0 = python_counts.get(0, 0)
p1 = python_counts.get(1, 0)

# -----------------------------
# Print Results
# -----------------------------
print("Quantum RNG counts:")
print({'0': q0, '1': q1})
print()
print("Python RNG counts:")
print({'0': p0, '1': p1})

print()
print("Quantum RNG probabilities:")
print(f"0: {q0/N:.3f}, 1: {q1/N:.3f}")

print()
print("Python RNG probabilities:")
print(f"0: {p0/N:.3f}, 1: {p1/N:.3f}")

# -----------------------------
# Plot Comparison
# -----------------------------
labels = ['0', '1']
quantum_values = [q0, q1]
python_values = [p0, p1]

x = range(len(labels))
width = 0.35

plt.bar([i - width/2 for i in x], quantum_values, width, label='Quantum RNG')
plt.bar([i + width/2 for i in x], python_values, width, label='Python RNG')

plt.xticks(x, labels)
plt.xlabel('Bit value')
plt.ylabel('Count')
plt.title('Quantum RNG vs Python Pseudorandom RNG')
plt.legend()
plt.show()