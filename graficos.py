import math
from math import pi
from matplotlib import pyplot as plt

x = []
for i in range(41):
    x.append(i)
print(x)

y = []
for i in x:
    y.append(math.sin(i*pi/10))
print(y)
plt.title("Función Seno")
plt.xlabel("Ángulo")
plt.ylabel(("Valor del Seno"))
plt.plot(x,y)
plt.show()
