## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self):
        self.name = None

    def speak(self):
        pass

## Dog is-an animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def speak(self):
        print "woof"

## Cat is-an Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    def speak(self):
        print "meow"

## Person is-an object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## initialize base class
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    def swim(self):
        print "swimming"

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet is satan (the Cat)
mary.pet = satan

## frank is-an Employee who is named "Frank" and whose salary is 120000
frank = Employee("Frank", 120000)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
