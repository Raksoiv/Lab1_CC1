def epsilon(fl):
	if(fl >= 1):
		exp = 0
		while(fl >= 2 ** (exp + 1)):
			exp += 1
	else:
		exp = -1
		while(fl <= 2 **(exp - 1)):
			exp -= 1
	exp -= 52
	return 2**exp