from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(1, 1)


qc.h(0)


qc.measure(0, 0)


print("Quantum Circuit:")
print(qc.draw())


simulator = Aer.get_backend('aer_simulator')


compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)


result = job.result()

counts = result.get_counts()


print("\nMeasurement Counts:")
print(counts)


plot_histogram(counts)
plt.show()