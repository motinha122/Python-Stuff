from msilib import _directories
from msilib.schema import Directory
import os 
import shutil 

print('''
  ______ _ _             _          __  __       _       
 |  ____(_) |           | |        |  \/  |     (_)      
 | |__   _| | ___  ___  | |_ ___   | \  / | __ _ _ _ __  
 |  __| | | |/ _ \/ __| | __/ _ \  | |\/| |/ _` | | '_ \ 
 | |    | | |  __/\__ \ | || (_) | | |  | | (_| | | | | |
 |_|    |_|_|\___||___/  \__\___/  |_|  |_|\__,_|_|_| |_| 
    ''')

mainFolder = os.listdir(os.getcwd())
folders = [] 


def setRootFoolder():
    for folder in mainFolder:
        if os.path.isdir(folder) and folder != '.git':
            folders.append(folder)
            print(f'{folders.index(folder)}:{folder}')
    if len(folders) != 0:
        mainDir = int(input("\nWhich folder : "))
        os.chdir(folders[mainDir])
        mainRoot = os.getcwd()
        for path,root,files in os.walk(os.getcwd()):
            for file in files:
                if not os.path.exists(os.path.join(mainRoot,file)):
                    shutil.move(os.path.join(path,file),mainRoot)
    else:
        return False

def main():
    if setRootFoolder() == False:
        print('Theres no directories')

if __name__ == "__main__":
    main()
