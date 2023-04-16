def hitungbaris(namafile) : #ngitung ada berapa baris di user.csv (header ga keitung)
    f = open(namafile)
    cc = f.readline()
    cc = f.readline()
    baris = 0
    while cc != '' :
        baris += 1
        cc = f.readline()
    f.close()
    return baris


