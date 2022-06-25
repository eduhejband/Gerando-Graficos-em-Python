
import matplotlib.pyplot as plt

from ColocandoIndiceNoGrafico import data

plt.legend()
plt.title('Preços', color='purple', size=20)
close_prices = data['AdjClose']
fig = plt.figure(figsize=(10, 5))
plt.plot(close_prices, color='purple')


plt.xticks(rotation=45, color='teal', size=12)
plt.yticks(rotation=45, color='teal', size=12)


plt.xlabel('Datas', {'color': 'orange', 'fontsize':15})
plt.ylabel('Preços', {'color': 'orange', 'fontsize':15})
plt.show()