import numpy as np
import matplotlib.pyplot as plt


array = np.random.normal(0, 1, 10000)


plt.hist(array, color='teal', orientation='horizontal')
plt.xlabel('Frequencia')
plt.ylabel('Qualquer Coisa')
plt.show()
