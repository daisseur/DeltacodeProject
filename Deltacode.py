# TEAM DELTA / DELTA's TEAM
# By daisseur, discord: daisseur#7755
import os
import string as s
import time
import sys
import shutil

def chercher(txt, premier, deuxieme):
    if deuxieme == "'":
        deuxieme = "' "

    result = (txt[txt.find(premier): txt.find(deuxieme)])

    if result == "":
        result = "#La chaîne de caractères n'a pas été trouvée#"

    result = str(result)

    if not result.startswith(deuxieme, 18) and result != "#La chaîne de caractères n'a pas été trouvée#":
        result = result + deuxieme

    return result


def no_accent_char(char):
    """Retire l'accent d'un caractère"""
    table_correspondance = {192: 65,
                            193: 65,
                            194: 65,
                            195: 65,
                            196: 65,
                            197: 65,
                            198: 65,
                            199: 67,
                            200: 69,
                            201: 69,
                            202: 69,
                            203: 69,
                            204: 73,
                            205: 73,
                            206: 73,
                            207: 73,
                            208: 68,
                            209: 78,
                            210: 79,
                            211: 79,
                            212: 79,
                            213: 79,
                            214: 79,
                            216: 79,
                            217: 85,
                            218: 85,
                            219: 85,
                            220: 85,
                            221: 89,
                            224: 97,
                            225: 97,
                            226: 97,
                            227: 97,
                            228: 97,
                            229: 97,
                            230: 97,
                            231: 99,
                            232: 101,
                            233: 101,
                            234: 101,
                            235: 101,
                            236: 105,
                            237: 105,
                            238: 105,
                            239: 105,
                            240: 111,
                            241: 110,
                            242: 111,
                            243: 111,
                            244: 111,
                            245: 111,
                            246: 111,
                            248: 111,
                            249: 117,
                            250: 117,
                            251: 117,
                            252: 117,
                            253: 121

                            }

    if 192 <= ord(char) <= 214 or 216 <= ord(char) <= 253:
        return chr(table_correspondance[ord(char)])
    else:
        return char


def no_accent_word(string):
    """Retire tous les accents d'un mot"""
    new_string = ""
    for char in string:
        new_string += no_accent_char(char)

    return new_string


def print_color(string, color='white', effect='classic', highlight='False') -> None:
    nocolor = "\033[0;0m"
    colors = {
        'black': '0;',
        'red': '1;',
        'green': '2;',
        'yellow': '3;',
        'blue': '4;',
        'violet': '5;',
        'cyan': '6;',
        'grey': '7;',
        'white': '9;'}
    effects = {
        'bold': '1m',
        'classic': '2m',
        'italic': '3m',
        'underline': '4m',
        'strike': '9m'}
    highlights = {
        'False': '\033[3',
        'True': '\033[4'}
    print(highlights[highlight] + colors[color] + effects[effect] + str(string) + nocolor)


class Cesar:
    def __init__(self, rot, string: str):
        self.lower = s.ascii_lowercase
        self.upper = s.ascii_uppercase
        self.rot = rot
        self.string = string

    def encode(self):
        if not isinstance(self.rot, int):
            try:
                self.rot = int(self.rot)
            except:
                return "ERREUR: La rotation doit être un nombre /!\\"
        if self.rot > 26:
            return "ERREUR: La rotation ne doit pas dépasser 26"

        result = str()
        for i in range(len(self.string)):
            char = no_accent_char(char=self.string[i])
            try:
                if char in self.lower:
                    result += self.lower[self.lower.index(char) + self.rot % 26]
                elif char in self.upper:
                    result += self.upper[self.upper.index(char) + self.rot % 26]
                else:
                    result += char
            except:
                if char in self.lower:
                    result += f"[ERROR string:'{self.lower.index(char)}', rot:'{self.rot}']"
                elif char in self.upper:
                    result += f"[ERROR string:'{self.upper.index(char)}', rot:'{self.rot}']"
        return result

    def decode(self):
        if not isinstance(self.rot, int):
            try:
                self.rot = int(self.rot)
            except:
                return "ERROR: La rotation doit être un nombre /!\\"
        if self.rot > 26:
            return "ERREUR: La rotation ne doit pas dépasser 26"
        result = str()
        for i in range(len(self.string)):
            char = no_accent_char(char=self.string[i])
            if char in self.lower:
                result += self.lower[self.lower.index(char) - self.rot % 26]
            elif char in self.upper:
                result += self.upper[self.upper.index(char) - self.rot % 26]
            else:
                result += char

        return result


class ROT:
    def __init__(self, password: str, string: str, error_input=False):
        self.result = str()
        self.password = password
        self.string = string
        self.password_len = len(password)
        self.error_input = error_input

    def error(self, error, fatal_error="[FATAL ERROR]"):
        try:
            if self.error_input:
                self.result += error
            else:
                print_color(error, color='red', effect='underline')
        except:
            if self.error_input:
                self.result += fatal_error
            else:
                print_color(fatal_error, color='red', effect='underline', highlight='True')


    def encode(self):
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in s.printable:
                    char = no_accent_char(char=char)
                    if char not in s.printable:
                        char = "?"
                self.result += s.printable[
                    (s.printable.index(char) + s.printable.index(self.password[i % self.password_len])) % len(s.printable)]

            except:
                self.error(f"[ERROR string:'{s.printable.index(char)}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return self.result

    def decode(self):
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in s.printable:
                    char = no_accent_char(char=char)
                self.result += s.printable[(s.printable.index(char) - s.printable.index(self.password[i % self.password_len]))]
            except:
                self.error(f"[ERROR string:'{s.printable.index(char)}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return self.result


class DayEncoding:
    def __init__(self, password: str, string, shift: int, hexa=True, debug=False, error_input=True, type_return=str):
        self.result = str()
        self.password_len = len(password)
        self.string = string
        self.password = password
        self.shift = shift
        self.type_return = eval("type_return" + "()")
        self.hexa = hexa
        self.debug_var = debug
        self.error_input = error_input
        self.debug(f"DayEncoding vient d'être appelée, result = {type(self.result)} = {self.result}")
        self.debug(hexa)
        if not isinstance(shift, int):
            try:
                self.shift = int(shift)
            except:
                self.error("ERREUR: le shift doit être un nombre /!\\",)
                return
        if shift > 1114111:
            self.error("ERREUR: le shift ne doit pas dépasser 1114111")
            return
        type_authorized = [str, tuple, list, 'hex']

        if type_return not in type_authorized:
            self.error("ERREUR: les types autorisés sont: str, tuple, list et 'hex'")
            return

    def return_(self, string):
        to_return = None
        if self.type_return is str():
            to_return = str()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return += i
            else:
                to_return = str(string)
        elif self.type_return is tuple():
            to_return = tuple()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return += (i,)
            else:
                to_return = str(string)
        elif self.type_return is list():
            to_return = list()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return.append(i)
            else:
                to_return = str(string)
        self.debug(type(self.type_return))
        return to_return

    def add_instance(self, to_be_add, string: str):
        string = str(string)
        self.debug(f"Adding instance... {type(to_be_add)} + {string}")
        if isinstance(to_be_add, list):
            to_be_add.append(string)
            self.debug("added")
        if isinstance(to_be_add, tuple):
            to_be_add += (string,)
            self.debug("added")
        if isinstance(to_be_add, str):
            to_be_add += string
            self.debug("added")
        return to_be_add

    def error(self, error, fatal_error="[FATAL ERROR]"):
        try:
            if self.error_input:
                self.result = self.add_instance(self.result, error)
            else:
                print_color(error, color='red', effect='underline')
        except Exception:
            if self.error_input:
                self.result = self.add_instance(self.result, fatal_error)
            else:
                print_color(fatal_error, color='red', effect='underline', highlight='True')
        if self.debug_var:
            raise Exception

    def debug(self, debug_message):
        if self.debug_var:
            print_color(debug_message, color='green', effect='bold')
            time.sleep(0.005)

    def encode(self):
        self.string = str(self.string)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if self.hexa:
                    self.result = tuple(self.result)
                    encoding = hex((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                    self.debug(f"'{char}' / {hex(ord(char))} == '{chr((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)}' / {encoding}")
                else:
                    encoding = chr((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                    self.debug(encoding)

                self.result = self.add_instance(self.result, encoding)
            except:
                self.error(f"[ERROR string:'{char}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR '{char}']")
        return self.return_(self.result)

    def decode(self):
        # Résultat en valeurs hexadecimales
        self.result = str()
        self.debug(f"string = {self.string}")
        if self.hexa:
            to_tuple = list()
            if isinstance(self.string, str):
                for hexa in self.string[2:].split('0x'):
                    to_tuple.append('0x' + hexa)
            elif isinstance(self.string, tuple) or isinstance(self.string, list):
                to_tuple = self.string
            try:
                string = tuple(to_tuple)
            except:
                self.error("Une erreur s'est produite lors de la préparation au décodage")
            else:
                nbr = 0
                self.debug(string)
                for i in string:
                    letter_ord = int(i, 16)
                    self.result += chr((letter_ord - ord(self.password[nbr % self.password_len]) - self.shift) % 1114111)
                    self.debug(f"'{chr(int(i, 16))}' / {i} == '{self.result[-1]}' / {hex((letter_ord - self.shift) % 1114111)}\n{self.result}")
                    nbr += 1
                return self.return_(self.result)
        else:
            for i in range(len(self.string)):
                char = self.string[i]
                try:
                    self.result += chr((ord(char) - ord(self.password[i % self.password_len])) - self.shift)
                except:
                    self.error(f"[ERROR, string:'{char}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR '{char}']")
        return self.return_(self.result)

class Deltacode:
    """                                                 \\\ DELTA-ENCODING //
    To decode or encode a text/string with rotation using all the existing characters.
    Pour encoder ou décoder un texte ou une chaîne de charactères avec une rotation utilisant tous les charactères existants.

    Example\\Exemple :

    """
    def __init__(self):
        self.use_copy = True
        self.valid_char = s.printable
        self.status = "in __init__"
        self.center_y = int(chercher(str(shutil.get_terminal_size()), "columns=", ",").replace("columns=", '').replace(",", ''))
        self.banner = ' \\\ DELTA // '
        self.password_running = "None"
        self.text_running = "None"
        self.shift_running = 0
        if os.path.exists("historique.txt"):
            with open("historique.txt", 'r') as f: self.history = f.read()
        else: self.history = "\n"
        if os.name == "posix": self.OS = "LINUX"
        elif os.name == "nt": self.OS = "WINDOWS"

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
            self.history += f"==ENCODE==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
        elif decode_encode == "decode":
            self.history += f"==DECODE==\n{shift_insert}{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"

    def input_coding(self, coding_function, decode_encode: str, shift=False, password=True, warning="None", from_file=False, **kwargs):
        if "hexa" in kwargs.keys():
            hexa = kwargs.fromkeys("hexa")
        else:
            hexa = None
            kwargs["hexa"] = None
        self.clear()
        if warning != "None":
            print_color(warning, color='yellow', effect='underline')
        self.copy(str(self.password_running))
        if hexa:
            hexa = input("Voulez-vous utiliser l'encodage hexadecimal ? ")
            if hexa.lower() == "oui":
                hexa = True
            else:
                hexa = False
        if password == True:
            Password = input('Mot de passe : ')
        else:
            Password = input("Nombre de rotation à effectuer : ")
        self.copy(str(self.text_running))
        if from_file:
            while True:
                filename = input('Nom du fichier : ')
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='UTF-8') as f:
                        Text = f.read()
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
                        int(Shift)
                    except:
                        print_color("/!\ Veuillez rentrer un nombre", color="red", effect="bold")
                    else:
                        Shift = int(Shift)
                        break
                if self.status == 'encode':
                    coding = coding_function(Password, Text, Shift, hexa).encode()
                else:
                    coding = coding_function(Password, Text, Shift, hexa).decode()
                print_color(coding, color='blue')
                self.add_history(Password, Text, coding, decode_encode, shift=str(Shift))
                self.text_running = coding
                self.password_running = Password
                self.shift_running = Shift
                if from_file is True:
                    return {"Password": Password,
                             "Text": Text,
                             "Encoded": coding,
                             "Shift": Shift,
                             "Filename": filename,
                             "Hexa": hexa}
                return {"Password": Password,
                 "Text": Text,
                 "Encoded": coding,
                 "Shift": Shift,
                 "Hexa": hexa}
            else:
                Shift = 0
                if self.status == 'encode':
                    coding = coding_function(Password, Text, Shift, hexa).encode()
                else:
                    coding = coding_function(Password, Text, Shift, hexa).decode()
                self.add_history(Password, Text, coding, decode_encode, shift=str(Shift))
                self.shift_running = Shift
        else:
            if decode_encode == "encode":
                coding = coding_function(Password, Text).encode()
            else:
                coding = coding_function(Password, Text).decode()
            print_color(coding, color='blue')
            self.add_history(Password, Text, coding, decode_encode)
        self.text_running = coding
        self.password_running = Password
        if from_file is True:
            return {"Password": Password,
                    "Text": Text,
                    "Encoded": coding,
                    "Filename": filename,
                    "Hexa": hexa}
        return {"Password": Password,
                "Text": Text,
                "Encoded": coding,
                "Hexa": hexa}

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
        calcul = tab*6 + 2*len(end) + len_max + len(str(len(lst))) + 3
        # print(calcul)
        if calcul > self.center_y or (calcul + tab*6) > self.center_y:
            menu_tab = (self.center_y - calcul) * " " + end
            new_calcul = len(menu_tab) + 2*len(end) + len_max + len(str(len(lst))) + 3
            if new_calcul > self.center_y:
                menu_tab = end
            if new_calcul - 2*len(end) > self.center_y:
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
        menu += f"{menu_tab}{'—'*len_max}{end}\n\n{menu_entry}>> "
        return menu


class main(Deltacode):
    def __init__(self, copy=None):
        super().__init__()
        if copy is None:
            self.use_copy = input("Voulez-vous utiliser la fonction copier ? Elle vous aidera à copier vos mots de passe, et texte déjà encodés directement quand vous en aurez besoin.\n")
            if self.use_copy.lower() == "oui":
                self.use_copy = True
            else:
                self.use_copy = False
        elif copy is True:
            self.use_copy = True
        elif copy is False:
            self.use_copy = False
    def choice_encoding(self):
        """
        Choice to encoding
        Choix pour encoder
        """
        self.banner += "- ENCODE"
        self.clear()
        self.status = "encode"
        choice_encode = input(self.create_menu(2, ["Code Cesar",
                                                   "Rotation avec caractères affichables",
                                                   "Rotation avec tous les caractères existants",
                                                   "Test infaillible"]))
        if choice_encode == "1":
            self.input_coding(Cesar, decode_encode=self.status, password=False)
        elif choice_encode == "2":
            self.input_coding(ROT, decode_encode=self.status,
                              warning="/!\ S'il y a une lettre avec un accent dans le texte à encoder ou \
                              dans le password, la lettre sera transformée pour qu'il n'y ait pas d'accent (à -> a)")
        elif choice_encode == "3":
            self.input_coding(DayEncoding, decode_encode=self.status, shift=True, hexa=True)
        elif choice_encode == "4":
            print("Développement en cours...")
        else:
            print_color('Invalid choice', color='red', effect='bold')

    def choice_decoding(self, return_choice=False):
        """
        Choice to decoding
        Choix pour decoder
        """
        self.banner += "- DECODE"
        self.clear()
        self.status = "decode"
        choice_decode = input(self.create_menu(2, ["Code Cesar",
                                                   "Rotation avec caractères affichables",
                                                   "Rotation avec tous les caractères existants",
                                                   "Test infaillible"]))
        if return_choice:
            return choice_decode
        if choice_decode == "1":
            self.input_coding(Cesar, decode_encode=self.status, password=False)
        elif choice_decode == "2":
            self.input_coding(ROT, decode_encode=self.status)
        elif choice_decode == "3":
            self.input_coding(DayEncoding, decode_encode=self.status, shift=True, hexa=True)
        elif choice_decode == "4":
            print("Développement en cours...")
        else:
            print_color('Invalid choice', color='red', effect='bold')

    def encoding_decoding(self):
        """
        To encode and decode with the encoding that has been chosen
        Pour encoder et décoder avec l'encodage qui a été choisi
        """
        self.banner += "- ENCODE & DECODE"
        self.clear()
        self.status = "encode"
        choice_code = input(self.create_menu(2, ["Code Cesar",
                                                   "Rotation avec caractères affichables",
                                                   "Rotation avec tous les caractères existants",
                                                   "Test infaillible"]))
        if choice_code == "1":
            info = self.input_coding(Cesar, decode_encode=self.status, password=False).copy()
            try:
                Password = info["Password"]
                Text = info["Encoded"]
                self.status = "decode"
                coding = Cesar(rot=Password, string=Text).decode()
                print_color(coding, color='blue')
                self.history += f"==DECODE==\n{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
            except:
                print("KEY ERROR")
        elif choice_code == "2":
            info = self.input_coding(ROT, decode_encode=self.status).copy()
            try:
                Password = info["Password"]
                Text = info["Encoded"]
                coding = ROT(Password, Text).decode()
                print_color(coding, color='blue')
                self.history += f"==DECODE==\n{self.curly(f'Rotation = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
            except:
                print("KEY ERROR")
        elif choice_code == "3":
            info = self.input_coding(DayEncoding, decode_encode=self.status, shift=True, hexa=True).copy()
            try:
                Password = info["Password"]
                Text = info["Encoded"]
                Shift = info["Shift"]
                Hexa = info["Hexa"]
                self.status = "decode"
                coding = DayEncoding(Password, Text, Shift, hexa=Hexa).decode()
                print_color(coding, color='blue')
                self.history += f"==DECODE==\n{self.curly(f'Shift = {Shift}')}\n{self.curly(f'Password = {Password}')}\n{self.curly(f'Texte = {Text}')}\n|--> {coding}\n"
            except:
                print("KEY ERROR")


        elif choice_code == "4":
            print("Développement en cours...")
        else:
            print_color('Invalid choice', color='red', effect='bold')

    def encode_decode_file(self):
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
                choice_decode = input(self.create_menu(2, ["Code Cesar",
                                                           "Rotation avec caractères affichables",
                                                           "Rotation avec tous les caractères existants",
                                                           "Test infaillible"]))
                if choice_decode == "1":
                    info = self.input_coding(Cesar, decode_encode=self.status, password=False, from_file=True).copy()
                    update = info["Encoded"]
                    filename = info["Filename"]
                    replace_file(filename, update)
                elif choice_decode == "2":
                    info = self.input_coding(ROT, decode_encode=self.status, from_file=True).copy()
                    update = info["Encoded"]
                    filename = info["Filename"]
                    replace_file(filename, update)
                elif choice_decode == "3":
                    info = self.input_coding(DayEncoding, decode_encode=self.status, shift=True, hexa=True, from_file=True).copy()
                    update = info["Encoded"]
                    filename = info["Filename"]
                    replace_file(filename, update)
                elif choice_decode == "4":
                    print("Développement en cours...")
                else:
                    print_color('Invalid choice', color='red', effect='bold')
                break

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
            os.execl(sys.executable, sys.executable, *sys.argv)
        except:
            print_color("Cette fonction n'est actuellement pas fonctionnel sur votre appareil", color="red", effect="bold")
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


if __name__ == '__main__':
    main(copy=True).run()
