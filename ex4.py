macchine = 100
spazio = 4.0
guidi = 30
passeggeri = 90
macchine_non_usate = macchine - guidi
macchine_usate = guidi
capacita = macchine_usate * spazio
media_passeggeri = passeggeri / macchine_usate

print "Ci sono", macchine, " macchine disponibili"
print "Ci sono solo ", guidi, " guidatori"
print "Ci saranno ", macchine_non_usate, " macchine inutilizzate"
print "Possiamo scortare ", capacita, " passeggeri oggi"
print "Abbiamo ", passeggeri, "passeggeri"
print "Ci sono circa ", media_passeggeri, " per ogni auto"
