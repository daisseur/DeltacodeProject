# Toutes les classes d'encodage dans un même fichier
# Avec un nouveau fonctionnement
# Pas fini --

import string as s
import time
import types

from DeltacodeProject.scripts import *


class Error(Exception):
    def __init__(self, message):
        self.message = message


class Run_Error(Exception):
    def __init__(self, message):
        self.message = message

class Cesar:
    def __init__(self, rot, string=''):
        self.result = ''
        self.lower = s.ascii_lowercase
        self.upper = s.ascii_uppercase
        self.rot = rot
        self.string = string

    def __str__(self):
        return self.string

    def verif(self, rot, string):
        if string:
            self.string = string
        if not self.string:
            raise Error("No string")
        if rot:
            self.rot = rot
        if not isinstance(self.rot, int):
            try:
                self.rot = int(self.rot)
            except:
                raise Error("La rotation doit être un nombre /!\\")

    def encode(self, string='', rot=0):
        self.result = ''
        self.verif(rot=rot, string=string)
        for i in range(len(self.string)):
            char = no_accent_char(char=self.string[i])
            try:
                if char in self.lower:
                    self.result += self.lower[(self.lower.index(char) + self.rot) % 26]
                elif char in self.upper:
                    self.result += self.upper[(self.upper.index(char) + self.rot) % 26]
                else:
                    self.result += char
            except:
                if char in self.lower:
                    self.result += f"[ERROR string:'{self.lower.index(char)}', rot:'{self.rot}']"
                elif char in self.upper:
                    self.result += f"[ERROR string:'{self.upper.index(char)}', rot:'{self.rot}']"
        return Cesar(rot=self.rot, string=self.result)

    def decode(self, string='', rot=0):
        self.result = ''
        self.verif(rot=rot, string=string)
        for i in range(len(self.string)):
            char = no_accent_char(char=self.string[i])
            if char in self.lower:
                self.result += self.lower[(self.lower.index(char) - self.rot) % 26]
            elif char in self.upper:
                self.result += self.upper[(self.upper.index(char) - self.rot) % 26]
            else:
                self.result += char

        return Cesar(rot=self.rot, string=self.result)


class ROT:
    def __init__(self, password: str, string='', error_input=False):
        self.result = ''
        self.password = password
        self.string = string
        self.error_input = error_input
        self.warning = "/!\ S'il y a une lettre avec un accent dans le texte à encoder ou \
                              dans le password, la lettre sera transformée pour qu'il n'y ait pas d'accent (à -> a)"

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

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

    def verif(self, string, password):
        if string:
            self.string = string
        if not self.string:
            raise Error("No string")
        if password:
            self.password = password
        if not self.password:
            self.result = self.string
            return ROT(password=self.password, string=self.result)

    def encode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in s.printable:
                    char = no_accent_char(char=char)
                    if char not in s.printable:
                        char = "?"
                self.result += s.printable[
                    (s.printable.index(char) + s.printable.index(self.password[i % len(self.password)])) % len(s.printable)]
            except:
                self.error(f"[ERROR string:'{s.printable.index(char)}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return ROT(password=self.password, string=self.result)

    def decode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)

        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in s.printable:
                    char = no_accent_char(char=char)
                self.result += s.printable[(s.printable.index(char) - s.printable.index(self.password[i % len(self.password)])) % len(s.printable)]
            except:
                self.error(f"[ERROR string:'{s.printable.index(char)}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return ROT(password=self.password, string=self.result)


class ROT_OLD:
    def __init__(self, password: str, string='', error_input=False):
        self.result = ''
        self.password = password
        self.string = string
        self.error_input = error_input
        self.warning = "/!\ S'il y a une lettre avec un accent dans le texte à encoder ou \
                              dans le password, la lettre sera transformée pour qu'il n'y ait pas d'accent (à -> a)"
        self.upper = s.ascii_uppercase
        self.lower = s.ascii_lowercase

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

    def error(self, error, fatal_error="[FATAL ERROR]"):
        raise Error(error)

    def verif(self, string, password):
        if string:
            self.string = string
        if not self.string:
            raise Error("No string")
        if password:
            self.password = password
        if not self.password:
            self.result = self.string
            return ROT_OLD(password=self.password, string=self.result)

    def encode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char in self.upper:
                    self.result += self.upper[
                        (self.upper.index(char) + self.upper.index(self.password[i % len(self.password)])) % 26]
                elif char in self.lower:
                    self.result += self.lower[
                        (self.lower.index(char) + self.lower.index(self.password[i % len(self.password)])) % 26]
                else:
                    self.result += char
            except:
                self.error(f"[ERROR string:'{'non'}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return ROT_OLD(password=self.password, string=self.result)

    def decode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char in self.upper:
                    self.result += self.upper[self.upper.index(char) - self.upper.index(self.password[i % len(self.password)]) % 26]
                elif char in self.lower:
                    self.result += self.lower[self.lower.index(char) - self.lower.index(self.password[i % len(self.password)]) % 26]
                else:
                    self.result += char
            except:
                self.error(f"[ERROR string:'{'non'}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return ROT_OLD(password=self.password, string=self.result)


class DayEncoding:
    def __init__(self, password: str, string='', byte_array=bytearray(), shift=0, hexa=True, debug=False, error_input=False):
        self.result = ''
        self.byte_result = bytearray()
        self.int_result = ''
        self.password_len = len(password)
        self.string = ''.join(str(i) for i in string) if isinstance(string, str) or isinstance(string, list) else string
        self.byte_array = byte_array
        self.password = password
        self.shift = shift
        self.estim = 0
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
                self.error("ERREUR: le shift doit être un nombre entier /!\\",)
                return
        if shift > 1114111:
            self.error("ERREUR: le shift ne doit pas dépasser 1114111")
            return

    def __str__(self):
        return ''.join(str(i) for i in self.string)

    def __int__(self):
        result_int = ''
        if self.hexa:
            try:
                result_int = ''.join(str(ord(hex(i))) for i in self.to_hexa(self.string, []))
            except:
                for l in self.string:
                    result_int += str(ord(l))
        else:
            for l in self.string:
                result_int += str(ord(l))
        return int(result_int)

    def __repr__(self):
        return ''.join(str(i) for i in self.string)

    def return_(self, result):
        if isinstance(result, str) or isinstance(result, list) or isinstance(result, tuple):
            string = ''.join(result)
            return DayEncoding(password=self.password, string=''.join(string), shift=self.shift, hexa=self.hexa,
                               debug=self.debug_var, error_input=self.error_input)
        elif isinstance(result, bytearray):
            return DayEncoding(password=self.password, byte_array=result, shift=self.shift,
                               hexa=self.hexa,
                               debug=self.debug_var, error_input=self.error_input)

    def verif(self, shift, string, password):
        if string and not isinstance(string, types.UnionType):
            self.string = string
        if shift:
            if not isinstance(shift, int):
                try:
                    self.shift = int(shift)
                except:
                    Error("ERREUR: le shift doit être un nombre entier /!\\", )
                    return
            if shift > 1114111:
                Error("ERREUR: le shift ne doit pas dépasser 1114111")
                return
        if password:
            self.password = password
        if not self.string or isinstance(self.string, types.UnionType):
            self.debug(repr(string), repr(self.string))
            raise Error("No string")
        if not self.password:
            self.result = self.string
            return DayEncoding(password=self.password, string=self.result, shift=self.shift, hexa=self.hexa, debug=self.debug_var, error_input=self.error_input)

    def verif_byte(self, shift, byte_array, password):
        if byte_array and not isinstance(byte_array, types.UnionType):
            self.byte_array = byte_array
        if shift:
            if not isinstance(shift, int):
                try:
                    self.shift = int(shift)
                except:
                    Error("ERREUR: le shift doit être un nombre entier /!\\", )
                    return
            if shift > 1114111:
                Error("ERREUR: le shift ne doit pas dépasser 1114111")
                return
        if password:
            self.password = password
        if not self.byte_array or isinstance(self.byte_array, types.UnionType):
            self.debug(repr(byte_array), repr(self.byte_array))
            raise Error("No bytearray")
        if not self.password:
            self.byte_result = byte_array
            return DayEncoding(password=self.password, byte_array=self.byte_result, shift=self.shift, hexa=self.hexa,
                               debug=self.debug_var, error_input=self.error_input)

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
        except:
            if self.error_input:
                self.result = self.add_instance(self.result, fatal_error)
            else:
                Error(fatal_error)
        if self.debug_var:
            raise Error(error)

    def debug(self, *args):
        if self.debug_var:
            print_color(*args, color='green', effect='bold')
            time.sleep(0.005)

    def get_estim(self):
        t1 = time.perf_counter()
        random_list = []
        for i in range(len(self.byte_array)):
            byte = self.byte_array[i]
            calc = ((byte + ord(self.password[i % self.password_len])) + self.shift) % 256
            random_list.append(calc)
            break
        return (time.perf_counter()-t1) * len(self.byte_array)

    def encode_byte(self, byte_array=bytearray(), password='', shift=0):
        self.byte_result = bytearray()
        verif = self.verif_byte(byte_array=byte_array, password=password, shift=shift)
        if verif:
            return verif
        self.estim = self.get_estim()
        for i in range(len(self.byte_array)):
            byte = self.byte_array[i]
            try:
                self.debug("normal")
                calc = ((byte + ord(self.password[i % self.password_len])) + self.shift) % 256
                self.int_result += str(calc)
                encoding = calc
                self.debug(encoding)

                self.byte_result.append(encoding)
            except:
                self.error(f"[ERROR byte:'{byte}', password:'{self.password[i % self.password_len]}']",
                           fatal_error=f"[FATAL ERROR '{byte}']")
        return self.return_(self.byte_result)


    def encode(self, string='', password='', shift=0):
        self.result = ''
        verif = self.verif(password=password, string=string, shift=shift)
        if verif:
            return verif
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if self.hexa:
                    self.debug("hexa")
                    self.result = tuple(self.result)
                    encoding = hex((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                    self.debug(
                        f"'{char}' / {hex(ord(char))} == '{chr((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)}' / {encoding}")
                else:
                    self.debug("normal")
                    encoding = chr((ord(char) + ord(self.password[i % self.password_len])) + self.shift % 1114111)
                    self.debug(encoding)

                self.result = self.add_instance(self.result, encoding)
            except:
                self.error(f"[ERROR string:'{char}', password:'{self.password[i % self.password_len]}']",
                           fatal_error=f"[FATAL ERROR '{char}']")
        return self.return_(self.result)

    def to_hexa(self, string, to_tuple):
        for hexa in string[2:].split('0x'):
            to_tuple.append('0x' + hexa)
        return to_tuple

    def decode_byte(self, byte_array=bytearray(), password='', shift=0):
        self.byte_result = bytearray()
        verif = self.verif_byte(byte_array=byte_array, password=password, shift=shift)
        if verif:
            return verif
        self.debug(f"bytes = {self.byte_array}")
        for i in range(len(self.byte_array)):
            byte = self.byte_array[i]
            try:
                coding = ((byte - ord(self.password[i % self.password_len])) - self.shift) % 256
                self.byte_result.append(coding)
                self.debug(coding)
            except:
                self.error(f"[ERROR, bytes:'{byte}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR '{byte}']")
        return self.return_(self.byte_result)

    def decode(self, string='', password='', shift=0):
        # Résultat en valeurs hexadecimales
        self.result = ''
        verif = self.verif(password=password, string=string, shift=shift)
        if verif:
            return verif
        self.debug(f"string = {self.string}")
        if self.hexa:
            self.debug("hexa")
            to_tuple = list()
            if isinstance(self.string, str):
                self.to_hexa(self.string, to_tuple)
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
            for i in range(len(str(self.string))):
                char = self.string[i]
                try:
                    coding = chr(((ord(char) - ord(self.password[i % self.password_len])) - self.shift) % 1114111)
                    self.result += coding
                    self.debug(coding)
                except:
                    self.error(f"[ERROR, string:'{char}', password:'{self.password[i % self.password_len]}']", fatal_error=f"[FATAL ERROR '{char}']")
        return self.return_(self.result)


class Custom:
    def __init__(self, password: str, string='', custom=s.ascii_lowercase, error_input=False):
        self.result = ''
        self.password = password
        self.string = string
        self.custom = custom
        self.error_input = error_input
        self.warning = "/!\ S'il y a une lettre avec un accent dans le texte à encoder ou \
                              dans le password, la lettre sera transformée pour qu'il n'y ait pas d'accent (à -> a)"

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

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

    def verif(self, string, password):
        if string:
            self.string = string
        if not self.string:
            raise Error("No string")
        if password:
            self.password = password
        if not self.password:
            self.result = self.string
            return Custom(password=self.password, string=self.result, custom=self.custom)

    def encode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in self.custom:
                    char = no_accent_char(char=char)
                    if char not in self.custom:
                        char = "?"
                        self.result += char
                    else:
                        self.result += self.custom[
                            (self.custom.index(char) + self.custom.index(self.password[i % len(self.password)])) % len(
                                self.custom)]

                else:
                    self.result += self.custom[(self.custom.index(char) + self.custom.index(self.password[i % len(self.password)])) % len(self.custom)]
            except:
                self.error(f"[ERROR string:'{self.custom.index(char)}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return Custom(password=self.password, string=self.result, custom=self.custom)

    def decode(self, string='', password=''):
        self.result = ''
        self.verif(string=string, password=password)
        for i in range(len(self.string)):
            char = self.string[i]
            try:
                if char not in self.custom:
                    char = no_accent_char(char=char)
                    if char not in self.custom:
                        self.result += char
                    else:
                        self.result += self.custom[
                            (self.custom.index(char) - self.custom.index(self.password[i % len(self.password)])) % len(
                                self.custom)]
                else:
                    self.result += self.custom[(self.custom.index(char) - self.custom.index(self.password[i % len(self.password)])) % len(self.custom)]
            except:
                self.error(f"[ERROR string:'{self.custom.index(char)}', password:'{self.password[i % len(self.password)]}']", fatal_error=f"[FATAL ERROR: '{char}']")
        return Custom(password=self.password, string=self.result, custom=self.custom)