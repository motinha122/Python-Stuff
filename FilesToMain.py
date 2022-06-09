import os
import shutil
import stat

directories = [] ; files = [] ; folderOrder = [] ; lists = [] ; blacklist = [] 
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

def listAllFolders(lists):
    directories.clear()
    for folder in lists:
        if os.path.isdir(folder) and folder != '.git' and folder not in blacklist:
            directories.append(folder)

def listAllFiles(lists):
    files.clear()
    for file in lists:
        if os.path.isfile(file):
            files.append(file)

def moveFiles(lists):
    for file in lists:
        if not os.path.exists(os.path.join(folderOrder[0],file)):
            shutil.move(os.path.join(folderOrder[-1],file),folderOrder[0])

def firstFolderMoveFiles():
    while len(directories) != 0:
        print(directories)
        os.chdir(directories[0])
        folderOrder.append(os.getcwd())
        lists = os.listdir(folderOrder[-1])
        listAllFolders(lists)

    listAllFiles(lists)
    blacklist.append(folderOrder[-1])

    if len(files) != 0:
        moveFiles(files)

def main():
    numberOfFolders(os.getcwd())
    listAllFolders(mainList)
    firstFolderMoveFiles()

if __name__ == "__main__":
    main()
