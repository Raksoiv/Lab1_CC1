# Item 1
print("i.1")
print("((1 + 2**(-52)) - 1) + 2**(-54) + 1")
r1 = 1 + 2**(-52)
print("((" + str(r1) + ") - 1) + 2**(-54) + 1")
r1 -= 1
print("(" + str(r1) + ") + 2**(-54) + 1")
r1 += 2**(-54)
print(str(r1) + " + 1")
r1 += 1
print(str(r1))
print("i.2")
print("((1 + 2**(-54)) - 1) + 2**(-52) + 1")
r1 = 1 + 2**(-54)
print("((" + str(r1) + ") - 1) + 2**(-52) + 1")
r1 -= 1
print("(" + str(r1) + ") + 2**(-52) + 1")
r1 += 2**(-52)
print(str(r1) + " + 1")
r1 += 1
print(str(r1))
print("")
# Item 2
print("ii.1")
print("(5 - 4) + 2**(-52)")
r1 = 5 - 4
print (str(r1) + " + 2**(-52)")
r1 += 2**(-52)
print(r1)
print("ii.2")
print("5 - (4 - 2**(-52))")
r1 = 4 - 2**(-52)
print("5 - " + str(r1))
r1 = 5 - r1
print(r1)
print("")
#Item 3
print("iii.1")
print("(2**(53) + (-2**(53)) + (1 + .5 + .25)")
r1 = 2**(53) + (-2**(53))
r2 = 1 + .5 + .25
print(str(r1) + " + " + str(r2))
print(str(r1 + r2))
print("iii.2")
print("(2**(53) + (1 + .5 + .25)) - 2**(53)")
r1 = 2**(53) + (1 + .5 + .25)
print(str(r1) + " - 2**(53)")
r1 = r1 - 2**(53)
print(r1)