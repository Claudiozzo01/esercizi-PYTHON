from collections import deque

fila = deque(["Mario", "Giulia", "Tonino", "Rosa"])

print("Persone in fila:", len(fila))

cliente = fila.popleft()
print("Macellaio: Avanti", cliente + "!")
print("Persone in fila:", len(fila))

cliente = fila.popleft()
print("Macellaio: Avanti", cliente + "!")
print("Persone in fila:", len(fila))

fila.append("Enzo")
print("Enzo si mette in fila")
print("Persone in fila:", len(fila))

cliente = fila.popleft()
print("Macellaio: Avanti", cliente + "!")
print("Persone in fila:", len(fila))

cliente = fila.popleft()
print("Macellaio: Avanti", cliente + "!")
print("Persone in fila:", len(fila))

cliente = fila.popleft()
print("Macellaio: Avanti", cliente + "!")
print("Persone in fila:", len(fila))

print("Negozio chiuso, a domani!")
