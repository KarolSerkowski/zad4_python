import tkinter as tk
from tkinter import filedialog as fd
import datetime
import os

from tkinter import messagebox as msb


class Application:
    fileName = datetime.datetime.today().strftime('%Y-%m-%d')
    directory = ""
    path = ""
    mainFilePath = ""
    nameNewFile = ""

    def __init__(self):
        self.window = tk.Tk()
        self.window.bind("<Button-1>", self.click_ppm_lpm_controller)
        self.window.bind("<Button-3>", self.click_ppm_lpm_controller)
        textInfo =  "Witaj, \n kliknij w to okno aby wybrać lokalizację zapisu plików: \n-plik data****-**-**.txt\n "
        self.displayInfo(textInfo)

        self.window.mainloop()

    def displayInfo(self, textInfo):
        text = tk.StringVar()
        label = tk.Label(self.window, textvariable=text, padx=100, pady=20)
        label.pack()
        text.set(textInfo)

    def click_ppm_lpm_controller (self, event):

        self.save_file()

        msb.showinfo("Info", "Plik został utworzony, za chwile nastąpi jego edycja w notatniku")
        execute = "notepad.exe " + self.path
        os.system(execute)
        self.mainFilePath = self.path
        newTextInfo= " Zostały utworzone pliki:%s"%self.createNewFileAfterTestContentTxt(self.path)
        self.displayInfo(newTextInfo)


    def save_file(self):

        self.directory = fd.askdirectory()  # wskazanie ścieżki do folderu docelowego
        if self.directory:
            msb.showinfo("Info", "Wybrano taki folder {folder} do zapisu plików.".format(folder=self.directory))
            filename = str(self.getDateToFileName())

        if filename:
            print (filename)
            newFiles = open(self.createFilePath(filename), "a+")
            print("plik z data zapisany")
            newFiles.close()


    def getDateToFileName(self):
        self.fileName = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
        return self.fileName

    def createFilePath(self,toFilename):
        path = os.path.join(self.directory, toFilename + ".txt")
        self.path = path
        print (path)
        return path

    def createNewFileAfterTestContentTxt(self,path):
        numberOfLines = len(open(path).readlines())

        if numberOfLines == 0:
            self.nameNewFile = "puste"
            self.updateFileTxt(self.nameNewFile)
            return  self.nameNewFile
        elif numberOfLines == 1:
            self.nameNewFile = "krótkie"
            self.updateFileTxt(self.nameNewFile)
            return  self.nameNewFile
        elif numberOfLines <=10:
            self.nameNewFile = "średnie"
            self.updateFileTxt(self.nameNewFile)
            return  self.nameNewFile
        elif numberOfLines >10:
            self.nameNewFile = "długie"
            self.updateFileTxt(self.nameNewFile)
            return  self.nameNewFile

    def updateFileTxt(self,fileName):
        newFiles = open(self.createFilePath(fileName), "a+")
        newFiles.write(self.mainFilePath + '\n')
        print("plik dopisany")
        newFiles.close()




apl = Application()
