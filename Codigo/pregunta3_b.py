from pregunta3_a import epsilon

print("| i | e |")
for i in range (-50, 51):
	print("| " + str(i) + " | " + str(epsilon(2**(i))) + " |")