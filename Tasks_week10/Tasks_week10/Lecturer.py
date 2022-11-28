from Person import Person

class Lecturer(Person):
    def __init__(self, name, family, age,nationality, university,  experience = 0):
        Person.__init__(self, name, family, age,nationality)
        self.university=university
        self.experience=experience

    def print(self):
        print(f"Lecturer: {self.name} {self.family} {self.age} {self.university} {self.experience}")
