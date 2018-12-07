import tkinter as tk
from tkinter import filedialog as fd
import datetime
import os

from tkinter import messagebox as msb


class Application:
    fileName = datetime.datetime.today().strftime('%Y-%m-%d')
    directory = ""
    path = ""

    def __init__(self):
        self.window = tk.Tk()
        self.window.bind("<Button-1>", self.click_ppm_lpm)
        self.window.bind("<Button-3>", self.click_ppm_lpm)
        textInfo =  "Witaj, \n kliknij w to okno aby wybrać lokalizację zapisu plików: \n-plik data****-**-**.txt\n "
        self.displayInfo(textInfo)

        self.window.mainloop()

    def displayInfo(self, textInfo):
        text = tk.StringVar()
        label = tk.Label(self.window, textvariable=text, padx=100, pady=20)
        label.pack()
        text.set(textInfo)

    def click_ppm_lpm (self, event):

        self.save_file()

        msb.showinfo("Info", "Plik został utworzony, za chwile nastąpi jego edycja w notatniku")
        execute = "notepad.exe " + self.path
        os.system(execute)
        newTextInfo= " Zostały utworzone pliki:"
        self.displayInfo(newTextInfo)


    def save_file(self):

        self.directory = fd.askdirectory()  # wywołanie okna dialogowego do wskazania ścieżki do folderu docelowego
        if self.directory:
            msb.showinfo("Info", "Wybrano taki folder {folder} do zapisu plików.".format(folder=self.directory))
            filename = str(self.getDateToFileName())

        if filename:
            print (filename)
            with open(self.createFilePath(), "w", -1, "utf-8") as file:
                file.write(filename) #.get(1.0, tk.END)
                print ("zapisano plik")


    def getDateToFileName(self):
        self.fileName = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
        return self.fileName

    def createFilePath(self):
        path = os.path.join(self.directory, self.fileName + ".txt")
        self.path = path
        print (path)
        return path



apl = Application()
