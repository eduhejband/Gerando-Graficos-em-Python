import matplotlib.pyplot as plt

from AdicionandoSubVariaveis import close_prices
from ColocandoIndiceNoGrafico import data

volume = data['AdjVolume']


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10, 8))


ax1.plot(close_prices, color='purple')
ax1.grid(True)


ax2.bar(volume.index, volume)
ax2.grid(True)


plt.show()