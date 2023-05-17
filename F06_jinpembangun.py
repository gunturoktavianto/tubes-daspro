import random
from Bacamatriks import *
from matriks import *
from hitungbaris import *
import variables
from length import *


def bangun():
    global butuh_pasir, butuh_batu, butuh_air
    butuh_pasir = random.randint(1, 5)
    butuh_batu = random.randint(1, 5)
    butuh_air = random.randint(1, 5) 
    if length(variables.candi) - 1 == 100:
        print(f'Sisa candi yang perlu dibangun: 0')
    else:
        if butuh_pasir > variables.punya_pasir or butuh_batu > variables.punya_batu or butuh_air > variables.punya_air:
            print('Bahan bangunan tidak mencukupi.')
            print('Candi tidak bisa dibangun!')
        else:
            variables.punya_pasir -= butuh_pasir
            variables.punya_batu -= butuh_batu
            variables.punya_air -= butuh_air
            
            # store id;pembuat;pasir;batu;air ke matriks candi
            baris_candi = length(variables.candi)

            for i in range(100):
                if variables.lst_avail_id[i] == i:
                    id_candi = i
                    variables.lst_avail_id[i] = ''
                    break

            tambahan_candi = str(id_candi) + ';' + variables.username + ';' + \
str(butuh_pasir) + ';' + str(butuh_batu) + ';' + str(butuh_air)
            
            variables.candi[baris_candi] = tambahan_candi

            temp_candi = ['' for _ in range(103)]

            for i in range(baris_candi + 1):
                temp_candi[i] = variables.candi[i]

            temp_candi[i+1] = ''
            variables.candi = temp_candi
            print(f'Candi berhasil dibangun. Sisa candi yang perlu dibangun: {101-length(variables.candi)}')
