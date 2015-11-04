class Citta (object):
	def __init__(self, nome, abitanti):
		self.Nome = nome
		self.Abitanti = abitanti
	
	def stampa_nome(self):
		print self.Nome

	def stampa_abitanti(self):
		print self.Abitanti

	def stampa_tutto(self):
		print "%s, %d" % (self.Nome, self.Abitanti)


torino = Citta("Torino", 156000)
milano = Citta("Milano", 245321)
roma = Citta("Roma", 845721)

torino.stampa_nome()
milano.stampa_abitanti()
roma.stampa_tutto()
