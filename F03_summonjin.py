from length import *
from Bacamatriks import *
import variables


def summonjin():
    baris = length(variables.users)
    count = 0
    
    for i in range(baris):  # menghitung jumlah jin
        if Bacamatriks(3, i+1, variables.users) == 'jin_pengumpul' or Bacamatriks(3, i+1, variables.users) == 'jin_pembangun':
            count += 1

    if count == 100:  # mengecek apakah sudah maksimal
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi)")
        jenisjin = 0
        while jenisjin == 0:  # input jenis jin
            jenisjin = int(
                input('Masukkan nomor jenis jin yang ingin dipanggil: '))
                
            if jenisjin != 1 and jenisjin != 2:
                print('Tidak ada jenis jin bernomor "' + str(jenisjin) + '"!')
                jenisjin = 0

        if jenisjin == 1:
            print('Memilih jin “Pengumpul”.')
        else:
            print('Memilih jin “Pembangun”.')

        mark = False
        while mark == False:
            username = str(input('Masukkan username jin: '))
            for i in range(baris):  # mengecek username valid atau tidak
                if Bacamatriks(1, i+1, variables.users) == username:
                    print('Username “' + str(username) + '” sudah diambil!')
                    mark = False
                    break
                else:
                    mark = True

        password = str(input('Masukkan password jin: '))
        mark = False
        while mark == False:  # validasi password
            if len(password) >= 5 and len(password) <= 25:
                mark = True
            else:
                print('Password panjangnya harus 5-25 karakter!')
                password = str(input('Masukkan password jin: '))

        print('Mengumpulkan sesajen... ')
        print('Menyerahkan sesajen... ')
        print('Membacakan mantra... ')

        print('Jin ' + str(username) + ' berhasil dipanggil!')

        if jenisjin == 1:
            role = 'jin_pengumpul'
        else:
            role = 'jin_pembangun'

        # jin dimasukkan ke dalam matriks data
        tambahan = username + ';' + password + ';' + role
        variables.users[baris] = tambahan
        temp = [0 for _ in range(baris+2)]
        
        for i in range(baris + 1):
            temp[i] = variables.users[i]
            
        temp[i+1] = ''
        
        variables.users = temp
       
