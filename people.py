# Let's start by creating two classes: one called Student and another called Instructor.
# The student class has an instance method called learn that returns "I get it!".
# The instructor class has an instance method called teach that returns "An object is an instance of a class".
# Both the instructor and the student have names. We know that instructors and students are both people. Create a parent Person class that contains the attribute name and an __init__() method to set the name.
# Both the instructor and the student should also be able to do a greeting, like "Hi, my name is so-and-so". Where's the best place to put this common method?
# Create an instance of instructor whose name is "Nadia" and call their greeting.
# Create an instance of student whose name is "Chris" and call their greeting.
# Call the teach method on your instructor instance and call the learn method on your student. Next, call the teach method on your student instance. What happens? Why doesn't that work? Leave a comment in your program explaining why.

class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def greeting(self):
        return f'Hi, my name is {self.name}.'

class Student(People):
    
    def learn(self):
        return "I get it!"

class Instructor(People):
    
    def teach(self):
        return "An object is an instance of a class."

nadia = Instructor('Nadia')
chris = Student('Chris')
print(nadia)
print(chris)
print(nadia.greeting())
print(chris.greeting())
print(nadia.teach())
print(chris.learn())
print(chris.teach())
# The teach method does not work on my student because there is no method defined for teach under my class student

