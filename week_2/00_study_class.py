class Person:
    def __init__(self, param_name):
        print("I am created!", self)
        self.name = param_name

    def talk(self):
        print("MTV2003 Remember? Saying", self.name)

person_1 = Person("Britney")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 = Person("Ciccone")
print(person_2.name)
print(person_2)
person_2.talk()