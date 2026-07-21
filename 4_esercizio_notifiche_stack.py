class Notifiche:
    def __init__(self):
        self.notifiche = []

    def arriva(self, notifica):
        self.notifiche.append(notifica)

    def leggi(self):
        if not self.notifiche:
            return "non hai notifiche nel tuo galaxy"
        return self.notifiche.pop()

    def prossima(self):
        if not self.notifiche:
            return "nessuna notifica."
        return self.notifiche[-1]

    def leggi_tutte(self):
        while self.notifiche:
            print(f"letta: {self.leggi()}")


galaxy = Notifiche()

galaxy.arriva("whatsapp - mario: ciao, giochiamo a rocket?")
galaxy.arriva("whatsapp - francesca: usciamo questa sera?")
galaxy.arriva("gmail - its: farai una settimana di assenza")

print(galaxy.notifiche)
print(galaxy.prossima())
print(galaxy.leggi())
print(galaxy.leggi())
print(galaxy.leggi())
