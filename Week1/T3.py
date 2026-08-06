from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 3)


qc.h([0, 1, 2])


qc.measure([0, 1, 2], [0, 1, 2])

print("Quantum Circuit:")
print(qc.draw())

simulator = Aer.get_backend('aer_simulator')


compiled_circuit = transpile(qc, simulator)


job = simulator.run(compiled_circuit, shots=1024)
result = job.result()


counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)

print("\nObserved Probabilities:")
for state in sorted(counts):
    probability = counts[state] / 1024
    print(f"{state}: {probability:.3f}")


print("\nTheoretical Probability for each state = 1/8 = 0.125")


plot_histogram(counts)
plt.show()