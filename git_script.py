import os


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


if __name__ == "__main__":
    with open('/home/thomas/Bureau/github_gpg_encoded_key.txt', 'r') as f:
        key = f.read()
    os.system("git add .")
    message = input("Message du commit : ")
    os.system(f"git commit -m \"{message}\"")
    password = input("Mot de passe : ")
    result = DayEncoding(password=password, string=key, shift=250).decode()
    print(result)
    os.system(f"echo '{str(result)}' | xclip")
    print("Copié !")
    os.system("ls")
    os.system("echo 'ENCODE_DECODE_SURE/*' | xclip")
    while True:
        rm_spe = 'NONE'
        rm = input("Selectionner un fichier à supprimer du commit ('entrée' pour quitter) : ")
        if rm[-2:] == "/*":
            rm_spe = rm
            rm = rm[:-2]
        if rm == '':
            break
        elif os.path.exists(rm):
            if rm_spe[-2:] == "/*":
                os.system(f"git rm -r --cached {rm_spe}")
            else:
                os.system(f"git rm --cached {rm}")
        else:
            print("Vérifier que le fichier existe bien")
    os.system("git push -u origin main")


