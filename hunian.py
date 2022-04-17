class Hunian():
	def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas = "", harga = 0):
		self.jenis = jenis
		self.jml_penghuni = jml_penghuni
		self.jml_kamar = jml_kamar
		self.luas = luas
		self.harga = harga

	def get_jenis(self):
		return self.jenis

	def get_jml_penghuni(self):
		return self.jml_penghuni

	def get_jml_kamar(self):
		return self.jml_kamar

	def get_luas(self):
		return self.luas
	
	def get_harga(self):
		return self.harga

	def get_dokumen(self):
		pass

	def get_summary(self):
		return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang.\n" + \
			"dengan jumlah kamar " + str(self.get_jml_kamar()) + "\n" + \
			"luas bangunan " + str(self.get_luas()) + " m\n" + \
			"harga per bulan Rp" + str(self.get_harga()) + "\n" + \
			self.get_dokumen() + "\n"