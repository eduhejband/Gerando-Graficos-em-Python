
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

arr = np.random.normal(size=30)


plt.plot(arr, color='teal', marker='*', linestyle='dashed')


plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()