import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
x = np.linspace(-2, 5)
y = (x) * np.sin(5*x)
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2)
plt.show()