class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta


class Dottore(Persona):
    def __init__(self, nome, cognome, eta, specializzazione, matricola, reparto):
        super().__init__(nome, cognome, eta)
        self.specializzazione = specializzazione
        self.matricola = matricola
        self.reparto = reparto
        self.pazienti = []

    def inserisci_paziente(self, nuovo_paziente):
        self.pazienti.append(nuovo_paziente)
        print(f"il paziente {nuovo_paziente.nome} aggiunto al dottor {self.cognome} {self.nome}")

    def visualizza_pazienti(self):
        nomi_pazienti = [p.cognome for p in self.pazienti]
        lista_testo = ", ".join(nomi_pazienti)
        print(f"il dottor {self.cognome} ha questi pazienti: {lista_testo}")
        if not nomi_pazienti:
            print(f"Il dottor {self.cognome} {self.nome} non ha pazienti")


class Paziente(Persona):
    def __init__(self, nome, cognome, eta, id, gruppo_sanguigno, patologie, allergie):
        super().__init__(nome, cognome, eta)
        self.id = id
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = []
        self.allergie = []


paziente1 = Paziente("Dario", "Spadola", 23, "01", "0 negativo", "nessuna", "graminacee")
paziente2 = Paziente("MariaFrancesca", "Amato", 22, "02", "AB", "stupida", "polline")
dottore1 = Dottore("Mattia", "Albensi", 88, "oncologo", 456, "A1")
dottore2 = Dottore("Alfio", "Sorbello", 21, "oculista", 567, "BC")

dottore1.inserisci_paziente(paziente1)

dottore1.visualizza_pazienti()
dottore2.visualizza_pazienti()
