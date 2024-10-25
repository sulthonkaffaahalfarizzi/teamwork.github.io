# mata_kuliah.py

class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa_terdaftar = []

    def ambil(self, mahasiswa):
        self.mahasiswa_terdaftar.append(mahasiswa)
        print(f"{mahasiswa.nama} telah mengambil mata kuliah {self.nama}.")
