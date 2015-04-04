import os

def rename_files ():
    # (1) get file names from a folder
    file_list = os.listdir("prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    # print(saved_path+"/prank")
    os.chdir(saved_path+"/prank")

    # # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()