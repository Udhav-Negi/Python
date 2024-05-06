class Employee:
    def __init__(self):
        self._fname = "Udhav"
        self.lname = "Negi"
    
    # getter method called
    @property
    def fname(self):
        return self._fname
    
    # setter
    @fname.setter
    def fname(self, value):
        self._fname = value

obj = Employee()

obj.fname = "Dhruv"
print(obj.fname)