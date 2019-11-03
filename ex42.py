## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class name is Dog which has object named Animal
class Dog(Animal):
    def __init__(self, name):
        ## calling name
        self.name = name


##class name is cat which has object Animal
class Cat(Animal):

    def __init__(self, name):
        ## calling name
        self.name = name

#class name is person having object
class Person(object):

    def __init__(self, name):
        #calling name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

## class name is Employee having object Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        # calling salary
        self.salary = salary


# class name Fish with object
class Fish(object):
    pass

# class name Salmon with object Fish
class Salmon(Fish):
    pass

# class name Halibut with object fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

#mary is-a person
mary = Person("mary")

# satan is mary's pet
mary.pet = satan

#frank is an Employee with salary 120000
frank = Employee("Frank", 120000)

#rover is franks pet
frank.pet = rover

#flipper is a Fish
flipper = Fish()

#crouse is a salmon
crouse = Salmon()

#harry is a Halibut()
harry = Halibut()


