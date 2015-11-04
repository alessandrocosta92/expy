from sys import argv

script, f = argv

print "Continuare? Il file %r verra' azzerato (CTRL+C per annullare, INVIO continua)" % f

print "\nVecchio testo: "
txt = open(f, "r+")
old = txt.read()
print old
txt.truncate()


print "Scrivi 3 linee\n"
l1 = raw_input("Linea 1: ")
l2 = raw_input("Linea 2: ")
l3 = raw_input("Linea 3: ")

txt.write(l1)
txt.write("\n")
txt.write(l2)
txt.write("\n")
txt.write(l3)
txt.write("\n")

txt.close()
