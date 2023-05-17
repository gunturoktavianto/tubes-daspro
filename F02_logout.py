from length import *
from Bacamatriks import *
from matriks import *
import variables

def logout():
    if variables.login_status == True:
        print("Logout berhasil!")
        variables.login_status = False
    else:
        print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")