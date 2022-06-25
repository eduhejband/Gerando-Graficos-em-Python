from matplotlib import pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
axes[0, 0].set(title='Esquerda superior')
axes[0, 1].set(title='Direita superior')
axes[1, 0].set(title='Esquerda Inferior')
axes[1, 1].set(title='Direita inferior')
plt.show()