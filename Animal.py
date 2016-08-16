class Animal(object):
	"""docstring for Animal"""

	def run(self):
		print 'Animal is running'

class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print 'dog is running'

	def eat(self):
		print 'Eating meat...'

	
class Cat(Animal):
	"""docstring for Cat"""
	def run(self):
		print 'Cat is running'

def run_twice(Animal):
	Animal.run()
	Animal.run()

class Tortoise(Animal):
	"""docstring for Tortoise"""
	def run(self):
		print 'Tortoise is running slowly...'
		


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# dog=Dog()
# dog.run()

# cat=Cat()
# cat.run()
		
		
		