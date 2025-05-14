# matplotlib_exemplo.py
import matplotlib.pyplot as plt # type: ignore

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x, y)
plt.title("Gráfico de x ao quadrado")
plt.xlabel("x")
plt.ylabel("x²")
plt.grid(True)
plt.show()