from length import *
from Bacamatriks import *
from matriks import *

def laporanjin() :
    # Menghitung jumlah jin pengumpul dan jin pembangun
    jinpengumpul = 0
    jinpembangun = 0
    for i in range(length(user)) :
            if Bacamatriks(3 , i , user) == 'jin_pembangun' :
                jinpembangun += 1
            elif Bacamatriks(3 , i , user) == 'jin_pengumpul' :
                jinpengumpul += 1
    totaljin = jinpengumpul + jinpembangun

    # Mencari jin terajin dan termalas
    # membuat matriks berisi username jin dengan banyak candi yang dibuat
    jin = [['nama jin' , 0] for i in range(jinpembangun)] 
    panjangjin = jinpembangun
    j = 0
    for i in range(length(user)) :
        if Bacamatriks(3 , i , user) == 'jin_pembangun' :
            jin[j][0] = Bacamatriks(1 , i , user)
            j += 1
    # mengisi jumlah candi yang dibuat masing2 jin ke dalam matriks jin
    for i in range(1 , length(candi)) :
        mark = False
        for j in range(panjangjin) : # mengecek apakah pembuat candi ada di matriks jin atau tidak
            if Bacamatriks(2 , i , candi) == jin[j][0] :
                 mark = True
                 indeks = j
                 break
        if mark == True : # jin ada di matriks jin
                jin[j][1] += 1 # candi ditambah 1
        else : # jin belum ada di matriks jin
            temp = [['nama jin' , 0] for a in range(panjangjin + 1)]
            for k in range(panjangjin) :
                temp[k] = jin[k]
            temp[panjangjin] = [Bacamatriks(2,i,candi),1] # jin dimasukkan ke dalam matriks jin lalu candi ditambah 1
            jin = temp
            panjangjin += 1
    
    # mencari jin terajin
    if jin == [] :
        jinterajin = '-'
    else :
        jinterajin = jin[0]
        for i in range(panjangjin) :
            if jin[i][1] > jinterajin[1] :
                jinterajin = jin[i]
            elif jin[i][1] == jinterajin[1] :
                if jin[i][0] < jinterajin[0] :
                    jinterajin = jin[i]
    # mencari jin termalas
    if jin == [] :
        jintermalas = '-'
    else :
        jintermalas = jin[0]
        for i in range(panjangjin) :
            if jin[i][1] < jintermalas[1] :
                jintermalas = jin[i]
            elif jin[i][1] == jintermalas[1] :
                if jin[i][0] > jintermalas[0] :
                    jintermalas = jin[i]              

    # Menghitung total bahan bangunan
    pasir = 0
    air = 0
    batu = 0
    for i in range(length(bahan)) :
        if Bacamatriks(1 , i , bahan) == 'pasir' :
             pasir += int(Bacamatriks(3 , i , bahan))
        elif Bacamatriks(1 , i ,bahan) == 'air' :
             air += int(Bacamatriks(3 , i , bahan))
        elif Bacamatriks(1 , i , bahan) == 'batu' :
             batu += int(Bacamatriks(3 , i , bahan))

    print('Total Jin:' , totaljin)
    print('Total Jin Pengumpul:' , jinpengumpul)
    print('Total Jin Pembangun:' , jinpembangun)
    print('Jin Terajin:' , jinterajin[0])    
    print('Jin Termalas:' , jintermalas[0])
    print('Jumlah Pasir:' , pasir , 'unit')
    print('Jumlah Air:' , air , 'unit')
    print('Jumlah Batu:' , batu , 'unit')