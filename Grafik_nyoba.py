import numpy as np
import datetime
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
fig.suptitle('Contoh Beberapa Grafis Acak')
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
ax1.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
ax1.set_xlabel('sumbu X')
ax1.set_ylabel('sumbu Y')

x = np.linspace(0, 10, 30)
y = np.sin(x)
ax2.plot(x, y, '-ok')
ax2.set_xlabel('sumbu X')
ax2.set_ylabel('sumbu Y')

fig.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()