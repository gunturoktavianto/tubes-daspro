from hitungbaris import *
def matriks() :
    f = open('user.csv')
    baris = hitungbaris('user.csv') + 1
    global user
    user = [0 for i in range(baris)]
    for i in range(baris) :
        cc = f.readline()
        user[i] = cc
    f.close()

    f = open('candi.csv')
    baris = hitungbaris('candi.csv') + 1
    global candi
    candi = [0 for i in range(baris)]
    for i in range(baris) :
        cc = f.readline()
        candi[i] = cc
    f.close()

    f = open('bahan_bangunan.csv')
    baris = hitungbaris('bahan_bangunan.csv') + 1
    global bahan
    bahan = [0 for i in range(baris)]
    for i in range(baris) :
        cc = f.readline()
        bahan[i] = cc
    f.close()
  
matriks()
print(user)
print(candi)
print(bahan)
