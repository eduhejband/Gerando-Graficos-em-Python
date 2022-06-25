import numpy as np
import matplotlib.pyplot as plt


array = np.random.normal(0, 1, 10000)

plt.hist(array, color='purple', histtype='step')
plt.xlabel('Qualquer Coisas')
plt.ylabel('Frequencia')
plt.show()
