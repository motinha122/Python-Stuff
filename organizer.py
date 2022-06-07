from ctypes.wintypes import tagRECT
import os 
import shutil

print('''
  _____ _ _          ___                        _              
 |  ___(_) | ___    / _ \ _ __ __ _  __ _ _ __ (_)_______ _ __ 
 | |_  | | |/ _ \  | | | | '__/ _` |/ _` | '_ \| |_  / _ \ '__|
 |  _| | | |  __/  | |_| | | | (_| | (_| | | | | |/ /  __/ |   
 |_|   |_|_|\___|   \___/|_|  \__, |\__,_|_| |_|_/___\___|_|   
                              |___/                            
''')

mainDir = os.getcwd()

lists = os.listdir(mainDir)

directories = [] ; files = [] ; extensions = []

#{item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder,item))}

def listItems():
    directories.clear() ; files.clear() ; extensions.clear()
    for item in lists:
        if os.path.isfile(item):
            files.append(item)
        if os.path.isdir(item):
            directories.append(item)

listItems()

print(f'Directories found : {len(directories)} | Files found : {len(files)}\n')

def showItem(direc):
    for item in direc:
        print(f'{direc.index(item)}:{item}')

if len(directories) != 0:
    print("##### Folders ######\n")
    showItem(directories)
    folder = int(input("\nWhich folder : "))
    os.chdir(directories[folder])
    print(f'\n##### {directories[folder]} #####')
    extensions = {item.split('.')[-1] for item in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(),item))}
    for extension in extensions:
        if not os.path.exists(os.path.join(os.getcwd(),extension)):
            os.makedirs(os.path.join(os.getcwd(),extension))

    for item in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(),item)):
            file_extension = item.split('.')[-1]
            print(item.split('.'))
            shutil.move(os.path.join(os.getcwd(),item),os.path.join(os.getcwd(),file_extension))
    print(" ##### Files organized #####")
else:
    print("##### Theres no folder to organize #####")


#if len(files) != 0:
#    print("Files : ")
#    showItem(files)

input("\nPress Enter to continue...")

#print(f'{list.index(item)}:{item}')

#Devolve o Rafael por favor



