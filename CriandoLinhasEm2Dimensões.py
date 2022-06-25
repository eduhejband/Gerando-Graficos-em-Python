
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

arr_2d = np.random.normal(size=40).reshape(20, 2)

plt.plot(arr_2d)



plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()