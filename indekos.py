from hunian import Hunian

class Indekos(Hunian):
	def __init__(self, nama_pemilik, nama_penghuni, luas, harga):
		super().__init__("Indekos")
		self.nama_pemilik = nama_pemilik
		self.nama_penghuni = nama_penghuni
		self.luas = luas
		self.harga = harga

	def get_dokumen(self):
		return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

	def get_nama_pemilik(self):
		return self.nama_pemilik

	def get_nama_penghuni(self):
		return self.nama_penghuni

	def get_luas(self):
		return self.luas
	
	def get_harga(self):
		return self.harga

	def get_summary(self):
		 return "Hunian Indekos, ditempati oleh " + str(self.nama_penghuni) + "\n" + \
			"dimiliki oleh " + str(self.nama_pemilik) + "\n" + \
			"luas ruangan " + str(self.get_luas()) + " m\n" + \
			"harga per bulan Rp" + str(self.get_harga()) + "\n" + \
			self.get_dokumen()