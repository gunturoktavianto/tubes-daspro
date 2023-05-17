import variables
from length import *
from Bacamatriks import *


def laporancandi():
    totalcandi = length(variables.candi) - 1
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    if length(variables.candi) == 1:
        harga = '-'
    else:
        harga = (int(Bacamatriks(3, 1, variables.candi)) * 10000) + (int(Bacamatriks(4, 1, variables.candi)) * 15000) + (int(Bacamatriks(5, 1, variables.candi)) * 7500)
    termahal = [Bacamatriks(1, 1, variables.candi), harga]
    termurah = [Bacamatriks(1, 1, variables.candi), harga]
    for i in range(1, length(variables.candi)):
        pasir_terpakai = int(Bacamatriks(3, i, variables.candi))
        batu_terpakai = int(Bacamatriks(4, i, variables.candi))
        air_terpakai = int(Bacamatriks(5, i, variables.candi))
        totalpasir += pasir_terpakai
        totalbatu += batu_terpakai
        totalair += air_terpakai
        harga = (pasir_terpakai * 10000) + (batu_terpakai * 15000) + (air_terpakai * 7500)
        if harga > termahal[1]:
            termahal = [Bacamatriks(1, i, variables.candi), harga]
        if harga < termurah[1]:
            termurah = [Bacamatriks(1, i, variables.candi), harga]

    print('Total Candi:', totalcandi)
    print('Total Pasir yang digunakan:', totalpasir)
    print('Total Batu yang digunakan:', totalbatu)
    print('Total Air yang digunakan:', totalair)
    print('ID Candi Termahal:', termahal[0], '(Rp', str(termahal[1]) + ')')
    print('ID Candi Termurah:', termurah[0], '(Rp', str(termurah[1]) + ')')
    
