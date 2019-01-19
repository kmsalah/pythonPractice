class Animal:
	def __init__(self, name, animType):
		self.name = name
		self.type = animType
		self.order = 0
	def setOrder(self, order):
		self.order = order
	def bark(self):
		print(self.name + ', ' + str(self.order))


class AnimalShelter:
	def __init__(self):
		self.dogs = []
		self.cats = []
		self.order = 0

	def enqueue(self, animal):
		self.order += 1
		animal.setOrder(self.order)
		if animal.type == "DOG":
			self.dogs.insert(0, animal)
		elif animal.type == "CAT":
			self.cats.insert(0, animal)
		else:
			return "WE ONLY ACCEPT DOGS AND CATS!!!"

	def dequeueAny(self):
		if len(self.dogs) == 0: #no dogs, so dequeue cats
			self.dequeueCat()
		if len(self.cats) == 0:
			self.dequeueDog()
		firstDog = self.peakDog()
		firstCat = self.peakCat()

		if firstDog and firstCat:
			if firstDog.order < firstCat.order:
				return self.dequeueDog()
			else:
				return self.dequeueCat()

	def dequeueCat(self):
		if len(self.cats) != 0:
			cat = self.cats.pop()
			return cat.name

	def dequeueDog(self):
		if len(self.dogs) != 0:
			dog = self.dogs.pop()
			return dog.name

	def peakCat(self):
		if len(self.cats) > 0:
			return self.cats[0]
		return None

	def peakDog(self):
		if len(self.dogs) > 0:
			return self.dogs[0]
		return None

	def printList(self):
		for d in self.dogs:
			d.bark()
		for c in self.cats:
			c.bark()


d1 = Animal("d1","DOG")
d2 = Animal("d2","DOG")
d3 = Animal("d3","DOG")
d4 = Animal("d4","DOG")

c1 = Animal("c1","CAT")
c2 = Animal("c2","CAT")
c3 = Animal("c3","CAT")
c4 = Animal("c4","CAT")

shelter = AnimalShelter()
shelter.enqueue(d1)
shelter.enqueue(c1)
shelter.enqueue(d2)
shelter.enqueue(c2)
shelter.enqueue(d3)
shelter.enqueue(c3)
shelter.enqueue(d4)
shelter.enqueue(c4)
#shelter.printList()

print(shelter.dequeueCat())
print(shelter.dequeueAny())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
print(shelter.dequeueCat())
print(shelter.dequeueAny())
print(shelter.dequeueCat())
print(shelter.dequeueDog())













