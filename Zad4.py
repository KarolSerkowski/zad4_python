import tkinter as tk
from tkinter import filedialog as fd
import datetime
import os

from tkinter import messagebox as msb


class Application:
    fileName = datetime.datetime.today().strftime('%Y-%m-%d')
    directory = ""
    path = ""
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

        newTextInfo= " Zostały utworzone pliki:%s"%self.createNewFileAfterTestContentTxt(self.path)
        self.displayInfo(newTextInfo)


    def save_file(self):

        self.directory = fd.askdirectory()  # wywołanie okna dialogowego do wskazania ścieżki do folderu docelowego
        if self.directory:
            msb.showinfo("Info", "Wybrano taki folder {folder} do zapisu plików.".format(folder=self.directory))
            filename = str(self.getDateToFileName())

        if filename:
            print (filename)
            with open(self.createFilePath(self.fileName), "w", -1, "utf-8") as file:
                file.write(filename) #.get(1.0, tk.END)
                print ("zapisano plik")


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
            with open(self.createFilePath(self.nameNewFile), "w", -1, "utf-8") as file:
                file.write(self.nameNewFile)

            return  self.nameNewFile
        elif numberOfLines == 1:
            self.nameNewFile = "krótkie"
            with open(self.createFilePath(self.nameNewFile), "w", -1, "utf-8") as file:
                file.write(self.nameNewFile)
            return  self.nameNewFile
        elif numberOfLines <=10:
            self.nameNewFile = "średnie"
            with open(self.createFilePath(self.nameNewFile), "w", -1, "utf-8") as file:
                file.write(self.nameNewFile)
            return  self.nameNewFile
        elif numberOfLines >10:
            self.nameNewFile = "długie"
            with open(self.createFilePath(self.nameNewFile), "w", -1, "utf-8") as file:
                file.write(self.nameNewFile)
            return  self.nameNewFile




apl = Application()
