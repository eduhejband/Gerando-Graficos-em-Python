import matplotlib.pyplot as plt
import volume as volume

from AdicionandoSubVariaveis import close_prices
from ColocandoIndiceNoGrafico import data

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10, 8))
ax1.plot(close_prices, color='purple', label='Preços')
ax1.grid(True)

# Setting the title of a first plot
ax1.set_title('Preços Diários')

# Setting the legend for the first plot
ax1.legend()

ax2.bar(volume.index, volume, label='Volume')
ax2.grid(True)

# Setting the title of a second plot
ax2.set_title('Volume')

# Setting the legend for the second plot
ax2.legend()

plt.show()