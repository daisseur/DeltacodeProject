# Toutes les classes d'encodage dans un même fichier

import string as s
import time
from DeltacodeProject.scripts import *


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
        self.description = "Rotation"
        self.abbr = "Rotation avec caractères affichables"
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
    def __init__(self, password: str, string: str | list | tuple, shift: int, hexa=True, debug=False, error_input=True, type_return=str):
        self.result = str()
        self.password_len = len(password)
        self.string = string
        self.password = password
        self.shift = shift
        self.type_return = type_return
        if hexa:
            self.hexa = True
        else:
            self.hexa = False
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
        if self.type_return is str:
            to_return = str()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return += i
            else:
                to_return = str(string)
        elif self.type_return is tuple:
            to_return = tuple()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return += (i,)
            else:
                to_return = str(string)
        elif self.type_return is list or self.type_return == "hex":
            to_return = list()
            if isinstance(string, list) or isinstance(string, tuple):
                for i in string:
                    to_return.append(i)
            else:
                to_return = str(string)
        self.debug(self.type_return)
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
        self.string = self.string
        for i in range(len(self.string)):
            char = self.string[i]
            for car in char:
                try:
                    if self.hexa:
                        self.debug("hexa")
                        self.result = tuple(self.result)
                        encoding = hex((ord(car) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                        self.debug(f"'{car}' / {hex(ord(car))} == '{chr((ord(car) + ord(self.password[i % self.password_len])) + self.shift % 1114111)}' / {encoding}")
                    else:
                        self.debug("normal")
                        encoding = chr((ord(car) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                        self.debug(encoding)

                    self.result = self.add_instance(self.result, encoding)
                except:
                    self.error(f"[ERROR string:'{car}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR '{car}']")
        return self.return_(self.result)

    def decode(self):
        # Résultat en valeurs hexadecimales
        # self.result = str()
        self.debug(f"string = {self.string}")
        if self.hexa:
            self.debug("hexa")
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
                    self.result = self.add_instance(self.result, chr((letter_ord - ord(self.password[nbr % self.password_len]) - self.shift) % 1114111))
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