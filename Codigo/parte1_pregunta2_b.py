e_mach = 2**(-52)
x = 1.9999999999999
while(((x + e_mach) - x) != 0):
	x += e_mach
	print(x)
print("El menor numero en el cual la suma no es representables es: " + str(x))
