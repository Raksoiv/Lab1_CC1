def bisection(tol, a, b, f):
	while(((b - a)/2) > tol):
		c = (a + b)/2
		if(f(c) == 0):
			return c
		elif(f(a) * f(c) < 0):
			b = c
		else:
			a = c
	return c

e_mach = 2**(-52)
f1 = lambda x: (x - e_mach) - x
result = bisection(0.1, 1, 3, f1)
print("tolerancia = 0.1 | resultado = " + str(result))
result = bisection(0.01, 1, 3, f1)
print("tolerancia = 0.01 | resultado = " + str(result))
result = bisection(0.0001, 1, 3, f1)
print("tolerancia = 0.0001 | resultado = " + str(result))
result = bisection(0.00000000000001, 1, 3, f1)
print("tolerancia = 0.00000000000001 | resultado = " + str(result))
result = bisection(e_mach, 1, 3, f1)
print("tolerancia = e_mach | resultado = " + str(result))
print("Finalmente el menor numero el cual no se puede representar su resta es 2 debido a que:")
print("(" + str(result) + " - " + str(e_mach) + ") - " + str(result))
print("(" + str(result - e_mach) + ") - " + str(result))
result2 = result - e_mach
print((result2) - result)
print("(" + str(2.4) + " - " + str(e_mach) + ") - " + str(2.4))
print("(" + str(2.4 - e_mach) + ") - " + str(result))
result2 = 2.4 - e_mach
print((result2) - 2.4)