import math

def exp(x, y):
	return pow(math.e, x + y)
def si(x, y):
	return math.sin(x + y)
def co(x, y):
	return math.cos(x + y)
def value(x, y):
	return x ** y

print("Введите операцию под номером")
print("1 - простейшие вычисления, 2 - exp^x+y, /n, 3 - sin(x + y), 4 - cos(x + y) или 5 - x^y")
a = int(input())

if(a == 1):
	print("Вы выбрали простейшие вычисления +, -, *, /")
	print("Введите простейшие вычисления:")
	print(eval(input()))

elif(a == 2):
	print("Вы выбрали e^x+y")
	print("Введите x y")
	print(exp(int(input()), int(input())))

elif(a == 3):
	print("Вы выбрали sin(x + y)")
	print("Введите x y")
	print(si(int(input()), int(input())))
elif(a == 4):
	print("Вы выбрали cos(x+y)")
	print("Введите x y")
	print(co(int(input()), int(input())))
elif(a == 5):
	print("Вы выбрали x^y")
	print("Введите x y")
	print(value(int(input()), int(input())))
