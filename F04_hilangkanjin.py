from length import *
from Bacamatriks import *
import variables

def hapusjin () :
    baris = length(variables.users)
    hapus = str(input('Masukkan username jin : '))
    mark = True
    for i in range(baris) : # mengecek username jin pada matriks data
        if Bacamatriks(1 , i , variables.users) == hapus :
            if (Bacamatriks(3,i,variables.users) == 'jin_pengumpul') or (Bacamatriks(3,i,variables.users) == 'jin_pembangun') :
                mark = False
                break
    if mark == True :
        print('Tidak ada jin dengan username tersebut.')
    else :
        final = str(input('Apakah anda yakin ingin menghapus jin dengan username ' + hapus + ' (Y/N)?'))
        if final == 'Y' or final == 'y' :
            print('Jin telah berhasil dihapus dari alam gaib.')
            # menghapus jin pada matriks variables.users
            temp = [0 for i in range(baris)]
            j = 0
            for i in range(baris) :
                if Bacamatriks(1 , i , variables.users) != hapus :
                    temp[j] = variables.users[i]
                    j += 1
            temp[baris - 1] = ''
            variables.users = temp
            # menghitung variables.candi yang dibuat jin
            count = 0
            for i in range(length(variables.candi)) :
                if Bacamatriks(2 , i , variables.candi) == hapus :
                    count += 1
            j = 0
            if count > 0 : # menghapus semua variables.candi yang dibuat jin
                temp = ['' for _ in range(102)]
                for i in range(length(variables.candi)) :
                    if Bacamatriks(2 , i , variables.candi) != hapus :
                        temp[j] = variables.candi[i]
                        j += 1
                    else:
                        id = int(Bacamatriks(1, i , variables.candi))
                        variables.lst_avail_id[id] = id

                temp[length(variables.candi) - count] = ''
                variables.candi = temp
