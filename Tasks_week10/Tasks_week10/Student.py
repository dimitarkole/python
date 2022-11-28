from Person import Person

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearOfStydy = 0):
        Person.__init__(self, name, family, age, nationality)
        self.university=university
        self.yearOfStydy=yearOfStydy
        self.wellcom()

    def wellcom(self):
        print(f"Wellcom {self.name} {self.family} to {self.university}")


    def print(self):
        print(f"Student: {self.name} {self.family} {self.age} {self.university} {self.yearOfStydy}")
