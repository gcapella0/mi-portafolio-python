import random 
n = random.randint(1, 10) 
adivino = int(input("Adivina el número entre 1 y 10: ")) 
while n != "adivino": 
	print 
	if adivino < n: 
		print ("Demasiado bajo") 
	elif adivino > n: 
		print ("Demasiado alto") 
	adivino = int(input("Adivina el número entre 1 y 10: ")) 
if adivino == n: 
	print ("¡Correcto!")