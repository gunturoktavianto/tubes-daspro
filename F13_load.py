import argparse, os
from matriks import matriks
import variables
from length import *
from Bacamatriks import *
parser = argparse.ArgumentParser()
parser.add_argument("path", type = str, nargs='?', const='')
args = parser.parse_args()

if not args.path:
    path = 'SaveFolder/template'
    matriks(path)
elif os.path.exists(f"SaveFolder/{args.path}"):
    print("Loading...")
    print("Selamat datang kembali!")
    path = f"SaveFolder/{args.path}"
    matriks(path)
    for i in range(100):
        for j in range(1, length(variables.candi)):
            if i == int(Bacamatriks(1, j, variables.candi)):
                variables.lst_avail_id[i] = ''
else:
    print(f"Folder \"{args.path}\" tidak ditemukan.")
    exit()