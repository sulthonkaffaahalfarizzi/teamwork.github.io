from metaflow import FlowSpec, step, Parameter

class InformaticsUMSFlow(FlowSpec):

    # Parameter untuk jumlah semester dan daftar mata kuliah dasar (untuk contoh)
    total_semesters = Parameter('total_semesters', default=8, help="Jumlah total semester")
    core_subjects = Parameter('core_subjects', default=['Pemrograman Dasar', 'Matematika Diskrit', 'Sistem Basis Data', 'Jaringan Komputer'], help="Daftar mata kuliah inti")

    @step
    def start(self):
        # Memulai alur akademik
        print("Selamat datang di Universitas Muhammadiyah Surakarta, Fakultas Komunikasi dan Informatika, Program Studi Teknik Informatika.")
        self.next(self.pmb)

    @step
    def pmb(self):
        # Masa Pengenalan Mahasiswa Baru (PMB)
        print("Tahap Pengenalan Mahasiswa Baru: Memahami lingkungan kampus dan peraturan akademik.")
        self.next(self.krs_planning)

    @step
    def krs_planning(self):
        # Perencanaan Studi dan Pengisian KRS
        print("Tahap Perencanaan Studi: Mengisi Kartu Rencana Studi (KRS) dan menentukan mata kuliah.")
        self.semester = 1
        self.next(self.semester_journey)

    @step
    def semester_journey(self):
        # Alur perkuliahan setiap semester
        print(f"\nMemulai semester {self.semester}.")
        print("Daftar mata kuliah:", self.core_subjects)
        
        # Langkah-langkah semester
        print(f"1. Mengikuti perkuliahan dan menyelesaikan tugas-tugas di semester {self.semester}.")
        print(f"2. Ujian Tengah Semester (UTS) di semester {self.semester}.")
        print(f"3. Praktikum atau Proyek di semester {self.semester}.")
        print(f"4. Ujian Akhir Semester (UAS) di semester {self.semester}.")
        
        # Input nilai IP semester ini
        self.semester_gpa = float(input(f"Masukkan nilai IP untuk semester {self.semester}: "))
        
        # Simpan nilai IP semester untuk menghitung IPK nanti
        if not hasattr(self, 'gpas'):
            self.gpas = []
        self.gpas.append(self.semester_gpa)
        
        # Periksa apakah ini semester terakhir atau lanjut ke semester berikutnya
        if self.semester < self.total_semesters:
            self.semester += 1
            self.next(self.semester_journey)
        else:
            self.next(self.skripsi_ta)

    @step
    def skripsi_ta(self):
        # Tahap Skripsi atau Tugas Akhir (TA)
        print("Tahap Skripsi atau Tugas Akhir (TA): Mahasiswa wajib menyelesaikan TA sebagai syarat kelulusan.")
        self.has_passed_ta = input("Apakah mahasiswa lulus Skripsi/TA? (ya/tidak): ").lower() == "ya"
        
        if self.has_passed_ta:
            self.next(self.graduation)
        else:
            print("Mahasiswa belum lulus TA. Mengulangi proses skripsi/TA.")
            self.next(self.skripsi_ta)

    @step
    def graduation(self):
        # Tahap Wisuda
        print("\nSelamat! Mahasiswa telah menyelesaikan seluruh persyaratan dan siap diwisuda.")
        print(f"IPK Akhir: {self.calculate_cumulative_gpa():.2f}")

    def calculate_cumulative_gpa(self):
        # Menghitung IPK (Indeks Prestasi Kumulatif) dari rata-rata nilai IP setiap semester
        return sum(self.gpas) / len(self.gpas)

    @step
    def end(self):
        # Akhir dari alur perkuliahan
        print("Perjalanan akademik selesai. Terima kasih telah mengikuti alur perkuliahan ini.")

# Menjalankan flow ini menggunakan Metaflow
if __name__ == '__main__':
    InformaticsUMSFlow()
