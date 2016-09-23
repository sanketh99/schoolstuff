from Utils.Function import Function, ExponentialDistribution
from Utils.Function import NormalDistribution


e = ExponentialDistribution(mean=3)
print(e.calcP(3))