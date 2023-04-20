def Bacamatriks (header , baris , matriks) : # nge-return dengan header dan baris yang kita mau
    kata = ''
    # header itu 1,2,3 untuk username,password,role
    cc = matriks[baris]
    for i in range(len(cc)) :
        if header == 1 :
            if cc[i] == ';' :
                break
            else :
                kata = kata + cc[i]
        else :
            if cc[i] == ';' :
                header -= 1
    return kata

def hitungbaris(namafile) : #ngitung ada berapa baris di user.csv (header ga keitung)
    f = open(namafile)
    cc = f.readline()
    cc = f.readline()
    baris = 0
    while cc != '' :
        baris += 1
        cc = f.readline()
    f.close()
    return baris

def length(matriks) :
    mark = True
    count = 0
    i = 0
    while mark == True :
        if matriks[i] != '' :
            count += 1
            i += 1
        else :
            mark = False
    return count

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
    

def matriks1(namafile) :
    f = open(namafile)
    baris = hitungbaris(namafile) + 1
    global user
    matriks = [0 for i in range(baris+1)]
    for i in range(baris) :
        cc = f.readline()
        a = ''
        for j in range(len(cc) - 1) :
            a = a + cc[j]
        matriks[i] = a
    matriks[baris] = ''
    f.close()
    return matriks

def inmatriks(variable, matriks):
    a =[]
    for i in range(1,length(matriks)):
        word = ''
        for char in matriks[i]:
            if char == ";":
                break
            else:
                word = word + char
        kata = word
        if kata == str(variable):
            a = matriks[i]
            indeks = i
    if a != []:
        value = True
    else:
        value = False
        indeks = 0
    return value,indeks

def delete(index, matrix):
    for i in range(length(matrix)):
        if i == index:
            matrix[i] = " ; ; ; ;"
    return matrix
