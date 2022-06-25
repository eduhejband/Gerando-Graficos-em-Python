
import matplotlib.pyplot as plt
import numpy as np



dictionary = {'a': np.linspace(1, 100, 50),
              'c': np.random.randint(0, 50, 50),
              'd': np.abs(np.random.randn(50)) * 100}

dictionary['b'] = dictionary['a'] * np.random.rand(50)


plt.scatter(dictionary['a'], dictionary['b'])


plt.xlabel('Pontos A')
plt.ylabel('Pontos B')
plt.show()