import os

def rename_files ():
    # (1) get file names from a folder
    # file_list = os.listdir("/Users/ralph/Downloads/prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)

    # # (2) for each file, rename filename
    # for file_name in file_list:
    #     os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()