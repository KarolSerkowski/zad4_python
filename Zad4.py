import tkinter as tk
from tkinter import filedialog as fd
import datetime

from tkinter import messagebox as msb


class Application:
    filename = datetime.datetime.today().strftime('%Y-%m-%d')
    def __init__(self):
        self.window = tk.Tk()
        self.window.bind("<Button-1>", self.wnd_lbc)
        self.window.bind("<Button-3>", self.wnd_rbc)

        text = tk.StringVar()
        label = tk.Label(self.window, textvariable=text, padx=100, pady=20)
        label.pack()
        text.set(
            "Witaj, \n kliknij w to okno aby wybrać lokalizację zapisu plików: \n-plik data****-**-**.txt\n ")

        # "pliki:\n - puste.txt, "
        # " jeśli utworzony plik nie zawiera żadnych danych,\n-krótkie.txt, jeśli utworzony plik ma jedną linię,\n-średnie.txt, jeśli utworzony plik ma najwyżej 10 linii,\n"
        # "-długie.txt, jeśli utworzony plik ma więcej niż 10 linii
        self.window.mainloop()

    def wnd_lbc(self, event):

        self.save_file()

        msb.showinfo("Info", "Plik został utworzony, za chwile nastąi jego edycja w notatniku")

    def wnd_rbc(self, event):
        if msb.askokcancel("Pytanie",
                           "Czy ja śnię,\nczy kliknąłeś w okno me!"):  # okno dialogowe z przyciskami ok i cancel - zwraca prawdę, gdy ok jest wciśnięte
            msb.showinfo("Info", "A jednak to prawdą było!\nA jednak mi się nie przyśniło")
        else:
            msb.showinfo("Info", "Przykro mi się zrobiło,\nChyba mi się coś przyśniło")

    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")],
                                        defaultextension="*.txt", initialfile =str(self.getDateToFileName()))  # wywołanie okna dialogowego save file

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))
    def getDateToFileName(self):
        self.filename = datetime.datetime.today().strftime('%Y-%m-%d')
        return self.filename


apl = Application()
