from matriks import *
import time

def ayamberkokok(): 
    jumlah = length(candi) - 1 # jumlah harus {length(candi) - 1} karena dikurang header
    if jumlah < 100 :
        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        time.sleep(1)
        print("Jumlah Candi: " + str(jumlah))
        print("")
        time.sleep(1)
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        time.sleep(1)
        print("*Bandung Bondowoso angry noise*")
        time.sleep(1)
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Kukuruyuk.. Kukuruyuk..")
        print("")
        time.sleep(1)
        print("Jumlah Candi: " + str(jumlah))
        print("")
        time.sleep(1)
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        
ayamberkokok()
