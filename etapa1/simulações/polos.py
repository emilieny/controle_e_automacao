import matplotlib.pyplot as plt

# Polos
p1 = -2
p2 = -1 + 2j
p3 = -1 - 2j
p4 = 1

plt.scatter(p1.real, p1.imag, marker='x', label='Polo real estável')
plt.scatter(p2.real, p2.imag, marker='x', label='Polos complexos')
plt.scatter(p3.real, p3.imag, marker='x')
plt.scatter(p4.real, p4.imag, marker='x', label='Polo instável')

plt.axhline(0)
plt.axvline(0)

plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.title("Diagrama de Polos no Plano s")
plt.legend()
plt.grid()

plt.show()