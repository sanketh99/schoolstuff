import sympy
import time


class Function(object):

	function = 0

	def __init__(self, function):
		self.function = sympy.sympify(function)

	def evaluate(self,x1,x2):
		return self.function.subs({'x': x2}).evalf() - self.function.subs({'x': x1}).evalf()

	def solvefor(self, value, guess):
		while self.f(guess)-value != 0:
			print("Guess: " + str(guess) + "|| Derivative: " + str(self.derivative(guess)) + "|| Value: " + str(self.f(guess)))
			guess -= ((self.f(guess)-value)/self.derivative(guess))
			time.sleep(1)

	def f(self,x):
		return self.function.subs({'x': x}).evalf()

	def derivative(self, x):
		delta = .000000001
		return (self.f(x+delta)-self.f(x))/delta