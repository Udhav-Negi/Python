class Person:
    def __init__(self, n, o) :
        print("Hey I am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harry", "Developer")
b = Person("Divya", "HR")
c = Person()
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()