from Pojisteni import Pojisteni

class PojisteniManager:
    def __init__(self):
        self.pojisteni_list = []

    def pridej_pojisteneho(self, pojisteni):
        self.pojisteni_list.append(pojisteni)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteni in self.pojisteni_list:
            if pojisteni.jmeno == jmeno and pojisteni.prijmeni == prijmeni:
                return pojisteni
        return None

    def __str__(self):
        return "\n".join(str(pojisteni) for pojisteni in self.pojisteni_list)