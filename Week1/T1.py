import qiskit
from qiskit_aer import Aer


print("Qiskit Version:", qiskit.__version__)

print("\nAvailable Backends:")
for backend in Aer.backends():
    print(backend.name)