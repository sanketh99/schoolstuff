from pydoc import replace


# noinspection PyPep8Naming
class HelpfulTools(object):

	def createEquation(self, coefficients, expression):
		for i in coefficients:
			expression = replace(expression, i, str(coefficients.get(i)))
		print(expression)
		return expression
