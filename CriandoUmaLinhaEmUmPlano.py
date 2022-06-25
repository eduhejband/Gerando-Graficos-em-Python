import matplotlib.pyplot as plt
fig = plt.figure()

x = [1.3, 2.9, 3.1, 4.7, 5.6, 6.5, 7.4, 8.8, 9.2, 10]
y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]


plt.plot(x,y)


plt.xlabel('Variáveis X')
plt.ylabel('Variáveis Y')
plt.show()