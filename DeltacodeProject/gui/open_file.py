from DeltacodeProject import DayEncoding
from customtkinter import *
from tkinter import filedialog
from os import listdir, getcwd
from threading import Thread
from threading import Event as Tevent
from time import sleep

# TODO: upgrade this gui


class PasswordManager:
    def __init__(self):
        self.app = CTk()
        self.app.protocol("WM_DELETE_WINDOW", self.close)
        self.app.title("Password Manager")
        self.app.geometry("740x740")
        self.output_file = ''
        self.filename = 'ex.txt'
        self.file = ''
        self.newfile = ''
        self.status = StringVar()
        self.event = Tevent()

        self.top = CTkFrame(self.app, fg_color="transparent")
        CTkButton(self.top, text="Reload", command=self.decode_file).grid(row=0, column=0, padx=10)
        CTkButton(self.top, text="Choisir un fichier à décoder", command=self.pick_file).grid(row=0, column=1, padx=30)
        CTkButton(self.top, text="Save", command=self.save).grid(row=0, column=2, padx=10)
        self.app.bind_all("<Control-s>", self.save)
        self.top.pack()
        self.options = CTkFrame(self.app, fg_color="transparent")
        CTkLabel(self.options, text="Password").grid(row=0, column=0, padx=3, pady=10)
        CTkLabel(self.options, text="Shift").grid(row=0, column=1, padx=3, pady=10)
        self.password = CTkEntry(self.options, width=150)
        self.shift = CTkEntry(self.options, width=50)
        self.password.grid(row=1, column=0, padx=3, pady=10)
        self.shift.grid(row=1, column=1, padx=3, pady=10)
        self.options.pack()

        self.file_label = CTkLabel(self.app, text=f"Fichier actuel : {self.filename}",
                                   font=CTkFont(family="Arial", size=13, weight="bold", underline=True))
        self.file_label.pack(pady=4, padx=4)
        CTkLabel(self.app, textvariable=self.status).pack()

        self.result = CTkFrame(self.app)
        self.output_text = CTkTextbox(self.result, bg_color="#ababab", font=("Arial", 12, "bold"))
        self.output_text.bind('<Key>', self.update)
        self.output_text.pack()
        self.result.pack()

        Thread(target=self.tex_size).start()
        self.decode_file()

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

