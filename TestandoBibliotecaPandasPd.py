
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()

ts = pd.Series(np.random.normal(size=50),index=pd.date_range(start='1/1/2019', periods=50))

ts.plot()

plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()