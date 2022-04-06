#Работа по классам на парах. Классы, классы наследники, деструкторы, уникальные методы, декораторы.
def decoration(wrapped):
	def wrapper(self):
		print ('Loading...')
		wrapped(self)
		print ('Im the First class!')
	return wrapper
def decoration2(wrapped):
	def wrapper(self):
		print ('Wait a bit...')
		wrapped(self)	
	return wrapper
def decoration3(wrapped):
	def wrapper(self):
		print ('Universal wrapper for class 2 and 3')
		wrapped(self)
	return wrapper
def next():
	print ("\n=================\n")
class Person:
	def  __init__ (self, name, age):
		self.name=name
		self.age=age
	def say(self,message):
		print(message)
	@decoration
	def say_hello(self):
		print('Hello')
	def display_info(self):
		print (f"Name: {self.name} / Age: {self.age}")
	def __str__(self):
		print('Переводим в строку...')
		return 'Имя: ' + str(self.name) + '\tВозраст: ' + str(self.age)
	def __del__(self):
		print(f"{self.name} более не используется и был удалён.")

class Student(Person):
	def __init__(self, name, age, avg):
		Person.__init__(self, name, age)
		self.avg = avg
	def __str__(self):
		return 'Имя: ' + str(self.name) + '\tВозраст: ' + str(self.age) + '\tСредний балл: ' + str(self.avg)
	@decoration3
	def info_sec(self):
		print ('Hey. Im the second class. But this text can be used in the next ones.')
	@decoration2
	def fordec(self):
		print ('Finally here.')

class Something(Student):
	def __init__(self, name, age, avg, something):
		Student.__init__(self, name, age, avg)
		self.something = something
	def info(self):
		print ('^ previous class and im the third')
	def __str__(self):
		return 'Имя: ' + str(self.name) + '\tВозраст: ' + str(self.age) + '\tСредний балл: ' + str(self.avg) + '\tSomething: ' + str(self.something)

print('Тут находится начало, а ещё', 'Тут находится начало\n'.count(' '), 'пробела мы насчитали в первой части предложения :) \n')
p1 = Person('Tom', 28)
p1.say_hello()
p1.say('!!!')
p1.display_info()
p2 = Person('Jerry', 53)
p2.display_info()
next()
print ('Исправляем возраст...\n')
p2.age = p2.age + 19
print('Исправленный возраст: ')
p2.display_info()
next()
print (p1)
print (p2)
next()
del p1
del p2
next()
s1 = Student('Second', 2, 2)
print(s1)
s1.info_sec()
s1.fordec()
next()
smth = Something('Third', 3, 3, 'Smth')
print(smth)
smth.info_sec()
smth.info()
next()