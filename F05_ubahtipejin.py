from length import *
from Bacamatriks import *
import variables

def ubahjin() :
    jin = str(input('Masukkan username jin : '))
    indeks = 0
    mark = False
    for i in range(length(variables.users)) : # mengecek username pada matriks data
        if Bacamatriks(1 , i , variables.users) == jin :
            mark = True
            indeks = i
            break
    tipe = Bacamatriks(3 , indeks , variables.users)
    if mark == False : 
        print('Tidak ada jin dengan username tersebut.')
    else :
        if tipe != 'jin_pengumpul' and tipe != 'jin_pembangun' : # mengecek apakah username adalah jin
          print('Tidak ada jin dengan username tersebut.')
        else :          
            if tipe == 'jin_pengumpul' :
                ganti = 'jin_pembangun'
            else :
                ganti = 'jin_pengumpul'
            final = str(input('Jin ini bertipe “' + tipe + '”. Yakin ingin mengubah ke tipe “' + ganti + '" (Y/N)?'))
            if final == 'Y' or final == 'y' : # tipe jin diubah
                variables.users[indeks] = Bacamatriks(1,indeks,variables.users) + ';' + Bacamatriks(2,indeks,variables.users) + ';' + ganti
                print('\nJin telah berhasil diubah')
