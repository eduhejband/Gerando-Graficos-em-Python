
import matplotlib.pyplot as plt
fig = plt.figure()


y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

#Define pontos da linha, podem trocar de forma adicionando "*" antes do"-"
plt.plot(y, 'g')


plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()