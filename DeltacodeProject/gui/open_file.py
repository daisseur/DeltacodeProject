from DeltacodeProject import DayEncoding
from tkinter import *
from tkinter import filedialog
from os import listdir, getcwd
from threading import Thread
from threading import Event as Tevent
from time import sleep

# TODO: upgrade this gui


class PasswordManager:
    def __init__(self):
        self.app = Tk()
        self.app.protocol("WM_DELETE_WINDOW", self.close)
        self.app.title("Password Manager")
        self.app.geometry("740x740")
        self.output_file = ''
        self.filename = 'ex.txt'
        self.file = ''
        self.newfile = ''
        self.status = StringVar()
        self.event = Tevent()

        self.top = Frame(self.app)
        Button(self.top, text="Reload", command=self.decode_file).grid(row=0, column=0, ipadx=10)
        Button(self.top, text="Choisir un fichier à décoder", command=self.pick_file).grid(row=0, column=1, ipadx=30)
        Button(self.top, text="Save", command=self.save).grid(row=0, column=2, ipadx=10)
        self.app.bind_all("<Control-s>", self.save)
        self.top.pack()
        self.options = Frame(self.app)
        Label(self.options, text="Password").grid(row=0, column=0), Label(self.options, text="Shift").grid(row=0, column=1)
        self.password = Entry(self.options, width=50)
        self.shift = Entry(self.options, width=50)
        self.password.grid(row=1, column=0), self.shift.grid(row=1, column=1)
        self.options.pack()

        self.file_label = Label(text=f"Fichier actuel : {self.filename}")
        self.file_label.pack()
        Label(textvariable=self.status).pack()

        self.result = Frame(self.app)
        self.output_text = Text(self.result)
        self.output_text.bind('<Key>', self.update)
        self.output_text.configure(bg="#ababab", font=("Arial", 12, "bold"))
        self.output_text.pack()
        self.result.pack()

        Thread(target=self.tex_size).start()

    def close(self):
        self.event.set()
        self.app.quit()


    def tex_size(self):
        while True:
            self.output_text.configure(height=self.app.winfo_height(), width=self.app.winfo_width())
            sleep(1)
            if self.event.is_set():
                break

    def save(self, key=None):
        shift = self.verif_shift()
        file = DayEncoding(
            password=self.password.get(),
            string=self.output_text.get(1.0, END),
            shift=shift if shift else 0
        )
        open(self.filename, 'w', encoding='UTF-8').write(file.encode().string)
        self.status.set("saved")
        print("saved")

    def update(self, key):
        print("modified")
        self.newfile = self.output_text.get(1.0, END)
        self.status.set("modified")

    def read_file(self):
        self.file = open(self.filename, encoding='UTF-8').read()
        return self.file

    def verif_shift(self):
        try:
            shift = int(self.shift.get())
        except:
            return False
        return shift

    def decode_file(self):
        if self.filename:
            self.output_text.delete(1.0, END)
            self.status.set("")
            shift = self.verif_shift()
            file = DayEncoding(
                password=self.password.get(),
                string=self.read_file(),
                shift=shift if shift else 0
            )
            self.output_file = file.decode().string
            self.output_text.insert(INSERT, self.output_file)
            print("loaded")

    def pick_file(self):
        self.filename = filedialog.askopenfilename(initialdir=getcwd())
        self.file_label.config(text=f"Fichier actuel : {self.filename}")
        print("New file on", self.filename)
        self.decode_file()

    def show(self):
        self.app.mainloop()


if __name__ == "__main__":
    PasswordManager().show()

