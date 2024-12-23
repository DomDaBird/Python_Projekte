

class Tier:
    def __init__(self, name: str, sex: int, age: int):
        self.name = name
        self.sex = sex  # 0 für männlich, 1 für weiblich
        self.age = age

    def eat(self):
        print(f"{self.name} isst.")

    def sleep(self):
        print(f"{self.name} schläft.")

    def grow(self, years: int):
        self.age += years
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")

