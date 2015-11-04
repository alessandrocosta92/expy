from sys import exit

class Stanza (object):
	def __init__(self, tipo = "normale"):
		self.Tipo = tipo
        def esci(self):
		print "Esci da Stanza", self.Tipo
	def toString(self):
		print "\n\n\n\nOra sei nella Stanza", self.Tipo

class StanzaOro (Stanza):
	def __init__(self):
 		super(StanzaOro, self).__init__("Oro")
	def pickOro(self, qta):
		if qta > 50:
			print "Prendi piu della meta delle monete...bravo!"
			exit()
		else:
			print "Prendi meno della meta delle monete!"
			exit()			

class StanzaOrso (Stanza):
	def __init__(self):
 		super(StanzaOrso, self).__init__("Orso")

	def fuggi(self):
		print "Fuggi dall'orso..."
		return False

	def offriMiele(self):
		print "Dai del miele all'orso..."
		return True


class StanzaBuia (Stanza):
	def __init__(self):
 		super(StanzaBuia, self).__init__("Buia")
		print "Stanza buia...fine gioco"
		exit()


stato = "0"
p = None;
scelta = None
x = True

## loop
while True:
	print "Stato attuale: ", stato
	x = True
	scelta = None

	if stato == "0":
		p = Stanza()
		p.toString()
		print "Porta [1] o porta [2]"
		while x:
			scelta = raw_input("> ")	
			if scelta == "1" or scelta =="2":
				x = False
		stato = scelta

	if stato == "1":
		p = StanzaBuia()
		p.toString()
	if stato == "2":
		p = StanzaOrso()
		p.toString()
		print "Porta [1] o porta [2]"
		while x:
			scelta = raw_input("> ")	
			if scelta == "1" or scelta =="2":
				x = False
		stato = scelta

		
		
## fine loop


	
