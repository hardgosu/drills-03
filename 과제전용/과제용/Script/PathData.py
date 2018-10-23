import os

class InitializeData:

    Sibal = "ㅁㄴㅇ"


    currentFolder = 'script'

    currentPath = os.getcwd()
    masterPath = os.getcwd()[0: os.getcwd().__len__() - currentFolder.__len__()]
    spriteSheetPath = masterPath + 'spriteSheet'

