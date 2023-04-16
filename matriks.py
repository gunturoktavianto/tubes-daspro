from hitungbaris import *
from length import *
from Bacamatriks import *
from summonjin import summonjin

def matriks() :
    f = open('user.csv')
    baris = hitungbaris('user.csv') + 1
    global user
    user = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        user[i] = cc
    user[baris] = ''
    f.close()

    f = open('candi.csv')
    baris = hitungbaris('candi.csv') + 1
    global candi
    candi = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        candi[i] = cc
    candi[baris] = ''
    f.close()

    f = open('bahan_bangunan.csv')
    baris = hitungbaris('bahan_bangunan.csv') + 1
    global bahan
    bahan = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        bahan[i] = cc
    bahan[baris] = ''
    f.close()
