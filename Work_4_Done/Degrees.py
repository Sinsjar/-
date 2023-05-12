import matplotlib.pyplot as plt
from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt
import numpy as np


delta = 1.0

x= linspace(-5,5,11)
y = x**2+delta*(rand(11)-0.5)

x+= delta*(rand(11)-0.5)

x.tofile('x_data.txt','\n')
y.tofile('y_data.txt','\n')

x = fromfile('x_data.txt', float, sep='\n')
y = fromfile('y_data.txt', float, sep='\n')


# Задаём вектор m
m_3 = vstack((x**3, x**2, x, ones(11))).T
m_2 = vstack((x**2, x, ones(11))).T
m_1 = vstack((x, ones(11))).T

# Находим коэффициенты при сост вектора m
s_3 = np.linalg.lstsq(m_3,y,rcond = None)[0]
s_2 = np.linalg.lstsq(m_2, y, rcond = None)[0]
s_1 = np.linalg.lstsq(m_1, y, rcond = None)[0]

# На отрезке
x_prec_3= linspace(-32, 30, 101)
x_prec_2 = linspace(-14, 10, 101)
x_prec_1 = linspace(-5, 5, 101)

# Отрисовка точек
plt.plot(x, y, 'D')

# Отрисовка кривой
# ax^3 + bx^2 + cx + d
plt.plot(x_prec_3,(s_3[0]*x_prec_3**3)+(s_3[1]*x_prec_3**2)+(s_3[2]*x_prec_3)+s_3[3],'-',lw=3)

plt.grid()
plt.savefig("Полином степени 3.png")
plt.show()

plt.plot(x, y, 'D')
#ax^2 + bx + c
plt.plot(x_prec_2, s_2[0] * x_prec_2**2 + s_2[1] + s_2[2],'-',lw=2)
plt.grid()
plt.savefig("Полином степени 2.png")
plt.show()



plt.plot(x, y, 'D')
#ax^2 + bx + c
plt.plot(x_prec_1, s_1[0] * x_prec_1**2 + s_1[1] ,'-', lw=1)
plt.grid()
plt.savefig("Полином степени 1.png")
plt.show()
