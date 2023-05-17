from length import *
from Bacamatriks import *
from matriks import *
import variables


def help():
    print("=========== HELP ===========")
    if variables.role == "none":
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    if variables.role == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hilangkanjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan")
        print("6. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk mengambil laporan jin")
        print("8. laporancandi")
        print("   Untuk mengambil laporan candi")
        print("9. Save")
        print("   Untuk menyimpan progress permainan")
    if variables.role == "roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan sebuah candi")
        print("3. ayam berkokok")
        print("   Untuk mengakhiri permainan")
        print("4. Save")
        print("   Untuk menyimpan progress permainan")
    if variables.role == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan bahan")
        print("3. Save")
        print("   Untuk menyimpan progress permainan")
    if variables.role == "jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun sebuah candi")
        print("3. Save")
        print("   Untuk menyimpan progress permainan")

