'''
Срез. Напишите код, который все элементы массива

x с четными индексами переставит в обратном порядке.

Т.е. если x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], то код должен

сформировать [8, 1, 6, 3, 4, 5, 2, 7, 0, 9].

replace

Замена каждого следующего элемента массива на не чётное
'''





list = []
for i in range(10):
	list.append(i)
	'''
	if(i % 2 != 0):
		ne.append(i)
	if(i % 2 == 0):
		ch.append(i)
	list = ne + ch
	'''
	
'[1, 3, 5, 7, 9, 0, 2, 4, 6, 8]'

list[::2] = list[::2][::-1]
print(list)

'''
print(ne)
print(ch)
print(list)
print(arr)
'''

'''
if(x[i] % 2 != 0):
	list = list(x[i])
	list.replace(ne, ch)
print(x)
	
'''


	
	
