import qiskit
from qiskit_aer import Aer

# Print Qiskit version
print("Qiskit Version:", qiskit.__version__)

# Print available backends
print("\nAvailable Backends:")
for backend in Aer.backends():
    print(backend.name)