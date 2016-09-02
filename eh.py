import math

c = 2.998*(10**8)			# m/s
h = 6.626*(10**-34)			# J/s
kb = 1.3807*(10**-23)		#
ke = 8.9875518*(10**9)		# N m^2 / C^2
me = 9.109*(10**-31)
eo = 8.85419*(10**-12)
N = 6.022*(10**23)
T = 300
charge_e = 1.602*(10**-19)	#Coulomb
e = math.exp(1)
pi = math.pi


# Aluminum
def aluminum():
	v = 2.2 * (10 ** 12)
	alpha = h * v / kb
	C = (-3 * N * h * v * alpha * (e ** (alpha / T))) / ((T ** 2) * ((e ** (alpha / T)) - 1) ** 2)
	print(C)


# Diamond
def diamond():
	v = 45 * (10 ** 12)
	alpha = h * v / kb
	C = (-3 * N * h * v * alpha * (e ** (alpha / T))) / ((T ** 2) * ((e ** (alpha / T)) - 1) ** 2)
	print(C)


def radius_of_bohrs_orbit(n):
	num = 4*pi*eo*((h/(2*pi))**2)*(n**2)
	den = me*(charge_e**2)
	return num/den


def ionization_energy(Z, orbit):
	num = -Z*ke*(charge_e**2)
	den = 2*radius_of_bohrs_orbit(orbit)
	conversion = 1
	return num/den * conversion


def wavelength(Z):
	val = ionization_energy(Z=Z, orbit=1)
	conversion = 10**9
	return (h*c)/val * conversion


def speed_of_electron(orbit, atomic_n):
	KE = abs(ionization_energy(Z=atomic_n, orbit=orbit))
	return (2*KE/me)**(1/2)


print("Helium: " + str(ionization_energy(Z=2, orbit=1)) + "| Wavelength: " + str(-1*wavelength(2)) + "nm")
print("Lithium: " + str(ionization_energy(Z=3, orbit=1)) + "| Wavelength: " + str(-1*wavelength(3)) + "nm")
print("Carbon: " + str(ionization_energy(Z=6, orbit=1)) + "| Wavelength: " + str(-1*wavelength(6)) + "nm")

print("Speed of electron in first Bohr orbit of atom H: " + str(speed_of_electron(orbit=1, atomic_n=1)) + " || Fraction of c: " + str(speed_of_electron(orbit=1, atomic_n=1)/c))
print("Z = 50 || speed = " + str(speed_of_electron(orbit=1, atomic_n=50)) + " || Fraction of c: " + str(speed_of_electron(orbit=1, atomic_n=50)/c))
