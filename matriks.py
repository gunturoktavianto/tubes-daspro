from hitungbaris import *

def matriks() :
    f = open('user.csv')
    baris = hitungbaris('user.csv') + 1
    global user
    user = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1) :
            a = a + cc[j]
        user[i] = a
    user[baris] = ''
    f.close()

    f = open('candi.csv')
    baris = hitungbaris('candi.csv') + 1
    global candi
    candi = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1) :
            a = a + cc[j]
        candi[i] = a
    candi[baris] = ''
    f.close()

    f = open('bahan_bangunan.csv')
    baris = hitungbaris('bahan_bangunan.csv') + 1
    global bahan
    bahan = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1) :
            a = a + cc[j]
        bahan[i] = a
    bahan[baris] = ''
    f.close()
matriks()

