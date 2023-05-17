import variables
import time
from length import *


def ayamberkokok():
    # jumlah harus {length(variables.candi) - 1} karena dikurang header
    jumlah = length(variables.candi) - 1
    if jumlah < 100:
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
    variables.inputan_exit_valid = True
