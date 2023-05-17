def Bacamatriks (header , baris, matriks) : # nge-return dengan header dan baris yang kita mau
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