from length import *
from Bacamatriks import *
import variables


def login():
    if variables.login_status == False:
        variables.username = input("Username: ")
        variables.password = input("Password: ")

        for i in range(length(variables.users)):
            if Bacamatriks(1, i+1, variables.users) == variables.username:
                flag_username = True
                variables.index_username = i
                break
            else:
                flag_username = False
        
        for i in range(length(variables.users)):
            if Bacamatriks(2, i+1, variables.users) == variables.password:
                flag_password = True
                variables.index_password = i
                break
            else:
                flag_password = False
        
        if flag_username == True:
            if flag_password == True and variables.index_username == variables.index_password:
                variables.role = Bacamatriks(3, i+1, variables.users)
                print("Selamat datang, " + variables.username + "!")
                print(
                    "Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                variables.login_status = True
            else:
                print("Password salah!")
                variables.login_status = False
        else:
            print("Username tidak terdaftar!")
            variables.login_status = False
    else:
        print("Kamu sudah login!")
