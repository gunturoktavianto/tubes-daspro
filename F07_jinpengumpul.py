import random
import variables
from Bacamatriks import *
from length import *


# header itu 1,2,3 untuk nama,deskripsi,jumlah
# baris 0,1,2,3 untuk header, pasir, batu, air

def kumpul():
    variables.pasir = random.randint(0,5) # random variables.bahan yang dikumpulkan jin
    variables.batu = random.randint(0,5)
    variables.air = random.randint(0,5)

    variables.punya_pasir += variables.pasir
    variables.punya_batu += variables.batu
    variables.punya_air += variables.air

    variables.bahan = ['nama;deskripsi;jumlah', f'pasir;descpasir;{variables.punya_pasir}', f'batu;deskripsibatu;{variables.punya_batu}', f'air;descair;{variables.punya_air}', ''] # 

def printF07(): # printnya dipisah agar fungsi kumpul langsung bisa dipake f08 batchkumpul
    print(f"Jin menemukan {variables.pasir} pasir, {variables.batu} batu, dan {variables.air} air.")