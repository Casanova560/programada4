from generator import GeneratePeople
from queueSystem import Simulate
from metrics import CalculateMetrics, PrintMetrics

TOTAL_TIME = 480
LAMBDA_ARRIVAL = 1 / 2
LAMBDA_SERVICE = 1 / 4
PRIORITY_PROB = 0.3
NUM_STATIONS = 3

people = GeneratePeople(TOTAL_TIME, LAMBDA_ARRIVAL, PRIORITY_PROB, LAMBDA_SERVICE)

print("Seleccione el tipo de sistema:")
print("1. Estaciones genéricas (todas atienden a todos)")
print("2. Una estación exclusiva para prioridad")
opcion = input("Ingrese 1 o 2: ").strip()

if opcion == "1":
    tipo = "generic"
elif opcion == "2":
    tipo = "exclusive"
else:
    print("Opción no válida. Se usará 'generic' por defecto.")
    tipo = "generic"

served, maxQueue, usage = Simulate(people, NUM_STATIONS, tipo, TOTAL_TIME)
metrics = CalculateMetrics(served, maxQueue, usage, TOTAL_TIME, NUM_STATIONS)

if tipo == "generic":
    PrintMetrics("generic stations", metrics)
else:
    PrintMetrics("1 exclusive station for priority", metrics)

