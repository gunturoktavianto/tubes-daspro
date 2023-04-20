from functions import *

candi = matriks1("candi.csv")
def hancurkancandi(candi):
    idcandi = int(input("Masukkan ID candi: "))
    found, indeks = inmatriks(idcandi, candi)
    if found:
        sure = input(f"Apakah anda yakin ingin menghancurkan candi ID: {idcandi} (Y/N)? ")
        answer = False
        while not(answer) :
            if sure == "Y":
                answer = True ; print("")
                candi = delete(indeks, candi)
                print("Candi telah berhasil dihancurkan.")
                print(candi)
            elif sure == "N":
                answer = True ; print("")
                print("Candi batal dihancurkan.")
            else:
                print("")
                print("Jawaban tidak sesuai! Jawab dengan (Y/N)!")
                sure = input(f"Apakah anda yakin ingin menghancurkan candi ID: {idcandi} (Y/N)? ")
    else:
        print("")
        print("Tidak ada candi dengan ID tersebut")
    return candi

candi = matriks1("candi.csv")
for i in range(5):
    candi = hancurkancandi(candi)

