import numpy as np
import matplotlib.pyplot as plt

from ColocandoIndiceNoGrafico import data


close_prices = data['AdjClose']

plt.plot(close_prices)
plt.xticks(rotation=45)
plt.show()
