"""
=====================================================================
   OBJECT-ORIENTED PYTHON  -  A HANDS-ON COURSE
=====================================================================

HOW TO USE THIS FILE (read me first!)
-------------------------------------
1. Read the explanation of each module. The EXAMPLE of each module
   is also commented: select it, press Ctrl + /  and run the file to
   see it work. Comment it back afterwards.
2. Every EXERCISE is written as a block of comments.
   To try it:
      - Select the whole exercise block with your mouse
      - Press  Ctrl + /   (Cmd + /  on Mac)  -> the block becomes code
      - Write your solution in the "YOUR CODE" area
      - Run the file and check the TEST lines
3. When you finish, select the block again and press Ctrl + /  to
   comment it back, so the file keeps running without errors.
4. Lines starting with "##" are instructions: they stay harmless
   comments even after you uncomment the block.
5. Every exercise is independent: write all the code it needs again
   inside the block (do not rely on a previous exercise).

Rule of the game: do not look for the solution on the Internet first.
Read the error message, think, try again. Errors are your teachers!

Requirements: Python 3.8+  and basics (variables, if, loops, functions,
lists, dictionaries).
=====================================================================
"""

import random
from abc import ABC, abstractmethod


def title(text):
    """Small helper that prints a nice banner for live examples."""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


# =====================================================================
# MODULE 1 : CLASSES AND OBJECTS
# =====================================================================
# A CLASS is a blueprint (a recipe, a cookie cutter).
# An OBJECT (or INSTANCE) is a real thing built from that blueprint.
#
# Vocabulary:
#   class       -> the blueprint
#   object      -> one thing made from it
#   instantiate -> to create an object:   rex = Dog()
#
# Naming convention: classes use CamelCase (Dog, BankAccount),
# variables and functions use snake_case.

# title("MODULE 1 - Classes and objects")


# class Dog:
#     pass


# rex = Dog()   # object number 1
# luna = Dog()  # object number 2
# print(type(rex))
# print(rex is luna)  # False: two different objects

# ---------------------------------------------------------------------
# EXERCISE 1.1  (uncomment the block to try it)
# ---------------------------------------------------------------------
## Create an empty class called Car.
## Create two cars: car1 and car2.
## Print the type of car1.
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## print(type(car1))   # should mention Car
## print(car1 is car2) # should print False

# EXERCISE 1.2 (just think, no code)
# Give 3 classes from real life and 2 objects for each one.
# Example: class Phone -> my phone, your phone.


# =====================================================================
# MODULE 2 : ATTRIBUTES AND THE CONSTRUCTOR  __init__
# =====================================================================
# ATTRIBUTES are the DATA of an object (what it HAS).
# __init__ is the CONSTRUCTOR: Python runs it automatically at the
# moment the object is created, to give it its starting data.
# "self" means "this particular object".
#
# COMMON MISTAKE: writing  name = name  instead of  self.name = name

# title("MODULE 2 - Attributes and __init__")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# rex = Dog("Rex", 3)
# print(rex.name, rex.age)
# rex.age = 4  # attributes can be changed later
# print(rex.name, "is now", rex.age)

## Default values work like in functions:
##   def __init__(self, name, age=1):

# ---------------------------------------------------------------------
# EXERCISE 2.1
# ---------------------------------------------------------------------
## Create a class Student with attributes: name, grade (0 to 20)
## and school. The school must have the default value "Lycee".
## Create 3 students (one of them with another school) and print
## their name, grade and school.
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## s1 = Student("Sara", 15)
## s2 = Student("Omar", 12, "College")
## print(s1.school)   # Lycee
## print(s2.school)   # College


# =====================================================================
# MODULE 3 : METHODS (THE BEHAVIOURS)
# =====================================================================
# METHODS are functions inside a class. They describe what an object
# can DO. They use and modify the object's attributes through "self".
# The first parameter of a method is ALWAYS self.

# title("MODULE 3 - Methods")


# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 10

#     def bark(self):
#         print(f"{self.name} says Woof!")

#     def run(self, minutes):
#         self.energy -= minutes


# rex = Dog("Rex")
# rex.bark()
# rex.run(3)
# print("Energy left:", rex.energy)

# ---------------------------------------------------------------------
# EXERCISE 3.1
# ---------------------------------------------------------------------
## Create a class BankAccount. The balance starts at 0.
## Methods:
##   deposit(amount)   -> adds money
##   withdraw(amount)  -> removes money, but if there is not enough
##                        money, print "Not enough money" and change
##                        nothing
##   show_balance()    -> prints the balance
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## acc = BankAccount()
## acc.deposit(100)
## acc.withdraw(30)
## acc.show_balance()   # 70
## acc.withdraw(500)    # Not enough money
## acc.show_balance()   # still 70


# =====================================================================
# MODULE 4 : MAGIC METHODS  (__str__ and friends)
# =====================================================================
# Python has special methods surrounded by double underscores.
# They let YOU decide how objects behave with Python's built-in tools.
#
#   __str__(self)         -> what print(obj) displays
#   __eq__(self, other)   -> what  obj1 == obj2  means
#   __lt__(self, other)   -> what  obj1 < obj2   means (used by sorted)
#
# Without __str__ you get an ugly  <__main__.Dog object at 0x...>

# title("MODULE 4 - Magic methods")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Dog({self.name}, {self.age} years)"

#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age


# print(Dog("Rex", 3))
# print(Dog("Rex", 3) == Dog("Rex", 3))  # True thanks to __eq__

# ---------------------------------------------------------------------
# EXERCISE 4.1
# ---------------------------------------------------------------------
## Write a class Student (name, grade).
## Add __str__ so that print(student) shows:   Sara - grade 15/20
## Add __eq__ so two students are equal when they have the
## same name AND the same grade.
## BONUS: add __lt__ so students can be compared by grade, then
## sort a list of students with sorted().
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## a = Student("Sara", 15)
## b = Student("Sara", 15)
## c = Student("Omar", 9)
## print(a)           # Sara - grade 15/20
## print(a == b)      # True
## print(a == c)      # False


# =====================================================================
# MODULE 5 : ENCAPSULATION (protect your data)
# =====================================================================
# Some data must not be changed carelessly: a bank balance should
# never become -5000 by accident.
#
# Convention: an attribute starting with _ means "private, please do
# not touch it directly".
# A PROPERTY lets us control reading and writing while the outside
# code still uses the simple syntax  obj.value

# title("MODULE 5 - Encapsulation")


# class Thermometer:
#     def __init__(self):
#         self._celsius = 20

#     @property
#     def celsius(self):  # reading:  t.celsius
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):  # writing: t.celsius = 30
#         if value < -273:
#             print("Impossible temperature!")
#         else:
#             self._celsius = value


# t = Thermometer()
# t.celsius = 35
# print(t.celsius)
# t.celsius = -500  # refused
# print(t.celsius)

# ---------------------------------------------------------------------
# EXERCISE 5.1
# ---------------------------------------------------------------------
## Create a class Player with a private attribute _health
## (starts at 100).
## Use a property "health" whose setter keeps the value between
## 0 and 100:
##    above 100 -> becomes 100
##    below 0   -> becomes 0
## Add a READ-ONLY property is_alive (True when health > 0).
## (A property with no setter cannot be modified.)
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## p = Player()
## p.health = 150
## print(p.health)     # 100
## p.health = -20
## print(p.health)     # 0
## print(p.is_alive)   # False
## p.is_alive = True   # should raise an error (AttributeError)


# =====================================================================
# MODULE 6 : CLASS ATTRIBUTES, @classmethod, @staticmethod
# =====================================================================
# An instance attribute belongs to ONE object.
# A CLASS ATTRIBUTE is SHARED by ALL objects of the class.
#
# @classmethod  -> receives the class (cls), can use class data
# @staticmethod -> receives nothing special; a utility function that
#                  logically belongs to the class

# title("MODULE 6 - Class attributes and methods")


# class Dog:
#     species = "Canis familiaris"  # shared by all dogs
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Dog.count += 1  # one more dog in the world

#     @classmethod
#     def how_many(cls):
#         return cls.count

#     @staticmethod
#     def bark_sound():
#         return "Woof"


# Dog("Rex")
# Dog("Luna")
# print("Dogs created:", Dog.how_many())
# print(Dog.species, "-", Dog.bark_sound())

# ---------------------------------------------------------------------
# EXERCISE 6.1
# ---------------------------------------------------------------------
## Write a class Student (name, grade).
## Add a class attribute total_students that increases every time
## a student is created.
## Add a @classmethod get_total() that returns it.
## Add a @staticmethod is_passing(grade) that returns True if the
## grade is 10 or more.
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## Student("Sara", 15)
## Student("Omar", 8)
## print(Student.get_total())        # 2
## print(Student.is_passing(12))     # True
## print(Student.is_passing(7))      # False


# =====================================================================
# MODULE 7 : INHERITANCE  ("is a")
# =====================================================================
# A class can INHERIT from another one to reuse its code.
#   parent class = base class      child class = subclass
# Relationship test: "A Dog IS AN Animal" -> inheritance makes sense.
#
# super() gives access to the parent class (very often used to call
# the parent's __init__).

# title("MODULE 7 - Inheritance")


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")


# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Woof!")


# class Cat(Animal):
#     def __init__(self, name, indoor):
#         super().__init__(name)  # let Animal handle the name
#         self.indoor = indoor


# rex = Dog("Rex")
# rex.eat()   # inherited from Animal
# rex.bark()  # specific to Dog
# tom = Cat("Tom", True)
# tom.eat()
# print(isinstance(rex, Animal))  # True

# ---------------------------------------------------------------------
# EXERCISE 7.1
# ---------------------------------------------------------------------
## Create a class Vehicle with attributes brand and speed and a
## method move() that prints "<brand> is moving at <speed> km/h".
## Create Car(Vehicle) and Bike(Vehicle).
## Bike has an extra attribute has_bell (use super().__init__).
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## c = Car("Toyota", 120)
## b = Bike("BMX", 20, True)
## c.move()
## b.move()
## print(b.has_bell)   # True

# ---------------------------------------------------------------------
# EXERCISE 7.2
# ---------------------------------------------------------------------
## Create Person (name, age) with a method introduce().
## Create Student(Person) with an extra attribute school and
## Teacher(Person) with an extra attribute subject.
## Create one of each and call introduce() on both.
##
## ---- YOUR CODE BELOW ----
#
#
#


# =====================================================================
# MODULE 8 : POLYMORPHISM AND OVERRIDING
# =====================================================================
# Poly = many, morph = forms.
# A child class can OVERRIDE (redefine) a method of its parent.
# Different classes then answer to the SAME method name in DIFFERENT
# ways, and the code that calls the method does not need to know
# which exact class it is talking to.

# title("MODULE 8 - Polymorphism")


# class Animal:
#     def speak(self):
#         print("...")


# class Dog(Animal):
#     def speak(self):
#         print("Woof!")


# class Cat(Animal):
#     def speak(self):
#         print("Meow!")


# for animal in [Dog(), Cat(), Animal()]:
#     animal.speak()  # same call, different behaviours

# ---------------------------------------------------------------------
# EXERCISE 8.1
# ---------------------------------------------------------------------
## Create a parent class Shape with a method area() returning 0.
## Create Rectangle (width, height) and Circle (radius) that
## override area().  (Use 3.14 for pi.)
## Put several shapes in a list and print the total area with a loop.
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## shapes = [Rectangle(2, 3), Circle(1), Rectangle(4, 5)]
## total = 0
## for s in shapes:
##     total += s.area()
## print(total)   # 29.14

# ---------------------------------------------------------------------
# EXERCISE 8.2
# ---------------------------------------------------------------------
## Add __str__ to Rectangle and Circle so printing a shape shows its
## type and its area, for example:  Circle with area 3.14
##
## ---- YOUR CODE BELOW ----
#
#
#


# =====================================================================
# MODULE 9 : COMPOSITION  ("has a")
# =====================================================================
# Not everything must be inheritance!
#    "is a"  -> inheritance   (a Dog IS AN Animal)
#    "has a" -> composition   (a Car HAS AN Engine)
# Composition = an object stored INSIDE another object.

# title("MODULE 9 - Composition")


# class Engine:
#     def __init__(self, power):
#         self.power = power

#     def start(self):
#         print(f"Engine of {self.power} hp started")


# class Car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine  # a Car HAS an Engine

#     def start(self):
#         print(f"{self.brand} is starting...")
#         self.engine.start()  # the Car asks its Engine to work


# Car("Toyota", Engine(110)).start()

# ---------------------------------------------------------------------
# EXERCISE 9.1
# ---------------------------------------------------------------------
## Create a class Book (title, author).
## Create a class Library that has a list of books (starts empty)
## and the methods:
##    add_book(book)
##    find_by_author(author)  -> returns a list of matching books
##    show_all()              -> prints every title
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## lib = Library()
## lib.add_book(Book("Dune", "Herbert"))
## lib.add_book(Book("Emma", "Austen"))
## lib.add_book(Book("Persuasion", "Austen"))
## lib.show_all()
## print(len(lib.find_by_author("Austen")))   # 2

# EXERCISE 9.2 (just think, no code)
# For each pair write "is a" or "has a":
#   Teacher / Person      School / Student      Laptop / Battery
#   Square / Rectangle    Team / Player         Dog / Animal


# =====================================================================
# MODULE 10 : ABSTRACT CLASSES (bonus)
# =====================================================================
# Sometimes a parent class is only a TEMPLATE and must never be
# created directly. With the abc module, we can force every child to
# implement certain methods.

# title("MODULE 10 - Abstract classes")


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2


# print(Square(4).area())
## Shape()  -> TypeError: can't instantiate an abstract class

# ---------------------------------------------------------------------
# EXERCISE 10.1
# ---------------------------------------------------------------------
## Create an abstract class Employee with the abstract method
## salary().
## Create FullTimeEmployee (fixed monthly salary) and
## Freelancer (hours worked x hourly rate).
## Check that Employee() raises an error.
##
## ---- YOUR CODE BELOW ----
#
#
#
## ---- TESTS ----
## print(FullTimeEmployee(2000).salary())   # 2000
## print(Freelancer(10, 25).salary())       # 250


# =====================================================================
# CHEAT SHEET
# =====================================================================
# Class / object ... class Dog: / rex = Dog()        blueprint vs thing
# Constructor ...... __init__(self, ...)             setup at birth
# Attribute ........ self.name                       what it HAS
# Method ........... def bark(self):                 what it DOES
# Print display .... __str__                         how it prints
# Protection ....... _x  and  @property              guard your data
# Shared data ...... class attribute, @classmethod,
#                    @staticmethod
# Inheritance ...... class Dog(Animal), super()      "is a"
# Polymorphism ..... same method name, other result  overriding
# Composition ...... object inside an object         "has a"
# Abstraction ...... ABC + @abstractmethod           template only


# =====================================================================
# FINAL ACTIVITY : DUNGEON ARENA  (mini text RPG)
# =====================================================================
# Work in teams of 2. Build a small turn-based fight game.
# EVERY technique of the course must appear at least once.
# Do it step by step and run your code after every step!
#
# The story: two teams of heroes fight in an arena. The last team
# with a living member wins.
#
# HOW TO WORK: uncomment the skeleton below (select all + Ctrl + /),
# then complete the TODOs one step at a time.
#
# STEP 1 (modules 1-4)  Character: name, health, attack_power,
#                       attack(target), __str__  ("Aria - HP: 80").
# STEP 2 (module 5)     Private health with a property kept between
#                       0 and max_health. Read-only is_alive.
# STEP 3 (module 6)     Class attribute total_created and a
#                       @staticmethod roll_dice() (1 to 6) used to
#                       add luck to every attack.
# STEP 4 (modules 7-8)  Subclasses that OVERRIDE attack():
#                         Warrior: armor reduces the damage it takes
#                         Mage:    mana; spell = double damage but
#                                  costs mana
#                         Archer:  30% chance to hit twice
#                       Use super().__init__(...).
# STEP 5 (module 9)     Weapon (name, bonus_damage): a Character HAS
#                       a weapon. Team: HAS a list of characters,
#                       with add_member, alive_members(),
#                       is_defeated().
# STEP 6 (module 10)    Abstract class Monster with the abstract
#                       method special_move(); build Goblin and
#                       Dragon with different special moves.
# STEP 7                Game loop: teams take turns, a random living
#                       member attacks a random living enemy. Stop
#                       when a team is defeated. Print the winner and
#                       Character.total_created.
#
# CHECKLIST before showing your work:
#   [ ] class + __init__ + methods     [ ] __str__
#   [ ] property (encapsulation)       [ ] class attribute / static
#   [ ] inheritance + super()          [ ] overriding (polymorphism)
#   [ ] composition                    [ ] abstract class
#
# BONUS IDEAS: a Healer who restores teammates, __lt__ to sort
# characters by health, saving scores in a JSON file, 3 assert tests.

# ---- SKELETON (uncomment to start) ----
#
# class Character:
#     total_created = 0
#
#     def __init__(self, name, health, attack_power):
#         # TODO: store attributes, increase total_created
#         pass
#
#     @staticmethod
#     def roll_dice():
#         return random.randint(1, 6)
#
#     def attack(self, target):
#         # TODO
#         pass
#
#     def __str__(self):
#         # TODO
#         pass
#
#
# # TODO: Warrior, Mage, Archer, Weapon, Team, Monster(ABC), Goblin, Dragon
#
#
# if __name__ == "__main__":
#     # TODO: build two teams and run the game loop
#     pass
