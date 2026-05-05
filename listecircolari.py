class NodoC:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None


class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None
        self.__size  = 0

    def insertLast(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__coda      = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while True:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
            if corrente == self.__testa:
                break

    def remove(self, valore):
        if self.__testa.valore == valore:
            self.removeFirst()
            return
        if self.__coda.valore == valore:
            self.removeLast()
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore:
                corrente.next = corrente.next.next
                self.__size -= 1
                return
            corrente = corrente.next

    def removeFirst(self):
        self.__testa     = self.__testa.next
        self.__coda.next = self.__testa
        self.__size -= 1

    def removeLast(self):
        corrente = self.__testa
        while corrente.next != self.__coda:
            corrente = corrente.next
        corrente.next = self.__testa
        self.__coda   = corrente
        self.__size -= 1

    def traverse(self, passi):
        corrente = self.__testa
        for i in range(passi):
            print(f"passo {i + 1}: {corrente.valore}")
            corrente = corrente.next

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while True:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
            if corrente == self.__testa:
                break
        return "CircularLinkedList([" + " → ".join(elementi) + " → ...])"


turni = CircularLinkedList()

turni.insertLast("alice")
turni.insertLast("bob")
turni.insertLast("carlo")
print(turni)

turni.traverse(6)

turni.insertAfter("bob", "diana")
print(turni)

turni.traverse(8)

turni.remove("bob")
print(turni)

turni.traverse(6)

print(f"Analisti nel team: {turni.size()}")