from length import *
from Bacamatriks import *
from matriks import *

def laporancandi() :
    totalcandi = length(candi) - 1
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    
    harga = (int(Bacamatriks(3,1,candi)) * 10000) + (int(Bacamatriks(4,1,candi)) * 15000) + (int(Bacamatriks(5,1,candi)) * 7500)
    termahal = [Bacamatriks(1 , 1 , candi) , harga]
    termurah = [Bacamatriks(1 , 1 , candi) , harga]
    for i in range(1 , length(candi)) :
        pasir = int(Bacamatriks(3 , i , candi))
        batu = int(Bacamatriks(4 , i , candi))
        air = int(Bacamatriks(5 , i , candi))
        totalpasir += pasir
        totalbatu += batu
        totalair += air
        harga = (pasir * 10000) + (batu * 15000) + (air * 7500)
        if harga > termahal[1] :
            termahal = [Bacamatriks(1,i,candi) , harga]
        if harga < termurah[1] :
            termurah = [Bacamatriks(1,i,candi) , harga]

    print('Total Candi:' , totalcandi)
    print('Total Pasir yang digunakan:' , totalpasir)
    print('Total Batu yang digunakan:' , totalbatu)
    print('Total Air yang digunakan:' , totalair)
    print('ID Candi Termahal:' , termahal[0] , '(Rp' , str(termahal[1]) + ')')
    print('ID Candi Termurah:' , termurah[0] , '(Rp' , str(termurah[1]) + ')')

laporancandi()