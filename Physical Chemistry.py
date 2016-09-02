from Utils.HelpfulTools import HelpfulTools
import numpy as np
import matplotlib.pyplot as plt

h = HelpfulTools()
coefficients = {
	'a': 0,
	'b': 0
}
formula = "x**2+a+b"

x = np.linspace(0,10)
fx = h.createEquation(coefficients, formula)
plt.plot(x, eval(fx))
plt.show()