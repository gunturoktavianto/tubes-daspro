import random

def kumpul():
    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)
    
    bahan[1][2] += pasir 
    bahan[2][2] += batu
    bahan[3][2] += air

    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
