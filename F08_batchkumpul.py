from F07_jinpengumpul import *
from length import *

def batchkumpul():
    jumlah = 0 
    pasirtotal = 0
    batutotal = 0
    airtotal = 0

    baris = length(user)

    for i in range(baris): # untuk menghitung berapa jumlah jin pengumpul
        if Bacamatriks(3, i, user) == 'jin_pengumpul':
            jumlah += 1

    for i in range (jumlah): 
        kumpul()
        pasirtotal += pasir # ngejumlah berapa banyak bahan yang terkumpul dalam sekali batchkumpul
        batutotal += batu
        airtotal += air

    print(f'Mengerahkan {jumlah} jin untuk mengumpulkan bahan.')
    print(f'Jin menemukan total {pasirtotal} pasir, {batutotal} batu, dan {airtotal} air.')
        

