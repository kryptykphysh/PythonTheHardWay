# ex042.py

## Animal is-a object (yes, sort of confusin) look at the the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## A Dog has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## A Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = none

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name, because an Employee is-a Person	
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	