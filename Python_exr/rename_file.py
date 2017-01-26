import os

#function to get list of files in a folder
def rename_files():
    file_list =os.listdir("C:\pyt\prank\prank")
    #print(file_list)
    saved_path=os.getcwd()
    print("current working directory is "+saved_path)
    os.chdir(r"C:\pyt\prank\prank")

    for file_name in file_list:
        print("old name  -"+file_name)
        print("new name  -"+file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
