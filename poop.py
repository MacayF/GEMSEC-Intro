import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-100,100,num=200)
y=x**3+x**2+x+36
plt.scatter(x,y)
plt.show()
