import os


def ShowCurrentDirectoyFiles():


    fileNameList = os.listdir()

    for name in fileNameList:
        print(name)
