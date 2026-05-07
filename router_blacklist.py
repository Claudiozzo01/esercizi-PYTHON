import ipaddress
import random
import time
from collections import deque


class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None
        self.right  = None

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)

    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                nodo.right = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        if nodo is None:
            return False
        if nodo.valore == valore:
            return True
        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            return self.__searchRicorsivo(nodo.right, valore)


class Queue:
    def __init__(self):
        self.__data = deque()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)


def ipToInt(ip):
    return int(ipaddress.ip_address(ip))

def intToIp(n):
    return str(ipaddress.ip_address(n))


blacklist_ip = [f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                for _ in range(1000)]


blacklist_bst = BST()
blacklist_lista = []   

for ip in blacklist_ip:
    n = ipToInt(ip)
    blacklist_bst.insert(n)
    blacklist_lista.append(n)


ip_bloccati = random.sample(blacklist_ip, 10)


ip_permessi = []
while len(ip_permessi) < 10:
    nuovo = f"{random.randint(224,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    if nuovo not in blacklist_ip:
        ip_permessi.append(nuovo)

pacchetti = []
for ip in ip_bloccati + ip_permessi:
    pacchetto = {
        "ip_sorgente":        ip,
        "ip_destinazione":    "10.0.0.1",
        "porta_sorgente":     random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo":         "TCP",
        "dimensione":         1500
    }
    pacchetti.append(pacchetto)


random.shuffle(pacchetti)


coda_pacchetti = Queue()
for p in pacchetti:
    coda_pacchetti.enqueue(p)


print("        CONTROLLO ACCESSI ROUTER")

bloccati = 0
permessi  = 0

while not coda_pacchetti.isEmpty():
    pacchetto = coda_pacchetti.dequeue()
    ip        = pacchetto["ip_sorgente"]
    ip_intero = ipToInt(ip)

    if blacklist_bst.search(ip_intero):
        print(f" BLOCCATO  | IP: {ip} | Porta: {pacchetto['porta_sorgente']} | {pacchetto['protocollo']}")
        bloccati += 1
    else:
        print(f" PERMESSO  | IP: {ip} | Porta: {pacchetto['porta_sorgente']} | {pacchetto['protocollo']}")
        permessi += 1


print(f"  Pacchetti totali : {bloccati + permessi}")
print(f"  Bloccati         : {bloccati}")
print(f"  Permessi         : {permessi}")


ip_da_cercare    = blacklist_ip[0]
intero_da_cercare = ipToInt(ip_da_cercare)

inizio_bst = time.perf_counter()
blacklist_bst.search(intero_da_cercare)
tempo_bst  = time.perf_counter() - inizio_bst


inizio_lista = time.perf_counter()
intero_da_cercare in blacklist_lista
tempo_lista  = time.perf_counter() - inizio_lista

print(f"\nIP cercato       : {ip_da_cercare}")
print(f"Tempo BST        : {tempo_bst:.10f} secondi")
print(f"Tempo Lista      : {tempo_lista:.10f} secondi")

if tempo_bst > 0 and tempo_lista > 0:
    if tempo_lista > tempo_bst:
        volte = tempo_lista / tempo_bst
        print(f"Il BST è {volte:.2f} volte più veloce della Lista")
    else:
        volte = tempo_bst / tempo_lista
        print(f"La Lista è {volte:.2f} volte più veloce del BST")
