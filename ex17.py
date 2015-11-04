from sys import argv
from os.path import exists

script, da, a = argv

print "Copio il file %s nel file %s (solo se gia  esistente)" % (da, a)

if exists(a):
	da_f = open(da, "r")
	da_txt = da_f.read()
	a_f = open(a, "w")
	a_f.write(da_txt)
	da_f.close()
	a_f.close()
else:
	print "Il file di destinazione non esiste."
