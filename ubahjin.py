from length import *
from Bacamatriks import *
from matriks import *

def ubahjin() :
    global user
    jin = str(input('Masukkan username jin : '))
    indeks = 0
    mark = False
    for i in range(length(user)) :
        if Bacamatriks(1 , i , user) == jin :
            mark = True
            indeks = i
            break
    tipe = Bacamatriks(3 , indeks , user)
    if mark == False : 
        print('Tidak ada jin dengan username tersebut.')
    else :
        if tipe != 'jin_pengumpul' and tipe != 'jin_pembangun' :
          print('Tidak ada jin dengan username tersebut.')
        else :          
            if tipe == 'jin_pengumpul' :
                ganti = 'jin_pembangun'
            else :
                ganti = 'jin_pengumpul'
            final = str(input('Jin ini bertipe “' + tipe + '”. Yakin ingin mengubah ke tipe “' + ganti + '" (Y/N)?'))
            if final == 'Y' or final == 'y' :
                user[indeks] = Bacamatriks(1,indeks,user) + ';' + Bacamatriks(2,indeks,user) + ';' + ganti

print(user)
ubahjin()
print(user)