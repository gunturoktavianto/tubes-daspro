import random
from Bacamatriks import *
from matriks import *
from hitungbaris import *

# header itu 1,2,3 untuk nama,deskripsi,jumlah
# baris 0,1,2,3 untuk header, pasir, batu, air

def kumpul():
    
    global pasir, batu, air
    pasir = random.randint(0,5) # random bahan yang dikumpulkan jin
    batu = random.randint(0,5)
    air = random.randint(0,5)

    if hitungbaris('bahan_bangunan.csv') == 3 :
        for i in range (1, 4): # untuk kasus udah ada matriksnya
            if Bacamatriks(1, i, bahan) == 'pasir' or Bacamatriks(1, i, bahan) == 'Pasir' : # menjumlahkan dan menulis ulang matriks
                bahan[i] = f'pasir;descpasir;{Bacamatriks(3, i, bahan) + pasir}'
            elif Bacamatriks(1, i, bahan) == 'air' or Bacamatriks(1, i, bahan) == 'Air' :
                bahan[i] = f'air;descair;{Bacamatriks(3, i, bahan) + air}'
            elif Bacamatriks(1, i, bahan) == 'batu' or Bacamatriks(1, i, bahan) == 'Batu' :
                bahan[i] = f'batu;descbatu;{Bacamatriks(3, i, bahan) + batu}'
    else : # untuk kasus matriksnya baru ada header
        bahan = ['nama;deskripsi;jumlah', f'pasir;descpasir;{pasir}', f'batu;deskripsibatu;{batu}', f'pasir;descair;{air}'] # 

def printF07(): # printnya dipisah agar fungsi kumpul langsung bisa dipake f08 batchkumpul
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")