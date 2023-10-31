from customtkinter import *
from tkinter import PhotoImage
from os.path import exists, dirname, join
from DeltacodeProject.encodings import *
from json import loads, dumps


class OptionsFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self._border_color = "gray"
        self._border_width = 2
        self.len = 0

    def create_option(self, lst, **kwargs):
        if "height" not in kwargs.keys():
            kwargs["height"] = 40
        listbox = CTkOptionMenu(self, values=lst, width=150, dropdown_font=("Arial", 16), **kwargs)
        if self.len == 0:
            listbox.grid(padx=10, pady=10)
        else:
            listbox.grid(padx=10, pady=5)
        self.len += 1
        return listbox

    def create_button(self, text, command=None, padx=10, pady=5, **kwargs):
        if command is None:
            button = CTkButton(self, text=text, **kwargs)
        else:
            button = CTkButton(self, text=text, command=command, **kwargs)
        button.grid(padx=padx, pady=pady)
        return button

    def create_switch(self, text, command=None, default=False, **kwargs):
        if "variable" not in kwargs.keys():
            var = BooleanVar(value=default)
        else:
            var = kwargs["variable"]
            del kwargs["variable"]
        switch = CTkSwitch(self, text=text, command=command, onvalue=True, offvalue=False,
                           variable=var, switch_width=55, switch_height=25, **kwargs)
        switch.grid(padx=10, pady=5)

    def options_pack(self):
        self.pack(side="left", anchor="n", fill=Y, pady=10)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("750x750")
        self.title("DeltacodeProject")
        # ico = PhotoImage(file=join(dirname(__file__), "Deltacode.ico"))
        # self.iconphoto(False, ico)
        self.minsize(440, 370)

        self.save = BooleanVar(value=False)
        self.started = False
        self.grid_number = 0
        self.var_password = StringVar()
        self.var_txt = StringVar()
        self.var_shift = StringVar()
        self.var_shift.set("0")
        self.var_result = StringVar()
        self.var_password.trace('w', self.change_label)
        self.var_txt.trace('w', self.change_label)
        self.var_shift.trace('w', self.change_label)

        for l_n in range(len(self.var_result.get())):
            if l_n in range(0, 10000, +21) != "\n" and l_n != 0:
                self.var_result.set(self.var_result.get()[:l_n] + "\n")
        self.options = OptionsFrame(self, width=300)
        self.mode_option = self.options.create_option(["Encoder", "Décoder"], fg_color="blue", height=70)
        self.hexa_option = self.options.create_option(["Avec hexa", "Sans hexa"])
        self.options.create_switch("Sauvegarde", button_color="#a32233", button_hover_color="red",
                                   progress_color="#226628", variable=self.save)
        self.options.create_button("Mesures", command=self.print_size, pady=140, fg_color="gray")
        self.options.options_pack()

        self.read_setup()

        self.create_label_entry('Mot de passe', trace=self.var_password)
        self.create_label_entry('Texte', trace=self.var_txt)
        self.create_label_entry('Shift', trace=self.var_shift)
        self.create_button("Encoder / Décoder", command=self.change_label)
        self.result_text = self.create_state_text(height=185, width=740)
        self.create_button("Copier", command=self.copy)

        self.started = True
        print("DeltacodeProject gui started !")

    def read_setup(self):
        if exists(".dltc"):
            try:
                setup = loads(open(".dltc", 'r', encoding='UTF-8').read())
                self.var_password.set(value=setup["password"])
                self.var_txt.set(value=setup["txt"])
                self.var_shift.set(value=setup["shift"])
                self.mode_option.set(setup["mod_option"])
                self.hexa_option.set(setup["hexa_option"])
            except Exception as error:
                print(f"DLTC ERROR: {error}")
                exit(0)
                # return

    def save_setup(self, *args):
        if self.save.get() is True:  # Seulement si l'option 'sauvegarde' a été activé
            print("Saving...", end='   ')
            setup = dict()
            setup["password"] = self.var_password.get()
            setup["txt"] = self.var_txt.get()
            setup["shift"] = self.var_shift.get()
            setup["hexa_option"] = self.hexa_option.get()
            setup["mod_option"] = self.mode_option.get()
            open(".dltc", 'w').write(dumps(setup))
            print("Saved !")
        else:
            return

    def create_state_text(self, **kwargs):
        text_widget = CTkTextbox(self, **kwargs)
        text_widget.pack(padx=5, pady=5)
        return text_widget

    def create_label_entry(self, text, example="", trace=None, master=None, **kwargs):
        if master is None:
            frame = CTkFrame(self, fg_color="transparent")
        else:
            frame = CTkFrame(master, fg_color="transparent")
        if trace is None:
            entry = CTkEntry(frame, **kwargs, width=150)
        else:
            entry = CTkEntry(frame, **kwargs, width=150, textvariable=trace)
        label = CTkLabel(frame, text=text,
                                       font=CTkFont(family="Arial", size=13, weight="bold"))
        """if temp_var is not None:
            label_info = CTkLabel(frame, textvariable=temp_var)
            label_info.grid(column=2, row=0, padx=30, pady=10)"""
        entry.insert(0, example)
        label.grid(column=0, row=0, pady=5, padx=5)
        entry.grid(column=1, row=0, pady=5, padx=5)

        frame.pack()
        return entry

    def create_label(self, text="optionnel", trace=None, effect="italic", **kwargs):
        frame_label = CTkFrame(self)
        font = CTkFont(family="Arial", size=11, slant=effect)
        if trace is None:
            label = CTkLabel(frame_label, text=text, font=font, **kwargs)
        else:
            label = CTkLabel(frame_label, text=text, font=font, textvariable=trace, **kwargs)

        label.grid()
        frame_label.pack()
        return label

    def create_button(self, text, command=None, **kwargs):
        if command is None:
            button = CTkButton(self, text=text, **kwargs)
        else:
            button = CTkButton(self, text=text, command=command, **kwargs)
        button.pack()
        return button

    def print_size(self):
        print(f"Height: {self.winfo_height()}     Width: {self.winfo_width()}")

    def change_label(self, *args):
        if self.started:
            password = self.var_password.get()
            string = self.var_txt.get()
            shift = self.var_shift.get()
            print(password, string, shift)
            result = ""
            hexa = True if self.hexa_option.get() == "Avec hexa" else False

            try:
                if self.mode_option.get() == "Encoder":
                    print("Selected mode: ENCODE")
                    if password != '' and string != '' and shift != '':
                        result = DayEncoding(password=password, string=string, shift=int(shift), hexa=hexa).encode()
                        print(f"Result: {result}")
                else:
                    print("Selected mode: DECODE")
                    if password != '' and string != '' and shift != '':
                        result = DayEncoding(password=password, string=string, shift=int(shift), hexa=hexa).decode()
                        print(f"Result: {result}")
            except Exception as error:
                print(f"ERROR: {error}")

            self.var_result.set(result)
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", result)
            self.result_text.configure(state="disabled")
            self.save_setup()

    def copy(self):
        self.var_result.set("Marche pas cheh")
        copy(self.var_result.get())


if __name__ == "__main__":
    set_appearance_mode("dark")
    app = App()
    app.mainloop()
