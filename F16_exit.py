import F14_save
import variables

def exit():
    while variables.inputan_exit_valid == False:
        inputan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if inputan == "y" or input == "Y":
            F14_save.save()
            variables.inputan_exit_valid = True
        elif inputan == "n" or inputan == "N":
            variables.inputan_exit_valid = True