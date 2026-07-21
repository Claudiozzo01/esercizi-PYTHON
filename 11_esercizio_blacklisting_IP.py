import ipaddress
import random
import time
from collections import deque


class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left = None
        self.right = None


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
        return self.__searchRicorsivo(nodo.right, valore)


def ipToInt(ip):
    return int(ipaddress.ip_address(ip))


def intToIp(n):
    return str(ipaddress.ip_address(n))


lista_ip_stringa = [f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}" for i in range(1000)]
lista_ip_interi = [ipToInt(ip) for ip in lista_ip_stringa]

mio_bst = BST()
for ip_int in lista_ip_interi:
    mio_bst.insert(ip_int)

da_bloccare = random.sample(lista_ip_stringa, 10)
da_far_passare = [f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}" for i in range(10)]

tutti_gli_ip = da_bloccare + da_far_passare
random.shuffle(tutti_gli_ip)

coda_router = deque()

for ip in tutti_gli_ip:
    pacchetto = {
        "ip_sorgente": ip,
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(1024, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": 1500,
    }
    coda_router.append(pacchetto)

bloccati = 0
permessi = 0

print("--- inizio controllo pacchetti ---")
while len(coda_router) > 0:
    p = coda_router.popleft()
    ip_da_testare = p["ip_sorgente"]
    ip_int = ipToInt(ip_da_testare)

    if mio_bst.search(ip_int):
        print(f"IP: {ip_da_testare} | Porta: {p['porta_sorgente']} -> BLOCCATO")
        bloccati += 1
    else:
        print(f"IP: {ip_da_testare} | Porta: {p['porta_sorgente']} -> PERMESSO")
        permessi += 1

print("\n--- riepilogo finale ---")
print("totale bloccati:", bloccati)
print("totale permessi:", permessi)

ip_test_stringa = tutti_gli_ip[0]
ip_test_int = ipToInt(ip_test_stringa)

inizio_lista = time.perf_counter()
if ip_test_int in lista_ip_interi:
    pass
fine_lista = time.perf_counter()
t_lista = fine_lista - inizio_lista

inizio_bst = time.perf_counter()
mio_bst.search(ip_test_int)
fine_bst = time.perf_counter()
t_bst = fine_bst - inizio_bst

print("\n--- test prestazioni ---")
print("tempo lista:", t_lista)
print("tempo bst:", t_bst)
if t_bst > 0:
    print("differenza di velocità:", t_lista / t_bst, "volte")
