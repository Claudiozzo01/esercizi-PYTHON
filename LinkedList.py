import random
import time


class NodoLista:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None

class LinkedList:
    def __init__(self):
        self.__testa = None

    def insert(self, valore):
        nuovo = NodoLista(valore)
        nuovo.next   = self.__testa
        self.__testa = nuovo

    def search(self, valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore:
                return True
            corrente = corrente.next
        return False


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


numeri = [random.randint(1, 10000) for _ in range(1000)]


lista = LinkedList()
albero = BST()

for n in numeri:
    lista.insert(n)
    albero.insert(n)


da_cercare = numeri[499]   
print(f"Numero da cercare: {da_cercare}")


inizio_lista = time.perf_counter()
lista.search(da_cercare)
fine_lista   = time.perf_counter()

tempo_lista = fine_lista - inizio_lista


inizio_bst = time.perf_counter()
albero.search(da_cercare)
fine_bst   = time.perf_counter()

tempo_bst = fine_bst - inizio_bst


print(f"Tempo LinkedList : {tempo_lista:.10f} secondi")
print(f"Tempo BST        : {tempo_bst:.10f} secondi")

if tempo_bst > 0 and tempo_lista > 0:
    if tempo_lista > tempo_bst:
        volte = tempo_lista / tempo_bst
        print(f"Il BST è {volte:.2f} volte più veloce della LinkedList")
    else:
        volte = tempo_bst / tempo_lista
        print(f"La LinkedList è {volte:.2f} volte più veloce del BST")