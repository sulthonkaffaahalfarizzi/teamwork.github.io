# mahasiswa.py

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.spp_paid = False
        self.nilai = {}

    def bayar_spp(self):
        self.spp_paid = True
        print(f"{self.nama} telah membayar SPP.")

    def ambil_matakuliah(self, matakuliah):
        if not self.spp_paid:
            print(f"{self.nama} harus membayar SPP terlebih dahulu.")
            return
        matakuliah.ambil(self)

    def isi_nilai(self, matakuliah, nilai):
        if matakuliah.kode not in self.nilai:
            self.nilai[matakuliah.kode] = nilai
            print(f"Nilai {nilai} untuk mata kuliah {matakuliah.nama} telah diisi.")
        else:
            print(f"Nilai untuk mata kuliah {matakuliah.nama} sudah ada.")

    def hitung_nilai_akhir(self):
        if not self.nilai:
            print(f"{self.nama} belum memiliki nilai.")
            return
        total_nilai = sum(self.nilai.values())
        jumlah_matakuliah = len(self.nilai)
        nilai_akhir = total_nilai / jumlah_matakuliah
        print(f"Nilai akhir {self.nama} adalah: {nilai_akhir:.2f}")
