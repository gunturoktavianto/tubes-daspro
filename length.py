def length(matriks) :
    mark = True
    count = 0
    i = 0
    while mark == True :
        if matriks[i] != '' :
            count += 1
            i += 1
        else :
            mark = False
    return count
