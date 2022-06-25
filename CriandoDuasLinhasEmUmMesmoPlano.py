
import matplotlib.pyplot as plt
fig = plt.figure()


y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]
plt.title("Gráfico")
#Define pontos da linha, podem trocar de forma adicionando "*" antes do"-"
plt.plot(y, 'go-')

#Define a cor dos pontos
plt.plot(y, 'ro')


plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()