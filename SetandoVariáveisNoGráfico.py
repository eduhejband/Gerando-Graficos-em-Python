import inline as inline
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111)


ax.set_title('Gráfico Título')


ax.set_xlim([0.5, 4.5])
ax.set_ylim([-3, 7])

ax.set_ylabel('Variável X')
ax.set_xlabel('Variável Y')


plt.show()