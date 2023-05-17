import variables
from hitungbaris import *
from Bacamatriks import *

def matriks(path):
    f = open(f'{path}/user.csv')
    baris = hitungbaris(f'{path}/user.csv') + 1
    variables.users = [0 for i in range(baris+1)]
    for i in range(baris):
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1):
            a = a + cc[j]
        variables.users[i] = a
    variables.users[baris] = ''
    f.close()

    f = open(f'{path}/candi.csv')
    baris = hitungbaris(f'{path}/candi.csv') + 1
    variables.candi = ['' for _ in range(102)]
    for i in range(baris):
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1):
            a = a + cc[j]
        variables.candi[i] = a
    variables.candi[baris] = ''
    f.close()


    f = open(f'{path}/bahan_bangunan.csv')
    baris = hitungbaris(f'{path}/bahan_bangunan.csv') + 1
    variables.bahan = [0 for i in range(baris+1)]
    for i in range(baris):
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1):
            a = a + cc[j]
        variables.bahan[i] = a
    variables.bahan[baris] = ''
    f.close()
    
    if baris == 1:
        variables.punya_pasir = 0
        variables.punya_batu = 0
        variables.punya_air = 0
    else:
        variables.punya_pasir = int(Bacamatriks(3, 1, variables.bahan))
        variables.punya_batu = int(Bacamatriks(3, 2, variables.bahan))
        variables.punya_air = int(Bacamatriks(3, 3, variables.bahan))
        


