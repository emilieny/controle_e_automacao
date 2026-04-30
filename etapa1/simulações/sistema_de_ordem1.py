import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

system = signal.TransferFunction([1], [1, 1])
t, y = signal.step(system)

plt.plot(t, y)

plt.xlabel("Tempo")
plt.ylabel("Saída")
plt.title("Resposta ao Degrau - Sistema de Primeira Ordem")
plt.grid()

plt.show()