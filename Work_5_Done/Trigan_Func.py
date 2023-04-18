import math as m
class Trigan():
	#x = int(input())
	def __init__(self, x): #Конструктор
		self.x = x
		
	def cos(self):
		print("Вычисление косинуса")
		print(m.cos(self.x))

	def sin(self):
		print("Вычисление синуса")
		print(m.sin(self.x))
			
	def tan(self):
		print("Вычисление тангенса")
		print(m.sin(self.x)/m.cos(self.x))
		
	def arcsin(self):
		print("Вычисление арксинуса")
		print(m.asin(self.x))
		
	def arccos(self):
		print("Вычисление арккосинуса")
		print(m.acos(self.x))
		
	def arctan(self):
		print("Вычисление арктангенса")
		print(m.atan(self.x))
		
	def degree_to_rad(self):
		print("Перевод из градусов в радианы")
		print(m.radians(self.x))



x = int(input())
t = Trigan(x) # Объект экземпляра класса

t.cos()
t.sin()
t.tan()

if(-1 < x <= 1):
	t.arcsin()
	t.arccos()

t.arctan()
t.degree_to_rad()
