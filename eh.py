import math

c = 2.998*(10**8)			# m/s
h = 6.626*(10**-34)			# Js
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


def radius_of_bohrs_orbit(n, Z):
	num = (n**2)*(h**2)*eo
	den = me*Z*(charge_e**2)*pi
	return num/den


def orbit_energy(Z, orbit):
	num = -Z*ke*(charge_e**2)
	den = 2*radius_of_bohrs_orbit(n=orbit, Z=Z)
	conversion = 1
	return num/den * conversion


def wavelength(Z):
	val = abs(orbit_energy(Z=Z, orbit=1))
	conversion = 10**9
	return (h*c)/val * conversion


def speed_of_electron(orbit, atomic_n):
	KE = abs(orbit_energy(Z=atomic_n, orbit=orbit))
	return (2*KE/me)**(1/2)


def delta_E(n1, n2, Z):
	if n2 > n1:
		one = abs(orbit_energy(Z=Z, orbit=n1))
		two = abs(orbit_energy(Z=Z, orbit=n2))
		return one-two
	else:
		print('n2 must be greater than n1')


def tata(Z):
	num = -me*(Z**2)*(charge_e**4)
	print(num)
	den = 8*(1)*(h**2)*(eo**2)
	print(den)
	return num/den


def roro():
	num = (charge_e**2)
	den = 2*eo*h
	return num/den


# -----------------Problem Sets--------------------
def Exercise5():
	print("Helium: " + str(orbit_energy(Z=2, orbit=1)*6.242*(10**18)) + "ev| Wavelength: " + str(
		-1 * wavelength(2)) + "nm")
	# print("Helium: " + str(tata(2) * 1.602 * (10 ** 19)))
	print("Lithium: " + str(orbit_energy(Z=3, orbit=1)*6.242*(10**18)) + "ev| Wavelength: " + str(
		-1 * wavelength(3)) + "nm")
	print("Carbon: " + str(orbit_energy(Z=6, orbit=1)*6.242*(10**18)) + "ev| Wavelength: " + str(
		-1 * wavelength(6)) + "nm")


def Exercise6():
	print("Z = 1: " + str(speed_of_electron(orbit=1, atomic_n=1)) + "m/s|| Fraction of c: " + str(speed_of_electron(orbit=1, atomic_n=1)/c))
	print("Z = 50: " + str(speed_of_electron(orbit=1, atomic_n=50)) + "m/s|| Fraction of c: " + str(speed_of_electron(orbit=1, atomic_n=50)/c))


def Exercise7():
	one = orbit_energy(Z=1, orbit=1)*207
	two = orbit_energy(Z=1, orbit=2)*207
	print("Mesonic Ground State: " + str(one))
	print("Radius of 1st Bohr Orbital: " + str(radius_of_bohrs_orbit(Z=1, n=1)/207))
	deltaE = abs(one)-abs(two)
	print("Energy associated with transition: " + str(deltaE))
	print("Frequency associated with this transition: " + str(deltaE/h))


def Exercise8():
	deltaE = delta_E(n1=1, n2=2, Z=30)*6.242*(10**18)
	print("delta E of Zn: " + str(deltaE) + "eV")
	print("KE: " + str(deltaE-4.30))


def Exercise9():
	wavelength = 5*(10**-11)
	m = 1.6750*(10**-27)
	num = h**2
	den = 3*kb*(wavelength**2)*m
	print("The required temperature is: " + str(num/den))


def answers():
	print('Exercise 5')
	print('')
	Exercise5()
	print('')

	print('Exercise 6')
	print('')
	Exercise6()
	print('')

	print('Exercise 7')
	print('')
	Exercise7()
	print('')

	print('Exercise 8')
	print('')
	Exercise8()
	print('')

	print('Exercise 9')
	print('')
	Exercise9()
	print('')

answers()
