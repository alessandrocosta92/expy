def somma(a, b):
	return a+b

def sottrazione(a, b):
	return a-b

def moltiplicazione(a, b):
	return a*b

def divisione(a, b):
	if (b == 0):
		return "Div per 0"
	else:
		return a/b

somma = somma(10, 5)
sottrazione = sottrazione(70, 67)
moltiplicazione = moltiplicazione(156, 3.5678)
divisione = divisione(5, 3.3)

print "Somma: ", somma
print "Sottrazione: ", sottrazione
print "Moltiplicazione: ", moltiplicazione
print "Divisione: ", divisione
