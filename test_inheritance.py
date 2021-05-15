# Inheritance with init funtion
class Person:
    print("Parent class")
      # Constructor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    def abc(self):
        print(self.firstname, self.lastname)

#create object of class, so that it can inherit the methods of that class
person = Person("John", "Doe")
person.abc()

person1 = Person("Jonny", "Rock")
person.abc()

class Student(Person):
    print("Child class")

    def abc1(self):
        print(self.firstname, self.lastname)

student=Student("Kane","Captain")
student.abc1()

#Inheritance without init funtion
class Animal:
    def speak(self):
        print("Animal Speaking")

    #child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()



#Multiple Inheritance
class Animal_multiple:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal_multiple):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()

#default contructor
class GeekforGeeks:
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    #another way of default constructor
    # def __init__(self,geek_name="GeekforGeeks1"):
    #     self.geek1 = geek_name

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
        #print(self.geek1)


# creating object of the class
obj = GeekforGeeks()
# calling the instance method using the object obj
obj.print_Geek()

#Parameterized Constructor
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)
# perform Addition
obj.calculate()
# display result
obj.display()
#obj.calculate()



######################################################
#Using parent class.init function in child class
# parent class
class Person():

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    # creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using its instance
a.display()

