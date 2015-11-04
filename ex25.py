def splitta(s):
	parola = s.split(' ')
	return parola

def ordina(a):
	return sorted(a)

def pop_inizio(a):
	return a.pop(0)

def pop_fine(a):
	return a.pop(-1)

frase = "Ciao questa frase vale tanto"

s = ordina(splitta(frase))

print "Array iniziale: ", s

prima = pop_inizio(s)
ultima = pop_fine(s)

print "Primo elemento: ", prima
print "Ultimo elemento: ", ultima

