import random
from Bacamatriks import *
from matriks import *

# header itu 1,2,3 untuk nama,deskripsi,jumlah
# baris 0,1,2,3 untuk header, pasir, batu, air

def kumpul():

    global pasir, batu, air

    pasirtotal = Bacamatriks(3, 1, bahan) # Mengambil data bahan awal di matriks
    batutotal = Bacamatriks(3, 2, bahan)
    airtotal = Bacamatriks(3, 3, bahan)
    
    pasir = random.randint(0,5) # random bahan yang dikumpulkan jin
    batu = random.randint(0,5)
    air = random.randint(0,5)

    pasirtotal = int(pasirtotal) + pasir # menjumlahkan data bahan awal dengan hasil yang dikumpulkan jin
    batutotal = int(batutotal) + batu
    airtotal = int(airtotal) + air

    bahan[1] = f'pasir;descpasir;{pasirtotal}' # menulis ulang matriks
    bahan[2] = f'batu;descbatu;{batutotal}'
    bahan[3] = f'air;descair;{airtotal}'

def printF07(): # printnya dipisah agar fungsi kumpul langsung bisa dipake f08
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")