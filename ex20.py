from sys import argv

script, in_file = argv

def stampa(f):
    print f.read()

def re(f):
    f.seek(0)

def linea(l, f):
    print l, f.readline()

f = open(in_file)

print "Stampa file: \n"

stampa(f)

print "Eseguo seek..."

re(f)

print "Stampo riga per riga:\n"

l = 1
linea(l, f)

l = l + 1
linea(l, f)

l = l + 1
linea(l, f)
