import sympy
import time
from math import pi as pi, erf, sqrt
from math import exp


class Function(object):
	function = 0

	def __init__(self, function):
		self.function = sympy.sympify(function)

	def evaluate(self, x1, x2):
		return self.function.subs({'x': x2}).evalf() - self.function.subs({'x': x1}).evalf()

	def solvefor(self, value, guess):
		while self.f(guess) - value != 0:
			print("Guess: " + str(guess) + "|| Derivative: " + str(self.derivative(guess)) + "|| Value: " + str(
				self.f(guess)))
			guess -= ((self.f(guess) - value) / self.derivative(guess))
			time.sleep(1)

	def f(self, x):
		return self.function.subs({'x': x}).evalf()

	def derivative(self, x):
		delta = .000000001
		return (self.f(x + delta) - self.f(x)) / delta


class NormalDistribution(object):
	mean = 0
	stnddev = 0

	def __init__(self, mean, stnddev):
		self.mean = mean
		self.stnddev = stnddev

	def XtoZ(self, x):
		return (x - self.mean) / self.stnddev

	def ZtoX(self, z):
		return (z * self.stnddev) + self.mean

	def calcP(self, z=None, x=None, x2=None, z2=None):
		if x is not None:
			if x2 is None:
				z = self.XtoZ(x)
				return self.p(z)
			else:
				z1 = self.XtoZ(x)
				z2 = self.XtoZ(x2)
				return 1 - self.p(z1) - self.p(-z2)
		elif z is not None:
			if z2 is None:
				return self.p(z)
			else:
				return 1 - self.p(z) - self.p(-z2)

	def p(self, z):
		return 0.5 * (1 + erf(z / sqrt(2)))


class ExponentialDistribution(object):
	mean = 0

	def __init__(self, mean):
		self.mean = mean

	def calcP(self, x, x2 = None):
		if x2 is None:
			return self.iPdf(x)-self.iPdf(0)
		else:
			return self.iPdf(x2)-self.iPdf(x)

	def pdf(self, x):
		return self.mean*exp(-self.mean*x)

	def iPdf(self,x):
		return -exp(-self.mean*x)

	def solveForX(self, p):
		return sympy.ln(1-p)/(-self.mean)