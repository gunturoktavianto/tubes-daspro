from matriks import *
from length import *
import variables


def inmatriks(variable, matriks):  # fungsi digunakan untuk mencari indeks id yang diinginkan
    a = []
    for i in range(1, length(matriks)):
        word = ''
        for char in matriks[i]:
            if char == ";":
                break
            else:
                word = word + char  # untuk mendapatkan id dari character matriks
        kata = word  # menyimpan id dari matriks pada variabel kata
        if kata == str(variable):  # jika id dari matriks sama dengan id yang diinginkan
            # menyimpan matriks id yang diinginkan untuk pengecekan
            a = matriks[i]
            indeks = i  # mendapatkan indeks id yang diinginkan
    if a != []:
        value = True  # value true apabila ditemukan yakni terdapat matriks yang disimpan
    else:
        value = False
        indeks = 0
    return value, indeks  # mengembalikan value untuk pengecekan keberadaan id,
    # mengembalikan indeks untuk apabila ditemukan maka akan masuk ke
    # fungsi deletecandi yang menggunakan indeks sebagai parameternya


def deletecandi(index, line, candi):
    newcandi = ['' for _ in range(103)]
    j = 0
    for i in range(line+1):
        if i != index:
            newcandi[j] = candi[i]
            j += 1
    newcandi[line] = ''
    candi = newcandi
    return candi


def hancurkancandi():
    idcandi = int(input("Masukkan ID candi: "))
    baris = length(variables.candi)
    found, indeks = inmatriks(idcandi, variables.candi)
    if found:
        sure = input(
            f"Apakah anda yakin ingin menghancurkan candi ID: {idcandi} (Y/N)? ")
        answer = False
        while not (answer):
            if sure == "Y":
                answer = True
                print("")
                variables.candi = deletecandi(indeks, baris, variables.candi)
                variables.lst_avail_id[idcandi] = idcandi
                print("Candi telah berhasil dihancurkan.")
            elif sure == "N":
                answer = True
                print("")
                print("Candi batal dihancurkan.")
            else:
                print("")
                print("Jawaban tidak sesuai! Jawab dengan (Y/N)!")
                sure = input(
                    f"Apakah anda yakin ingin menghancurkan candi ID: {idcandi} (Y/N)? ")
    else:
        print("")
        print("Tidak ada candi dengan ID tersebut")
 
