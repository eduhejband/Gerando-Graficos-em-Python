import numpy as np
import matplotlib.pyplot as plt

from ColocandoIndiceNoGrafico import data


close_prices = data['AdjClose']

fig = plt.figure(figsize=(10, 5))
plt.plot(close_prices)
plt.show()
