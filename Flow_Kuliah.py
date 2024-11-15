from metaflow import FlowSpec, step

class UniversityJourneyFlow(FlowSpec):

    @step
    def start(self):
        # Langkah awal dari alur perkuliahan
        print("Memulai perjalanan akademik mahasiswa di Teknik Informatika UMS")
        self.next(self.pmb)

    @step
    def pmb(self):
        # Masa Pengenalan Mahasiswa Baru (PMB)
        print("Tahap Pengenalan Mahasiswa Baru")
        self.next(self.krs_planning)

    @step
    def krs_planning(self):
        # Perencanaan Studi dan KRS
        print("Tahap Perencanaan Studi dan Pengisian KRS")
        self.semester = 1
        self.next(self.semester_journey)

    @step
    def semester_journey(self):
        # Alur setiap semester: perkuliahan, UTS, proyek/praktikum, UAS
        print(f"Memulai semester {self.semester}")
        
        # Langkah-langkah dalam semester
        print(f"1. Perkuliahan dan Tugas di semester {self.semester}")
        print(f"2. Ujian Tengah Semester (UTS) di semester {self.semester}")
        print(f"3. Praktikum dan Proyek di semester {self.semester}")
        print(f"4. Ujian Akhir Semester (UAS) di semester {self.semester}")
        
        # Simpan nilai IP semester ini
        self.semester_gpa = float(input(f"Masukkan IP semester {self.semester}: "))
        
        # Cek apakah ini adalah semester akhir atau bukan
        if self.semester < 8:
            self.semester += 1
            self.next(self.semester_journey)
        else:
            self.next(self.skripsi_ta)

    @step
    def skripsi_ta(self):
        # Proses Skripsi atau Tugas Akhir (TA)
        print("Menyelesaikan Skripsi atau Tugas Akhir sebagai syarat kelulusan")
        self.has_passed_ta = input("Apakah mahasiswa lulus Skripsi/TA? (ya/tidak): ").lower() == "ya"
        
        # Cek apakah mahasiswa lulus atau perlu mengulang TA
        if self.has_passed_ta:
            self.next(self.graduation)
        else:
            print("Mahasiswa belum lulus TA. Mengulangi proses skripsi/TA.")
            self.next(self.skripsi_ta)

    @step
    def graduation(self):
        # Wisuda, tahap terakhir
        print("Selamat! Mahasiswa telah menyelesaikan semua persyaratan dan akan diwisuda.")
        print(f"IPK Akhir: {self.calculate_cumulative_gpa()}")

    def calculate_cumulative_gpa(self):
        # Menghitung IPK dari rata-rata IP tiap semester
        total_gpa = sum([self.semester_gpa])  # Sederhanakan untuk contoh, seharusnya simpan IP tiap semester
        cumulative_gpa = total_gpa / self.semester
        return cumulative_gpa

    @step
    def end(self):
        # Menyelesaikan flow
        print("Perjalanan akademik selesai.")

# Jalankan flow ini menggunakan metaflow
if __name__ == '__main__':
    UniversityJourneyFlow()
