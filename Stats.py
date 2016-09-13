from sympy import integrate

from Utils.Function import Function


f = Function('2*x')
print(f.evaluate(49.8,50.25))
