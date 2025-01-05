# Program ilustrasi proses mengikuti kuliah di informatika menggunakan kelas

class KuliahInformatika:
    def __init__(self):
        self.daftar_matkul = []
        self.performance = {}

    def bayar_spp(self):
        print("SPP berhasil dibayarkan!")

    def daftar_matakuliah(self):
        self.daftar_matkul = ["Pemrograman Dasar", "Struktur Data", "Sistem Operasi"]
        print("Mata kuliah berhasil didaftarkan!")

    def ikuti_perkuliahan(self):
        print("Anda sedang mengikuti perkuliahan:")
        for matkul in self.daftar_matkul:
            print(f"- {matkul}")
        self.performance = {matkul: [] for matkul in self.daftar_matkul}

    def kerjakan_tugas(self):
        for matkul in self.performance:
            tugas = int(input(f"Masukkan nilai tugas untuk {matkul} (0-100): "))
            self.performance[matkul].append(tugas)
        print("Nilai tugas berhasil dimasukkan.")

    def ikuti_ujian(self):
        for matkul in self.performance:
            ujian = int(input(f"Masukkan nilai ujian untuk {matkul} (0-100): "))
            self.performance[matkul].append(ujian)
        print("Nilai ujian berhasil dimasukkan.")

    def hitung_nilai_akhir(self):
        self.nilai_akhir = {}
        for matkul, nilai in self.performance.items():
            if len(nilai) >= 2:
                tugas, ujian = nilai[0], nilai[1]
                self.nilai_akhir[matkul] = tugas * 0.4 + ujian * 0.6
        print("Nilai akhir berhasil dihitung.")

    def tampilkan_nilai_akhir(self):
        print("\nNilai akhir mata kuliah:")
        for matkul, nilai in self.nilai_akhir.items():
            print(f"- {matkul}: {nilai:.2f}")

def main():
    print("Selamat datang di simulasi kuliah informatika!")

    kuliah = KuliahInformatika()

    # Proses 1: Bayar SPP
    kuliah.bayar_spp()

    # Proses 2: Daftar mata kuliah
    kuliah.daftar_matakuliah()

    # Proses 3: Ikuti perkuliahan
    kuliah.ikuti_perkuliahan()

    # Proses 4: Kerjakan tugas
    kuliah.kerjakan_tugas()

    # Proses 5: Ikuti ujian
    kuliah.ikuti_ujian()

    # Proses 6: Hitung nilai akhir
    kuliah.hitung_nilai_akhir()

    # Proses 7: Tampilkan nilai akhir
    kuliah.tampilkan_nilai_akhir()

if __name__ == "__main__":
    main()
