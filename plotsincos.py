from math import pi

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('wxagg')

x = np.linspace(-2*pi, 2*pi, 240)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, x, y_cos)

plt.title('Plot of sine and cosine functions')
plt.xlabel('-2\u03c0 < x < 2\u03c0')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['y = sin(x)', 'y = cos(x)'])
plt.show()
