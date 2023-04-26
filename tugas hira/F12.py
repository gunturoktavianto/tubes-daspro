from matriks import *
from F11 import *

def ayamberkokok(jumlah): # jumlah yang dimasukkan harus {length(candi) - 1} karena dikurang header
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


candi = hancurkancandi(candi)

ayamberkokok(length(candi)-1)
