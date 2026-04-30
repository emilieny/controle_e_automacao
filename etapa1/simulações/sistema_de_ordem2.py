import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def sistema(zeta):
    wn = 1
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    return signal.TransferFunction(num, den)

zetas = [0.3, 1, 2]

for z in zetas:
    system = sistema(z)
    t, y = signal.step(system)
    plt.plot(t, y, label=f'zeta={z}')

plt.xlabel("Tempo")
plt.ylabel("Saída")
plt.title("Resposta ao Degrau - Sistemas de Segunda Ordem")
plt.legend()
plt.grid()

plt.show()