# main.py

from mahasiswa import Mahasiswa
from mata_kuliah import MataKuliah

def main():
    # Membuat objek mata kuliah
    mata_kuliah1 = MataKuliah("IF101", "Algoritma dan Pemrograman")
    mata_kuliah2 = MataKuliah("IF102", "Struktur Data")

    # Membuat objek mahasiswa
    mahasiswa1 = Mahasiswa("Sulthon")

    # Proses pembayaran SPP
    mahasiswa1.bayar_spp()

    # Mengambil mata kuliah
    mahasiswa1.ambil_matakuliah(mata_kuliah1)
    mahasiswa1.ambil_matakuliah(mata_kuliah2)

    # Mengisi nilai untuk mata kuliah
    mahasiswa1.isi_nilai(mata_kuliah1, 80)
    mahasiswa1.isi_nilai(mata_kuliah2, 90)

    # Menghitung nilai akhir
    mahasiswa1.hitung_nilai_akhir()

if __name__ == "__main__":
    main()
