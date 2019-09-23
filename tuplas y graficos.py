# -*- coding: utf-8 -*-


tupla = 1, 3, 4, 6  # herencia de Python 2.X
tupla = (1, 3, 4, 6)

tupla = (1, 1.0, 1+1j, True, 'YES', (1,2,3))
print(tupla[2:4])
# de dos en dos
print(tupla[::2])
print(tupla[:2])
print(tupla[2:])
print(tupla.count(1))
print(tupla.count(1))
# Index of the first element with the specified value
print(tupla.index(3))
print(tupla.index(3, 3)) # Index from the specified index
print(tupla.index(3, 3, 7)) 
print(1 in tupla)


# GRAFICOS 1

import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib
# %matplotlib inline
x = np.linspace(-1, 1, 100)
y = x ** 2
plt.plot(x, y)
plt.show()

# GRAFICOS 2

import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib
x = np.linspace(-1, 1, 100)
for n in range(1, 10):
    y = x ** n
    plt.plot(x, y, label='x^{}'.format(n))

plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.grid(True)
plt.legend()

plt.show()