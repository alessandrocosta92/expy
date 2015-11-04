# -*- coding: utf-8 -*-

x = "Ci sono %d tipi di persone" % 10
binario = "Binario"
non = "non lo conosce"
y = "Chi conosce il %s, e chi %s" % (binario, non)

print x
print y

print "Ho detto %r" % x
print "..e anche '%s'." %y

h = False
hs = "Non è divertente! %r"

print hs % h

