import random
import time


# --- classi bst ---
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


# --- classi linkedlist ---
class NodoLL:
    def __init__(self, valore):
        self.valore = valore
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, valore):
        nuovo = NodoLL(valore)
        nuovo.next = self.head
        self.head = nuovo

    def search(self, valore):
        corrente = self.head
        while corrente:
            if corrente.valore == valore:
                return True
            corrente = corrente.next
        return False


lista_numeri = [random.randint(1, 10000) for i in range(1000)]

mio_albero = BST()
mia_lista = LinkedList()

for n in lista_numeri:
    mio_albero.insert(n)
    mia_lista.insert(n)

da_cercare = lista_numeri[499]

inizio1 = time.perf_counter()
mia_lista.search(da_cercare)
fine1 = time.perf_counter()
tempo_lista = fine1 - inizio1

inizio2 = time.perf_counter()
mio_albero.search(da_cercare)
fine2 = time.perf_counter()
tempo_bst = fine2 - inizio2

print("tempo con la lista linkata:", tempo_lista)
print("tempo con il bst:", tempo_bst)

volte = tempo_lista / tempo_bst
print("il bst è stato più veloce di", volte, "volte")
