

from tier import Tier

class Gorilla(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def eat(self):
        print(f"{self.name}, der Gorilla, isst Bananen.")

    def sleep(self):
        print(f"{self.name}, der Gorilla, schläft auf einem Baum.")

    def grow(self, years: int):
        self.age += years
        print(f"{self.name}, der Gorilla, ist jetzt {self.age} Jahre alt.")

    def klettern(self):
        print(f"{self.name} klettert auf einen Baum.")
