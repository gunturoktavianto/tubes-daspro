from F07_jinpengumpul import *
from length import *
import variables


def batchkumpul():
    jumlah = 0
    pasirtotal = 0
    batutotal = 0
    airtotal = 0

    baris = length(variables.users)

    for i in range(baris):  # untuk menghitung berapa jumlah jin pengumpul
        if Bacamatriks(3, i, variables.users) == 'jin_pengumpul':
            jumlah += 1

    for i in range(jumlah):
        kumpul()
        # ngejumlah berapa banyak bahan yang terkumpul dalam sekali batchkumpul
        pasirtotal += variables.pasir
        batutotal += variables.batu
        airtotal += variables.air
    if jumlah == 0:
        print(
            'Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
    else:
        print(f'Mengerahkan {jumlah} jin untuk mengumpulkan bahan.')
        print(
            f'Jin menemukan total {pasirtotal} pasir, {batutotal} batu, dan {airtotal} air.')


def batchbangun():
    pasir_batchbangun = 0
    batu_batchbangun = 0
    air_batchbangun = 0
    baris_candi = length(variables.candi)
    jumlah_pembangun = 0

    arr_jinpembangun = [0 for _ in range(length(variables.users))]
    index_arr_jinpembangun = 0
    for i in range(length(variables.users)):
        if Bacamatriks(3, i, variables.users) == 'jin_pembangun':
            jumlah_pembangun += 1
            arr_jinpembangun[index_arr_jinpembangun] = Bacamatriks(1, i, variables.users)
            index_arr_jinpembangun += 1

    penampung_candi_batchbangun = [0 for _ in range(jumlah_pembangun)]
    lst_penampung_candiID = [0 for _ in range(jumlah_pembangun)]

    # sisa candi yang perlu dibangun lebih kecil dari jumlah jin pembangun
    global butuh_pasir, butuh_batu, butuh_air
    if(101-length(variables.candi)) < jumlah_pembangun:
        for i in range(101-length(variables.candi)):
            butuh_pasir = random.randint(1, 5)
            butuh_batu = random.randint(1, 5)
            butuh_air = random.randint(1, 5)
            pasir_batchbangun += butuh_pasir
            batu_batchbangun += butuh_batu
            air_batchbangun += butuh_air
            for j in range(100):
                if j == variables.lst_avail_id[j]:
                    id_candi = j
                    variables.lst_avail_id[j] = ''
                    break
            penampung_candi_batchbangun[i] = str(id_candi) + ';' + str(arr_jinpembangun[i]) + ';' + str(butuh_pasir) + ';' + str(butuh_batu) + ';' + str(butuh_air)
            lst_penampung_candiID[i] = id_candi

        if jumlah_pembangun == 0:
            print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
        else:
            if pasir_batchbangun <= variables.punya_pasir and batu_batchbangun <= variables.punya_batu and air_batchbangun <= variables.punya_air:
                print(f'Mengerahkan {101-length(variables.candi)} jin untuk membangun candi dengan total bahan {pasir_batchbangun} pasir, {batu_batchbangun} batu, dan {air_batchbangun} air.')
                print(f'Jin berhasil membangun total {101-length(variables.candi)} candi.')
                variables.punya_pasir -= pasir_batchbangun
                variables.punya_batu -= batu_batchbangun
                variables.punya_air -= air_batchbangun
                for i in range(101-length(variables.candi)):
                    variables.candi[baris_candi] = penampung_candi_batchbangun[i]
                    baris_candi += 1
            else:
                selisih_pasir = pasir_batchbangun - variables.punya_pasir
                selisih_batu = batu_batchbangun - variables.punya_batu
                selisih_air = air_batchbangun - variables.punya_air

                if selisih_pasir < 0:
                    selisih_pasir = 0
                if selisih_batu < 0:
                    selisih_batu = 0
                if selisih_air < 0:
                    selisih_air = 0
                print(f"Bangun gagal. Kurang {selisih_pasir} pasir, {selisih_batu} batu, dan {selisih_air} air.")
                for i in range(101-length(variables.candi)):
                    variables.lst_avail_id[lst_penampung_candiID[i]] = lst_penampung_candiID[i]
    # sisa candi yang perlu dibangun lebih besar dari jumlah jin pembangun
    else:
        for i in range(jumlah_pembangun):
            butuh_pasir = random.randint(1, 5)
            butuh_batu = random.randint(1, 5)
            butuh_air = random.randint(1, 5)
            pasir_batchbangun += butuh_pasir
            batu_batchbangun += butuh_batu
            air_batchbangun += butuh_air
            for j in range(100):
                if j == variables.lst_avail_id[j]:
                    id_candi = j
                    variables.lst_avail_id[j] = ''
                    break
            penampung_candi_batchbangun[i] = str(id_candi) + ';' + str(arr_jinpembangun[i]) + ';' + str(butuh_pasir) + ';' + str(butuh_batu) + ';' + str(butuh_air)
            lst_penampung_candiID[i] = id_candi

        if jumlah_pembangun == 0:
            print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
        else:
            if pasir_batchbangun <= variables.punya_pasir and batu_batchbangun <= variables.punya_batu and air_batchbangun <= variables.punya_air:
                print(f'Mengerahkan {jumlah_pembangun} jin untuk membangun candi dengan total bahan {pasir_batchbangun} pasir, {batu_batchbangun} batu, dan {air_batchbangun} air.')
                print(f'Jin berhasil membangun total {jumlah_pembangun} candi.')
                variables.punya_pasir -= pasir_batchbangun
                variables.punya_batu -= batu_batchbangun
                variables.punya_air -= air_batchbangun
                for i in range(jumlah_pembangun):
                    variables.candi[baris_candi] = penampung_candi_batchbangun[i]
                    baris_candi += 1
            else:
                selisih_pasir = pasir_batchbangun - variables.punya_pasir
                selisih_batu = batu_batchbangun - variables.punya_batu
                selisih_air = air_batchbangun - variables.punya_air

                if selisih_pasir < 0:
                    selisih_pasir = 0
                if selisih_batu < 0:
                    selisih_batu = 0
                if selisih_air < 0:
                    selisih_air = 0
                print(f"Bangun gagal. Kurang {selisih_pasir} pasir, {selisih_batu} batu, dan {selisih_air} air.")
                for i in range(jumlah_pembangun):
                    variables.lst_avail_id[lst_penampung_candiID[i]] = lst_penampung_candiID[i]

