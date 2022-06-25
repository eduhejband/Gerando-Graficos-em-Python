
import matplotlib.pyplot as plt
import numpy as np

from ColocandoIndiceNoGrafico import data

x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

color = np.random.rand(10)
size = np.random.randint(50, 100, 10)

plt.scatter(x=data['AdjOpen'], y=data['AdjClose'])
plt.show()

