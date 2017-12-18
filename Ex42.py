## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## has-a name
        self.name = name

## is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ##has-a name
        self.name = name

## is-a object
class Person(object):

    def __init__(self,name):
        ##has-a name
        self.name = name

        ## Person has-a pet of some kind

        self.pet = None

## is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##has-a name
        super(Employee, self).__init__(name)
        ##has-a salary
        self.salary = salary

## is-a object
class Fish(object):
    pass

##is-a Fish
class Salmon(Fish):
    pass

##is-a Fish
class Halibut(Fish):
    pass

##rover is-a dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##Marys pet has-a name satan
mary.pet = satan

##Frank has a salary of 120000 and has a name Frank
frank = Employee("Frank", 120000)

##frank has-a pet rover
frank.pet = rover

##flipper is-a fish
flipper = Fish()
