#O functie pentru media aritmetica
def media(cifre):
   return float(sum(cifre)) / max(len(cifre), 1)


#O functie pentru numere prime
def prim(n):
	divizori = 0
	d = 1
	while d <= n:
		if n % d == 0:
			divizori += 1
		d += 1
	if divizori == 2:
		print(str(n) + " este prim!")
	else:
		print(str(n) + " nu este prim!")


#Viitor feature: sa se poata scrie valorile intr un browser si sa iti afiseze imediat si rezultatele. 
