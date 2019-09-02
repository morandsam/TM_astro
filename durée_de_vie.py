import matplotlib.pyplot as plt
import numpy as np
from math import *
plt.plot([0.3,1,3,10,30],[8*10000000000,10*1000000000,3*100000000,1*100000000,6*10000000])

plt.yscale('log')

plt.title("Durée sur la séquence principale en fonction de la masse")
plt.xlabel("Masse (par rapport au soleil )")
plt.ylabel("Durée (en années)")
plt.show()
