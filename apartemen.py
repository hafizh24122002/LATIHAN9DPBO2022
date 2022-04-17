from hunian import Hunian

class Apartemen(Hunian):
	def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas, harga):
		super().__init__("Apartemen", jml_penghuni, jml_kamar, luas, harga)
		self.nama_pemilik = nama_pemilik

	def get_dokumen(self):
		return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

	def get_nama_pemilik(self):
		return self.nama_pemilik

	def get_summary(self):
		return super().get_summary() + "dimiliki oleh " + self.get_nama_pemilik() + "\n"