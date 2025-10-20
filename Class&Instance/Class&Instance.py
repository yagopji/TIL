class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("Hello! " + to_name + " I'm", self.name)

    def introduce(self):
        print("My name is " + self.name + " I'm " + str(self.age) + " years old.")

class Police(Person):
    def arrest(self, to_arrest):
        print("You are under arrest, " + to_arrest + "!")

class Programmer(Person):
    def program (self, to_program):
        print("What should I do? I'll do it: " + to_program)    

Tommy = Person("Tommy", 20)
Jenny = Police("Jenny", 25)
Michael = Programmer("Michael", 30)

Tommy.say_hello("Jenny")
Tommy.introduce()
Jenny.introduce()
Jenny.arrest("Tommy")
Michael.introduce()
Michael.program("Make a game")