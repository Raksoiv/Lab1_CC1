e_mach = 2**(-52)
x_1 = 0.9999999999999
x_2 = x_1
while(((x_2 + e_mach/2) - x_2) != 0):
	x_1 = x_2
	x_2 += e_mach/2
	print(x_2)
print("El menor numero en el cual la suma no es representables es: " + str(x_1))