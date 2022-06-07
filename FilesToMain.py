import os
import shutil

directories = [] ; files = [] ; folderOrder = [] ; lists = []
rootFolder = os.getcwd()
mainList = os.listdir(rootFolder)

print('''
  ______ _ _             _          __  __       _       
 |  ____(_) |           | |        |  \/  |     (_)      
 | |__   _| | ___  ___  | |_ ___   | \  / | __ _ _ _ __  
 |  __| | | |/ _ \/ __| | __/ _ \  | |\/| |/ _` | | '_ \ 
 | |    | | |  __/\__ \ | || (_) | | |  | | (_| | | | | |
 |_|    |_|_|\___||___/  \__\___/  |_|  |_|\__,_|_|_| |_| 
    ''')

def listFolders(lists):
    directories.clear()
    for item in lists:
        if os.path.isdir(item) and item != '.git':
            directories.append(item)
    print(directories)

def listFiles(lists):
    files.clear()
    for item in lists:
        if os.path.isfile(item):
            files.append(item)
    print(files)

def firstFolder():
    while len(directories) != 0:
        print(directories)
        print(directories[0])
        os.chdir(directories[0])
        folderOrder.append(os.getcwd())
        print(folderOrder[-1])
        lists = os.listdir(folderOrder[-1])
        listFolders(lists)
        input()
    listFiles(lists)

def main():
    listFolders(mainList)
    firstFolder()

if __name__ == "__main__":
    main()
