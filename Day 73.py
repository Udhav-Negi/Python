class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        print(f"The name of the wmployee is ")

e = Employee()
print(e.name)
print(len(e))