from Person import Person
from Student import Student
from Lecturer import Lecturer


myPerson1 = Person("Ivan", "Petrov", 30, "BG")
myPerson2 = Person("Bob", "Lo", 30, "UK")
myPerson3 = Person("Jon", "K", 30, "USA")
myPerson1.print()
myPerson2.print()
myPerson3.print()

print()
myStrudent1 = Student("Miroslava", "Al", 21, "BG", "UNSS", 3)
myStrudent2 = Student("Bob", "Lo", 30, "UK", "TU", 3)
myStrudent3 = Student("Jon", "K", 30, "USA", "SU", 3)
myStrudent1.print()
myStrudent2.print()
myStrudent3.print()

print()
myLecturer1 = Lecturer("Aziv", "Cappy", 59, "BG", "SU", 35)
myLecturer2 = Lecturer("Angel", "Dimitriev", 26, "BG", "SU", 5)
myLecturer3 = Lecturer("Minko", "Markov", 45, "BG", "SU", 15)
myLecturer1.print()
myLecturer2.print()
myLecturer3.print()

