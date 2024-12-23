

from tier import Tier

class Tiger(Tier):
    num_appendages = 4
    is_cold_blooded = False
    is_mammal = True

    def eat(self):
        print(f"{self.name}, der Tiger, reißt seine Beute und isst.")

    def sleep(self):
        print(f"{self.name}, der Tiger, schläft in seiner Höhle.")

    def grow(self, years: int):
        self.age += years
        print(f"{self.name}, der Tiger, ist jetzt {self.age} Jahre alt.")

    def roar(self):
        print(f"{self.name} brüllt laut!")
