from length import *
from Bacamatriks import *
import variables


def laporanjin():
    # Menghitung jumlah jin pengumpul dan jin pembangun
    jinpengumpul = 0
    jinpembangun = 0
    for i in range(length(variables.users)):
        if Bacamatriks(3, i, variables.users) == 'jin_pembangun':
            jinpembangun += 1
        elif Bacamatriks(3, i, variables.users) == 'jin_pengumpul':
            jinpengumpul += 1
    totaljin = jinpengumpul + jinpembangun

    # Mencari jin terajin dan termalas
    # membuat matriks berisi usersname jin dengan banyak variables.candi yang dibuat
    jin = [['nama jin', 0] for i in range(jinpembangun)]
    panjangjin = jinpembangun
    j = 0
    for i in range(length(variables.users)):
        if Bacamatriks(3, i, variables.users) == 'jin_pembangun':
            jin[j][0] = Bacamatriks(1, i, variables.users)
            j += 1
    # mengisi jumlah variables.candi yang dibuat masing2 jin ke dalam matriks jin
    for i in range(1, length(variables.candi)):
        mark = False
        # mengecek apakah pembuat variables.candi ada di matriks jin atau tidak
        for j in range(panjangjin):
            if Bacamatriks(2, i, variables.candi) == jin[j][0]:
                mark = True
                indeks = j
                break
        if mark == True:  # jin ada di matriks jin
            jin[j][1] += 1  # variables.candi ditambah 1
        else:  # jin belum ada di matriks jin
            temp = [['nama jin', 0] for a in range(panjangjin + 1)]
            for k in range(panjangjin):
                temp[k] = jin[k]
            # jin dimasukkan ke dalam matriks jin lalu variables.candi ditambah 1
            temp[panjangjin] = [Bacamatriks(2, i, variables.candi), 1]
            jin = temp
            panjangjin += 1

    # mencari jin terajin
    if jin == []:
        jinterajin = '-'
    else:
        jinterajin = jin[0]
        for i in range(panjangjin):
            if jin[i][1] > jinterajin[1]:
                jinterajin = jin[i]
            elif jin[i][1] == jinterajin[1]:
                if jin[i][0] < jinterajin[0]:
                    jinterajin = jin[i]
    # mencari jin termalas
    if jin == []:
        jintermalas = '-'
    else:
        jintermalas = jin[0]
        for i in range(panjangjin):
            if jin[i][1] < jintermalas[1]:
                jintermalas = jin[i]
            elif jin[i][1] == jintermalas[1]:
                if jin[i][0] > jintermalas[0]:
                    jintermalas = jin[i]

    # Menghitung total variables.bahan bangunan
    # pasir = 0
    # air = 0
    # batu = 0
    # for i in range(length(variables.bahan)):
    #     if Bacamatriks(1, i, variables.bahan) == 'pasir':
    #         pasir += int(Bacamatriks(3, i, variables.bahan))
    #     elif Bacamatriks(1, i, variables.bahan) == 'air':
    #         air += int(Bacamatriks(3, i, variables.bahan))
    #     elif Bacamatriks(1, i, variables.bahan) == 'batu':
    #         batu += int(Bacamatriks(3, i, variables.bahan))

    print('Total Jin:', totaljin)
    print('Total Jin Pengumpul:', jinpengumpul)
    print('Total Jin Pembangun:', jinpembangun)
    print('Jin Terajin:', jinterajin[0])
    print('Jin Termalas:', jintermalas[0])
    print('Jumlah Pasir:', variables.punya_pasir, 'unit')
    print('Jumlah Air:', variables.punya_air, 'unit')
    print('Jumlah Batu:', variables.punya_batu, 'unit')
    
