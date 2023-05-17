# File: main.py
import F01_login
import F02_logout
import F03_summonjin
import F04_hilangkanjin
import F05_ubahtipejin
import F06_jinpembangun
import F07_jinpengumpul
import F08_batchkumpulbangun
import F09_laporanjin
import F10_laporancandi
import F11_hancurkancandi
import F12_ayamberkokok
import F13_load
import F14_save
import F15_help
import F16_exit
import variables
from Bacamatriks import *
from hitungbaris import *


# load("user.csv", users)
# load("candi.csv", candi)
# load("bahan_bangunan.csv", bahan_bangunan)

while variables.inputan_exit_valid == False:
    masukan = input(">>> ")
    # F01
    if masukan == "login":
        F01_login.login()
    # F02
    elif masukan == "logout":
        F02_logout.logout()
    # F03
    elif masukan == "summonjin":
        if variables.role == "bandung_bondowoso":
            F03_summonjin.summonjin()
        else:
            print("Anda tidak memiliki akses untuk memanggil jin!")
    # F04
    elif masukan == "hapusjin":
        if variables.role == "bandung_bondowoso":
            F04_hilangkanjin.hapusjin()
        else:
            print("Anda tidak memiliki akses untuk menghapus jin!")
    # F05
    elif masukan == "ubahjin":
        if variables.role == "bandung_bondowoso":
            F05_ubahtipejin.ubahjin()
        else:
            print("Anda tidak memiliki akses untuk mengubah tipe jin!")
    # F06
    elif masukan == "bangun":
        if variables.role == "jin_pembangun":
            F06_jinpembangun.bangun()
        else:
            print("Anda tidak memiliki akses untuk membangun candi!")
    # F07
    elif masukan == "kumpul":
        if variables.role == "jin_pengumpul":
            F07_jinpengumpul.kumpul()
            F07_jinpengumpul.printF07()
        else:
            print("Anda tidak memiliki akses untuk mengumpulkan bahan!")
    # F08a
    elif masukan == "batchkumpul":
        if variables.role == "bandung_bondowoso":
            F08_batchkumpulbangun.batchkumpul()
        else:
            print(
                "Anda tidak memiliki akses untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan")
    # F08a
    elif masukan == "batchbangun":
        if variables.role == "bandung_bondowoso":
            F08_batchkumpulbangun.batchbangun()
        else:
            print(
                "Anda tidak memiliki akses untuk mengerahkan seluruh pasukan jin untuk membangun candi")
    # F09
    elif masukan == "laporanjin":
        if variables.role == "bandung_bondowoso":
            F09_laporanjin.laporanjin()
        else:
            print("Anda tidak memiliki akses untuk mengambil laporan jin")
    # F10
    elif masukan == "laporancandi":
        if variables.role == "bandung_bondowoso":
            F10_laporancandi.laporancandi()
        else:
            print("Anda tidak memiliki akses untuk mengambil laporan candi")
    # F11
    elif masukan == "hancurkancandi":
        if variables.role == "roro_jonggrang":
            F11_hancurkancandi.hancurkancandi()
        else:
            print("Anda tidak memiliki akses untuk menghancurkan candi")
    # F12
    elif masukan == "ayamberkokok":
        if variables.role == "roro_jonggrang":
            F12_ayamberkokok.ayamberkokok()
        else:
            print("Anda tidak memiliki akses untuk menghancurkan candi")
    # F14
    elif masukan == "save":
        F14_save.save()
    # F15
    elif masukan == "help":
        F15_help.help()
    # F16
    elif masukan == "exit":
        F16_exit.exit()
