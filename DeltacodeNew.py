# TEAM DELTA / DELTA's TEAM
# By daisseur, discord : daisseur#7755
import os
import shutil
import signal
import subprocess
import sys
import string as s
from time import sleep
from DeltacodeProject.scripts import *
from DeltacodeProject import *
from DeltacodeProject import __version__


class Deltacode:
    """                                                 \\\ DELTA-ENCODING //
    To decode or encode a text/string with rotation using all the existing characters.
    Pour encoder ou décoder un texte ou une chaîne de caractères avec une rotation utilisant tous les caractères existants.

    """

    def __init__(self, *args):
        # print(args[0])
        self.encodings = {}
        self.class_encodings = []
        for class_ in args[0]:
            # print(class_)
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
        # print(self.encodings)
        # print(self.class_encodings)
        for class_ in self.class_encodings:
            self.create_class_func(class_.__name__, class_)
        self.use_copy = True
        self.valid_char = s.printable
        self.status = "in __init__"
        self.center_y = int(
            find(str(shutil.get_terminal_size()), "columns=", ",", replace=True))
        self.banner = f' \\\ DELTACODE // '
        self.password_running = None
        self.text_running = None
        self.shift_running = 0
        self.coding_running = None
        self.filename = ''
        self.hexa = True
        if os.path.exists("historique.txt"):
            with open("historique.txt", 'r', encoding='UTF-8') as f:
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
        if txt not in ["None", None, False, True, '']:
            if self.use_copy is True:
                copy(txt)

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

    def read_file(self, filename, byte=False):
        return bytearray(open(filename, 'rb').read()) if byte else open(filename, 'r').read()

    def write_file(self, filename, data, byte=False):
        if byte and isinstance(data, bytearray):
            open(filename, 'wb').write(data)
        elif byte:
            data = bytearray(ord(i) for i in data)
            open(filename, 'wb').write(data)
        else:
            open(filename, 'w').write(data)

    def add_history(self, Password, Text, coding, decode_encode: str, shift="None"):
        if shift != "None":
            shift_insert = self.curly(f"Shift = {shift}") + "\n"
        else:
            shift_insert = ''
        if isinstance(Text, bytearray):
            Text = f"Old bytes of {self.filename}"
            coding = f"New bytes of {self.filename}"

        if decode_encode == "encode":
            self.history += f"== ENCODE - {self.coding_running} ==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
        elif decode_encode == "decode":
            self.history += f"== DECODE - {self.coding_running} ==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"

    def byte_or_text(self, filename):
        if get_file_ex(filename) in bytes_ext:
            return bytearray(open(filename, 'rb').read())
        else:
            return open(filename, 'r').read()


    def input_coding(self, coding_class, decode_encode: str, shift=False, password=True, warning="None",
                     from_file=False, hexa=False, byte=False):
        self.status = decode_encode
        self.clear()
        if hexa:
            self.hexa = input("Voulez-vous utiliser l'encodage hexadecimal ? ")
            if self.hexa.lower() in ["o", "y", "yes", "oui"]:
                self.hexa = True
            else:
                self.hexa = False

        def ifif(opt):
            if password:
                opt = opt(password=Password)
            else:
                opt = opt(rot=Password)
            if hexa:
                opt.hexa = self.hexa
            if shift:
                opt.shift = Shift
            if byte:
                opt.byte_array = coding.byte_array
                opt.string = coding.string
            return opt

        def coding_option():
            print(hexa)
            kwargs = {}
            if hexa:
                kwargs["hexa"] = self.hexa
            if shift:
                kwargs["shift"] = Shift
            if password:
                kwargs["password"] = Password
            else:
                kwargs["rot"] = Password
            print(byte, isinstance(Text, bytearray))
            if byte:
                if self.status == "encode":
                    coding = coding_class(**kwargs).encode_byte(Text)
                else:
                    coding = coding_class(**kwargs).decode_byte(Text)
                self.add_history(Password, Text, coding.byte_array, decode_encode, shift=str(Shift))
            else:
                if self.status == "encode":
                    coding = coding_class(**kwargs).encode(Text)
                else:
                    coding = coding_class(**kwargs).decode(Text)
                self.add_history(Password, Text, coding.string, decode_encode, shift=str(Shift))
            return coding

        def input_return():
            if shift:
                if from_file:
                    return [Text, coding, self.filename]
                return [Text, coding]
            elif password is False:
                if from_file:
                    return [Text, coding, self.filename]
                return [Text, coding]
            else:
                if from_file:
                    return [Text, coding, self.filename]
                return [Text, coding]

        def get_rot():
            while True:
                rot = input("Nombre de rotation à effectuer : ")
                try:
                    int(rot)
                except:
                    pass
                else:
                    break
            return rot

        if warning is not None:
            print_color(warning, color='yellow', effect='underline')
        self.copy(str(self.password_running))
        if password:
            Password = input('Mot de passe : ')
        else:
            Password = get_rot()
        if from_file:
            while True:
                self.copy(self.filename)
                self.filename = input('Nom du fichier : ')
                if os.path.exists(self.filename):
                    Text = self.byte_or_text(self.filename)
                    break
        else:
            file = input(f"Voulez-vous {decode_encode}r à partir d'un fichier ? ")
            if file.lower() == "oui":
                from_file = True
                while True:
                    self.copy(self.filename)
                    self.filename = input('Nom du fichier : ')
                    if os.path.exists(self.filename):
                        Text = self.byte_or_text(self.filename)
                        break
                return Text
            else:
                self.copy(str(self.text_running))
                from_file = False
                Text = input('Texte : ')
                self.text_running = Text
        if from_file:
            if get_file_ex(self.filename) in bytes_ext and byte is False:
                return [False]
            byte = True if isinstance(Text, bytearray) else False
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
                coding = coding_option()
                print_color(coding.string, color='blue')
                self.text_running = coding.string
                self.password_running = Password
                self.shift_running = Shift
                return input_return()
            else:
                Shift = 0
                coding = coding_option()
                self.shift_running = Shift
                return input_return()
        else:
            Shift = "None"
            coding = coding_option()
            print_color(coding.string, color='blue')
        self.text_running = coding.string
        self.password_running = Password
        return input_return()

    def create_menu(self, tab: int, lst: list):
        menu_tab = "\t" * tab + "│"
        end = "│"
        menu = """"""
        len_max = 0
        number = 0
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
        # sys.tracebacklimit = 0
        signal.signal(signal.SIGINT, signal_handler)

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
            # print(index)
            if choice_encode == index:
                self.coding_running = name
                # print(self.coding_running)
                # print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                # print("password", password)
                # print("shift", shift)
                # print("hexa", hexa)
                # print("warning", warning)
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
            # print(index)
            if choice_decode == index:
                self.coding_running = name
                # print(self.coding_running)
                # print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False

                warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                # print("password", password)
                # print("shift", shift)
                # print("hexa", hexa)
                # print("warning", warning)
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
            # print(index)
            if choice_code == index:
                self.coding_running = name
                # print(self.coding_running)
                # print(self.encodings[name]["__init__"])
                password = True if "password" in self.encodings[name]["__init__"] else False
                # print("password", password)
                shift = True if "shift" in self.encodings[name]["__init__"] else False
                # print("shift", shift)
                hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                # print("hexa", hexa)
                byte = True if "byte_array" in self.encodings[name]["__init__"] else False
                # print("byte", byte)
                warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                # print("warning", warning)
                self.status = "encode"
                info = self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa,
                                  warning=warning).copy()
                self.status = "decode"
                if byte:
                    if info[1].byte_array:
                        coding = info[1].decode_byte()
                        print_color(coding, color="blue")
                        self.add_history(Password=info[1].password, Text=info[1], coding=coding.byte_array,
                                         decode_encode=self.status, shift=coding.shift if shift else "None")
                        break
                coding = info[1].decode()
                print_color(coding, color="blue")
                self.add_history(Password=info[1].password if password else info[1].rot, Text=info[1], coding=coding.string, decode_encode=self.status, shift=coding.shift if shift else "None")
                break
            elif choice_code == "4":
                print("Développement en cours...")
                continue
        if choice_code not in [str(i) for i in range(1, len(self.class_encodings) + 1)]:
            print_color('Invalid choice', color='red', effect='bold')

    def encode_decode_file(self, return_choice=False):
        self.clear()

        def replace_file(filename: str, update):
            if isinstance(update, str):
                open(filename, 'w').write(update)
            elif isinstance(update, bytearray):
                open(filename, 'wb').write(update)
            else:
                print(type(update))
                raise Exception

        while True:
            ed = ["Encoder" + 20*" ", "Decoder"]
            encode_decode = input("Encoder ou decoder votre fichier ?\n" + self.create_menu(0, ed))
            if int(encode_decode) in [1, 2]:
                encode_decode = ed[int(encode_decode)-1][:6].lower()
                self.banner += f"- {encode_decode.upper()}"
                self.clear()
                self.status = encode_decode
                choice_code = input(self.create_menu(2, list(self.encodings.keys())))
                if return_choice:
                    return choice_code
                for encoding in self.class_encodings:
                    name = encoding.__name__
                    index = str(self.class_encodings.index(encoding) + 1)
                    # print(index)
                    if choice_code == index:
                        self.coding_running = name
                        # print(self.coding_running)
                        # print(self.encodings[name]["__init__"])
                        password = True if "password" in self.encodings[name]["__init__"] else False
                        # print("password", password)
                        shift = True if "shift" in self.encodings[name]["__init__"] else False
                        # print("shift", shift)
                        hexa = True if "hexa" in self.encodings[name]["__init__"] else False
                        # print("hexa", hexa)
                        byte = True if "byte_array" in self.encodings[name]["__init__"] else False
                        # print("byte", byte)
                        warning = encoding.warning if "warning" in self.encodings[name]["__init__"] else None
                        # print("warning", warning)
                        info = self.input_coding(encoding, decode_encode=self.status, password=password, shift=shift, hexa=hexa,
                                          warning=warning, from_file=True, byte=byte).copy()
                        if info[0] is False:
                            print_color('Vous ne pouvez pas choisir cet encodage pour ce fichier', color='red', effect='bold')
                            break
                        update = info[1]
                        filename = info[-1]
                        if byte:
                            replace_file(filename, update.byte_array)
                        else:
                            replace_file(filename, update.string)

                        break
                    elif choice_code == "4":
                        print("Développement en cours...")
                        break
                if choice_code not in [str(i) for i in range(1, len(self.class_encodings) + 1)]:
                    print_color('Invalid choice', color='red', effect='bold')
            else:
                print_color('Invalid choice', color='red', effect='bold')
                sleep(0.5)
            break

    def clear_history(self):
        """
        To clear the program history
        Pour effacer l'historique du programme
        """
        self.clear(effect='strike')
        sleep(0.5)
        self.history = "\nL'historique actuelle a été vidé"
        self.clear()
        sleep(0.5)
        self.history = "\n"

    def save_history(self):
        """
        To save the program history
        Pour sauvegarder l'historique du programme
        """
        with open("historique.txt", "a", encoding='utf-8') as f:
            f.write(self.history)
        print_color("L'historique a été sauvegardé", effect="italic")
        sleep(0.5)
        self.clear()

    def del_save(self):
        self.clear(effect='strike', color='red')
        sleep(0.5)
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
        command = [sys.executable] + sys.argv
        for arg in command:
            if "DeltacodeProject\\__main__.py" in arg:
                command = command + ["-new"]
        # print(command)
        subprocess.Popen(command)
        sys.exit(88)

    def test(self):
        choice_code = input(self.create_menu(2, list(self.encodings.keys())))

        for encoding in self.class_encodings:
            name = encoding.__name__
            index = str(self.class_encodings.index(encoding) + 1)
            # print(index)
            if choice_code == index:
                Shift = 10
                Password = "DELTA's TEAM BY DAISSEUR"
                Text = "Je ne sais pas pourquoi le mot de passe est en anglais mais bon. Alors ça marche ?"
                self.status = "encode"
                encoding_ = encoding(password=Password, string=Text, shift=Shift, debug=True).encode().string
                print_color(encoding_, color='blue')
                self.add_history(Password, Text, encoding_, decode_encode="encode", shift=str(Shift))
                self.status = "decode"
                decoding_ = encoding(Password, encoding_, Shift, hexa=True, debug=True, error_input=True).decode().string
                print_color(decoding_, color='blue')
                self.add_history(Password, encoding_, decoding_, decode_encode="decode", shift=str(Shift))

                break
            elif choice_code == "4":
                print("Développement en cours...")
        if choice_code not in [str(i) for i in range(1, len(self.class_encodings) + 1)]:
            print_color('Invalid choice', color='red', effect='bold')

    def run(self):
        wait = 0.5
        while True:
            self.banner = f' \\\ DELTACODE {__version__}// '
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
                wait = 0
                self.restart()
            elif choice == "9":
                self.test()
            elif choice == "8275":
                print(deltacorp.decode())
                sleep(10.25)
                from DeltacodeProject.game import play
                play()
                exit(0)
            sleep(wait)

if __name__ == '__main__' or "debug" in sys.argv:
    signal.signal(signal.SIGINT, signal_handler)
    main(Cesar, ROT, DayEncoding, copy=True).run()


