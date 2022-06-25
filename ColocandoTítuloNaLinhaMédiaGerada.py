from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from ColocandoIndiceNoGrafico import data

plt.legend()
plt.title('Preços', color='purple', size=20)

close_prices = data['Linha']
fig = plt.figure(figsize=(10, 5))
plt.plot(close_prices, color='purple')
plt.text(datetime(2014, 1, 7), 120, 'PreçoMédio', size=15, color='r')

plt.xticks(rotation=45, color='teal', size=12)
plt.yticks(rotation=45, color='teal', size=12)
plt.grid(True)

plt.xlabel('Datas', {'color': 'orange', 'fontsize': 15})
plt.ylabel('Preços', {'color': 'orange', 'fontsize': 15})

mean_price = np.mean(close_prices)
plt.axhline(mean_price, color='r', linestyle='dashed')

plt.show()
