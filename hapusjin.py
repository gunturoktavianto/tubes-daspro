from length import *
from Bacamatriks import *
from matriks import *

def hapusjin () :
    global user
    global candi
    baris = length(user)
    hapus = str(input('Masukkan username jin : '))
    mark = True
    for i in range(baris) : # mengecek username jin pada matriks data
        if Bacamatriks(1 , i , user) == hapus :
            if (Bacamatriks(3,i,user) == 'jin_pengumpul') or (Bacamatriks(3,i,user) == 'jin_pembangun') :
                mark = False
                break
    if mark == True :
        print('Tidak ada jin dengan username tersebut.')
    else :
        final = str(input('Apakah anda yakin ingin menghapus jin dengan username ' + hapus + ' (Y/N)?'))
        if final == 'Y' or final == 'y' :
            print('Jin telah berhasil dihapus dari alam gaib.')
            # menghapus jin pada matriks user
            temp = [0 for i in range(baris)]
            j = 0
            for i in range(baris) :
                if Bacamatriks(1 , i , user) != hapus :
                    temp[j] = user[i]
                    j += 1
            temp[baris - 1] = ''
            user = temp
            # menghitung candi yang dibuat jin
            count = 0
            for i in range(length(candi)) :
                if Bacamatriks(2 , i , candi) == hapus :
                    count += 1
            j = 0
            if count > 0 : # menghapus semua candi yang dibuat jin
                temp = [0 for i in range(length(candi) - count + 1)]
                for i in range(length(candi) - count + 1) :
                    if Bacamatriks(2 , i , candi) != hapus :
                        temp[j] = candi[i]
                        j += 1
                temp[length(candi) - count] = ''
                candi = temp
