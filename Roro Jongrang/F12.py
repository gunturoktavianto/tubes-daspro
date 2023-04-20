from functions import *

def ayamberkokok(jumlah):
    cek = False
    if jumlah < 100 :
        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        print("Jumlah Candi: " + str(jumlah))
        print("")
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        print("Jumlah Candi: " + str(jumlah))
        print("")
        print("Yah, Bandung Bondowoso memenangkan permainan!")


candi = matriks1("candi.csv")
ayamberkokok(length(candi))