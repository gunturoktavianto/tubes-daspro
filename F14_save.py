import argparse

import os
from length import *
from Bacamatriks import *
import variables

def save():

    nama_folder = input("Masukkan nama folder: ")
    
    print("\nSaving...")
    
    path = f'SaveFolder/{nama_folder}'
    if not os.path.isdir(path):
        print(f"\nMembuat folder {nama_folder}...")
        os.mkdir(path)
    
    path_user   = os.path.join(path, "user.csv")
    path_candi  = os.path.join(path, "candi.csv")
    path_bahan  = os.path.join(path, "bahan_bangunan.csv")

    file_user = open(path_user, 'w')
    file_candi = open(path_candi, 'w')
    file_bahan= open(path_bahan, 'w')

    file_user.write('username;password;role\n')
    file_candi.write('id;pembuat;pasir;batu;air\n')
    file_bahan.write('nama;deskripsi;jumlah\n')
    
    for i in range(1, length(variables.users)):
        new_line = variables.users[i]
        file_user.write(new_line + '\n')
    
    
    file_bahan.write(f'pasir;descpasir;{variables.punya_pasir}\n')
    file_bahan.write(f'batu;descbatu;{variables.punya_batu}\n')
    file_bahan.write(f'air;descair;{variables.punya_air}\n')

    
    for i in range(1, length(variables.candi)):
        new_line = variables.candi[i]
        file_candi.write(new_line + '\n')
    
    print(f"\nBerhasil menyimpan data di folder {nama_folder}!")