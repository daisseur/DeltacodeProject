# TEAM DELTA / DELTA's TEAM
# By daisseur, discord : daisseur#7755

import inspect
import os
import string as s
import time
import sys
import shutil
from scripts import *
from ALL_ENCODING_2 import ROT as rotation
from ALL_ENCODING_2 import DayEncoding as DD
from ALL_ENCODING_2 import Cesar as ceasar

class Deltacode:
    """                                                 \\\ DELTA-ENCODING //
    To decode or encode a text/string with rotation using all the existing characters.
    Pour encoder ou décoder un texte ou une chaîne de caractères avec une rotation utilisant tous les caractères existants.

    Example\\Exemple :

    """

    # Ce serait bien de faire que pour chaque encodage on mette une classe comme ça : Deltacode(DayEncoding, Cesar) et
    # Deltacode s'adapterait.
    def __init__(self, *args):
        print(args[0])
        self.encodings = {}
        self.class_encodings = []
        for class_ in args[0]:
            print(class_)
            self.class_encodings.append(class_)
            self.encodings[class_.__name__] = {}
            new_dict = self.encodings[class_.__name__]
            new_dict["name"] = class_.__name__
            new_dict["functions"] = [func for func in dir(class_) if not func.startswith("__") and not func.endswith("__")]
            new_dict["__init__"] = class_.__init__.__code__.co_varnames[1:]
            if "description" in new_dict["__init__"]:
                new_dict["description"] = new_dict["__init__"]["description"]
            if "abbr" in new_dict["__init__"]:
                new_dict["description"] = new_dict["__init__"]["abbr"]
        print(self.encodings)
        print(self.class_encodings)
        for class_ in self.class_encodings:
            self.create_class_func(class_.__name__, class_)
        time.sleep(1)
        self.use_copy = True
        self.valid_char = s.printable
        self.status = "in __init__"
        self.center_y = int(
            chercher(str(shutil.get_terminal_size()), "columns=", ",", replace=True))
        self.banner = ' \\\ DELTA // '
        self.password_running = None
        self.text_running = None
        self.shift_running = 0
        self.coding_running = None
        if os.path.exists("historique.txt"):
            with open("historique.txt", 'r') as f:
                self.history = f.read()
        else:
            self.history = "\n"
        if os.name == "posix":
            self.OS = "LINUX"
        elif os.name == "nt":
            self.OS = "WINDOWS"

    def create_class_func(self, name, class_):
        globals()[name] = type("name", (class_,), {})

    def copy(self, txt):
        if self.use_copy is True:
            if os.name == "posix":
                os.system(f"echo '{str(txt)}' | xclip")
            else:
                from clipboard import copy
                copy(txt)
        else:
            return

    def clear(self, effect='italic', color='blue'):
        if self.OS == "LINUX":
            os.system("clear")
        elif self.OS == "WINDOWS":
            os.system("cls")
        print_color(self.banner.center(self.center_y, ' '), color='green', effect='bold')
        print_color(f"OS: {self.OS}".center(self.center_y, ' '), color='violet', effect='bold')
        print_color(self.history, color=color, effect=effect)

    def curly(self, string: str):
        return '{' + string + '}'

    def add_history(self, Password, Text, coding, decode_encode: str, shift="None"):
        if shift != "None":
            shift_insert = self.curly(f"Shift = {shift}") + "\n"
        else:
            shift_insert = ''

        if decode_encode == "encode":
            self.history += f"== ENCODE - {self.coding_running} ==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
        elif decode_encode == "decode":
            self.history += f"== DECODE - {self.coding_running} ==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"

    def input_coding(self, coding_function, decode_encode: str, shift=False, password=True, warning="None",
                     from_file=False, hexa=False):

        def ifhexa(opt):
            if hexa:
                opt.hexa = hexa
                return opt
            else:
                return opt

        def input_return():
            if shift:
                if from_file:
                    return [Text, ifhexa(coding_function(password=Password, string=coding.string, shift=Shift)), filename]
                return [Text, ifhexa(coding_function(password=Password, string=coding.string, shift=Shift))]
            elif password is False:
                if from_file:
                    return [Text, ifhexa(coding_function(rot=Password, string=coding.string, shift=Shift)), filename]
                return [Text, ifhexa(coding_function(rot=Password, string=coding.string, shift=Shift))]
            else:
                if from_file:
                    return [Text, ifhexa(coding_function(password=Password, string=coding.string)), filename]
                return [Text, ifhexa(coding_function(password=Password, string=coding.string))]

        self.clear()
        if warning is not None:
            print_color(warning, color='yellow', effect='underline')
        self.copy(str(self.password_running))
        if hexa:
            hexa = input("Voulez-vous utiliser l'encodage hexadecimal ? ")
            if hexa.lower() == "oui":
                hexa = True
            else:
                hexa = False
        if password:
            Password = input('Mot de passe : ')
        else:
            Password = input("Nombre de rotation à effectuer : ")
            while True:
                Password = input("Nombre de rotation à effectuer : ")
                try:
                    int(Password)
                except:
                    pass
                else:
                    break
        self.copy(str(self.text_running))
        if from_file:
            while True:
                filename = input('Nom du fichier : ')
                if os.path.exists(filename):
                    Text = open(filename, 'r', encoding='UTF-8').read()
                    break
        else:
            file = input(f"Voulez-vous {decode_encode}r à partir d'un fichier ? ")
            if file.lower() == "oui":
                from_file = True
                while True:
                    filename = input('Nom du fichier : ')
                    if os.path.exists(filename):
                        with open(filename, 'r', encoding='UTF-8') as f:
                            Text = f.read()
                        break
            else:
                from_file = False
                Text = input('Texte : ')
        if shift:
            Shift = input("Utiliser le shift ? ")
            if Shift.lower() == "oui":
                while True:
                    self.copy(str(self.shift_running))
                    Shift = input('Shift : ')
                    try:
                        Shift = int(Shift)
                    except:
                        print_color("/!\ Veuillez rentrer un nombre", color="red", effect="bold")
                    else:
                        break
                if self.status == 'encode':
                    coding = coding_function(Password, Text, Shift, hexa=hexa).encode()
                else:
                    coding = coding_function(Password, Text, Shift, hexa=hexa).decode()
                print_color(coding, color='blue')
                self.add_history(Password, Text, coding, decode_encode, shift=str(Shift))
                self.text_running = coding
                self.password_running = Password
                self.shift_running = Shift
                return input_return()
            else:
                Shift = 0
                if self.status == 'encode':
                    coding = coding_function(Password, Text, Shift, hexa=hexa).encode()
                else:
                    coding = coding_function(Password, Text, Shift, hexa=hexa).decode()
                self.add_history(Password, Text, coding, decode_encode, shift=str(Shift))
                self.shift_running = Shift
                return input_return()
        else:
            if decode_encode == "encode":
                coding = coding_function(Password, Text).encode()
            else:
                coding = coding_function(Password, Text).decode()
            print_color(coding, color='blue')
            self.add_history(Password, Text, coding, decode_encode)
        self.text_running = coding
        self.password_running = Password
        return input_return()

    def create_menu(self, tab: int, lst: list):
        menu_tab = "\t" * tab + "│"
        end = "│"
        menu = """"""
        len_max = 0
        number = 0
        before = 4
        for i in lst:
            if len(i) > len_max:
                len_max = len(i) + 4
        calcul = tab * 6 + 2 * len(end) + len_max + len(str(len(lst))) + 3
        # print(calcul)
        if calcul > self.center_y or (calcul + tab * 6) > self.center_y:
            menu_tab = (self.center_y - calcul) * " " + end
            new_calcul = len(menu_tab) + 2 * len(end) + len_max + len(str(len(lst))) + 3
            if new_calcul > self.center_y:
                menu_tab = end
            if new_calcul - 2 * len(end) > self.center_y:
                end = ''
                menu_tab = ''
            # print("RESPONSIVE", self.center_y, "\n" + "-" * self.center_y, calcul)
            # menu_tab = menu_tab.replace("      ", "\t")
            menu_entry = menu_tab[:-1] + " "
        else:
            menu_entry = (tab * "\t")[:-1] + 4 * ' '
        menu += f"{menu_tab}{'—' * len_max}{end}\n"
        for i in lst:
            if i == '':
                end_tab = (len_max - len(i)) * ' ' + end
                menu += f"{menu_tab}{end_tab}\n"
            elif i == ' ':
                end_tab = (len_max - len(i) - 2) * ' ' + end
                menu += f"{menu_tab}[ ]{end_tab}\n"
                number += 1
            else:
                number += 1
                before = len(str(number)) + 3
                end_tab = (len_max - len(i) - before) * ' ' + end
                menu += f"{menu_tab}[{number}] {i}{end_tab}\n"
        menu += f"{menu_tab}{'—' * len_max}{end}\n\n{menu_entry}>> "
        return menu


class main(Deltacode):

    def __init__(self, *args, copy=None):
        super().__init__(args)
        sys.tracebacklimit = 0

        if copy is None:
            self.use_copy = input(
                "Voulez-vous utiliser la fonction copier ? Elle vous aidera à copier vos mots de passe, et texte déjà encodés directement quand vous en aurez besoin.\n")
            if self.use_copy.lower() == "oui":
                self.use_copy = True
            else:
                self.use_copy = False
        elif copy:
            self.use_copy = True
        elif copy is False:
            self.use_copy = False

    def choice_encoding(self, return_choice=False):
        """
        Choice to encoding
        Choix pour encoder
        """
        self.banner += "- ENCODE"
        self.clear()
        self.status = "encode"
        choice_encode = input(self.create_menu(2, list(self.encodings.keys())))
        if return_choice:
            return choice_encode
        for encoding in self.class_encodings:
            name = encoding.__name__
            index = str(self.class_encodings.index(encoding) + 1)
            print(index)
            if choice_encode == index:
                self.coding_running = name
                print(self.coding_running)
                print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                print("password", password)
                print("shift", shift)
                print("hexa", hexa)
                print("warning", warning)
                self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa, warning=warning)
                break
            elif choice_encode == "4":
                print("Développement en cours...")
        if choice_encode not in [str(i) for i in range(1, len(self.class_encodings))]:
            print_color('Invalid choice', color='red', effect='bold')

    def choice_decoding(self, return_choice=False):
        """
        Choice to decoding
        Choix pour decoder
        """
        self.banner += "- DECODE"
        self.clear()
        self.status = "decode"
        choice_decode = input(self.create_menu(2, list(self.encodings.keys())))
        if return_choice:
            return choice_decode
        for encoding in self.class_encodings:
            name = encoding.__name__
            index = str(self.class_encodings.index(encoding) + 1)
            print(index)
            if choice_decode == index:
                self.coding_running = name
                print(self.coding_running)
                print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                warning = encoding.warning if "hexa" in self.encodings[name]["__init__"] else None
                print("password", password)
                print("shift", shift)
                print("hexa", hexa)
                print("warning", warning)
                self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa,
                                  warning=warning)
                break
            elif choice_decode == "4":
                print("Développement en cours...")
        if choice_decode not in [str(i) for i in range(1, len(self.class_encodings))]:
            print_color('Invalid choice', color='red', effect='bold')

    def encoding_decoding(self, choice_code="0", return_choice=False):
        """
        To encode and decode with the encoding that has been chosen
        Pour encoder et décoder avec l'encodage qui a été choisi
        """
        self.banner += "- ENCODE & DECODE"
        self.clear()
        self.status = "encode"
        if choice_code == "0":
            choice_code = input(self.create_menu(2, list(self.encodings.keys())))
        if return_choice:
            return choice_code
        for encoding in self.class_encodings:
            name = encoding.__name__
            index = str(self.class_encodings.index(encoding) + 1)
            print(index)
            if choice_code == index:
                self.coding_running = name
                print(self.coding_running)
                print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                print("password", password)
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                print("shift", shift)
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                print("hexa", hexa)
                warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                print("warning", warning)
                self.status = "encode"
                info = self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa,
                                  warning=warning).copy()
                self.status = "decode"
                coding = info[1].decode()
                print_color(coding, color="blue")
                self.add_history(Password=info[1].password, Text=info[1], coding=coding, decode_encode=self.status, shift=coding.shift if shift else "None")
                break
            elif choice_code == "4":
                print("Développement en cours...")
        if choice_code not in [str(i) for i in range(1, len(self.class_encodings) + 1)]:
            print_color('Invalid choice', color='red', effect='bold')

    def encode_decode_file(self, return_choice=False):
        self.clear()

        def replace_file(filename: str, update: str):
            with open(filename, 'w') as file:
                update = str(update)
                file.write(update)

        while True:
            encode_decode = input("Encoder ou decoder votre fichier ? ")
            if encode_decode.lower() == "encoder" or encode_decode.lower() == "decoder":
                encode_decode = encode_decode[:-1]
                self.banner += f"- {encode_decode.upper()}"
                self.clear()
                self.status = encode_decode
                choice_code = input(self.create_menu(2, list(self.encodings.keys())))
                if return_choice:
                    return choice_code
                for encoding in self.class_encodings:
                    name = encoding.__name__
                    index = str(self.class_encodings.index(encoding) + 1)
                    print(index)
                    if choice_code == index:
                        self.coding_running = name
                        print(self.coding_running)
                        print(self.encodings[name]["__init__"])
                        password = True if "password" in self.encodings[name]["__init__"] else False
                        print("password", password)
                        shift = True if "shift" in self.encodings[name]["__init__"] else False
                        print("shift", shift)
                        hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                        print("hexa", hexa)
                        warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                        print("warning", warning)
                        self.status = "encode"
                        info = self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa,
                                          warning=warning, from_file=True).copy()
                        update = info[1]
                        filename = info[-1]
                        replace_file(filename, update)

                        break
                    elif choice_code == "4":
                        print("Développement en cours...")
                if choice_code not in [str(i) for i in range(1, len(self.class_encodings) + 1)]:
                    print_color('Invalid choice', color='red', effect='bold')
            else:
                print_color('Invalid choice', color='red', effect='bold')
                time.sleep(0.5)

    def clear_history(self):
        """
        To clear the program history
        Pour effacer l'historique du programme
        """
        self.clear(effect='strike')
        time.sleep(0.5)
        self.history = "\nL'historique actuelle a été vidé"
        self.clear()
        time.sleep(0.5)
        self.history = "\n"

    def save_history(self):
        """
        To save the program history
        Pour sauvegarder l'historique du programme
        """
        with open("historique.txt", "a", encoding='utf-8') as f:
            f.write(self.history)
        print_color("L'historique a été sauvegardé", effect="italic")
        time.sleep(0.5)
        self.clear()

    def del_save(self):
        self.clear(effect='strike', color='red')
        time.sleep(0.5)
        self.history = "\n"
        try:
            os.remove("historique.txt")
        except:
            with open('historique.txt', 'w') as f:
                f.write("deleted")
            self.save_history()
        self.clear()
        print_color("La sauvegarde de l'historique a été supprimé", effect="italic")

    def restart(self):
        try:
            os.execl(__file__, *sys.argv)
            exit(0)
        except:
            print_color("Cette fonction n'est actuellement pas fonctionnel sur votre appareil", color="red",
                        effect="bold")
            time.sleep(1.5)

    def test(self):
        Shift = 10
        Password = "DELTA's TEAM BY DAISSEUR"
        Text = "Je ne sais pas pourquoi le mot de passe est en anglais mais bon. Alors ça marche ?"
        self.status = "encode"
        encoding = DayEncoding(password=Password, string=Text, shift=Shift, debug=True).encode()
        print_color(encoding, color='blue')
        self.add_history(Password, Text, encoding, decode_encode="encode", shift=str(Shift))
        self.status = "decode"
        decoding = DayEncoding(Password, encoding, Shift, hexa=True, debug=True, error_input=True).decode()
        print_color(decoding, color='blue')
        self.add_history(Password, encoding, decoding, decode_encode="decode", shift=str(Shift))

    def run(self):
        while True:
            self.banner = ' \\\ DELTA // '
            self.clear()
            choice = input(self.create_menu(2, ["Encoder",
                                                "Décoder",
                                                "Encoder et Décoder",
                                                "Encoder ou decoder un fichier",
                                                '',
                                                "Effacer l'historique actuel",
                                                "Sauvegarder l'historique",
                                                "Effacer la sauvegarde de l'historique",
                                                '',
                                                "Redémarrer le programme",
                                                '',
                                                " ",
                                                ]))
            if choice == '1':
                self.choice_encoding()
            elif choice == '2':
                self.choice_decoding()
            elif choice == "3":
                self.encoding_decoding()
            elif choice == "4":
                self.encode_decode_file()
            elif choice == "5":
                self.clear_history()
            elif choice == "6":
                self.save_history()
            elif choice == "7":
                self.del_save()
            elif choice == "8":
                self.restart()
            elif choice == "9":
                self.test()
            time.sleep(0.5)


if __name__ == '__main__' or "debug" in sys.argv:
    main(rotation, ceasar, DD, copy=True).run()
