class Nodo:
    def __init__(self, v):
        self.v = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.testa = None

    def insertLast(self, v):
        n = Nodo(v)
        if not self.testa: self.testa = n; return
        c = self.testa
        while c.next: c = c.next
        c.next = n

    def insertAfter(self, rif, v):
        c = self.testa
        while c:
            if c.v == rif:
                n = Nodo(v); n.next = c.next; c.next = n; return
            c = c.next

    def insertBefore(self, rif, v):
        if self.testa.v == rif:
            n = Nodo(v); n.next = self.testa; self.testa = n; return
        c = self.testa
        while c.next:
            if c.next.v == rif:
                n = Nodo(v); n.next = c.next; c.next = n; return
            c = c.next

    def removeFirst(self):
        self.testa = self.testa.next

    def removeLast(self):
        c = self.testa
        while c.next.next: c = c.next
        c.next = None

    def size(self):
        c, n = self.testa, 0
        while c: n += 1; c = c.next
        return n

    def peekFirst(self): return self.testa.v

    def __repr__(self):
        c, els = self.testa, []
        while c: els.append(c.v); c = c.next
        return "LinkedList([" + " → ".join(els) + "])"


cronologia = LinkedList()

cronologia.insertLast("admin")
cronologia.insertLast("mario")
cronologia.insertLast("sara")
print(cronologia)

cronologia.insertAfter("mario", "guest")
print(cronologia)

cronologia.insertBefore("admin", "root")
print(cronologia)

cronologia.insertBefore("sara", "luca")
print(cronologia)

cronologia.removeFirst()
print(cronologia)

cronologia.removeLast()
print(cronologia)

print(f"Modifiche registrate: {cronologia.size()}")
print(f"Prima modifica: {cronologia.peekFirst()}")