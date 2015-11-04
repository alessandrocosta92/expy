from sys import argv

script, file = argv

txt = open(file, "r")

print "%r" % txt.read()

f2 = raw_input("Nuovo file ? ")

txt = open(f2, "r")

print "Nuovo file: ", txt.read()
