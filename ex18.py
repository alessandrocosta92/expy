def foo1 (*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def foo2 (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def foo3 (arg1):
	print "arg1: ", arg1

def foo4 ():
	print "Niente"

foo1("Ciao", "Tutti")
foo2("Albero", "Casa")
foo3("Sole")
foo4()
