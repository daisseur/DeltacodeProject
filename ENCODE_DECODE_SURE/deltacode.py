import base58
import base64
import codecs
import os
import string as s
import time
import sys
import shutil
import subprocess

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

centery = int(chercher(str(shutil.get_terminal_size()), "columns=", ",").replace("columns=", "").replace(",",""))
time.sleep(0.5)

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


nbr = 0

banniere = ' \\\ DELTA // '
if os.path.exists("historique.txt"):
    with open("historique.txt", 'r') as f:
        historique = f.read()
else:
    historique = "\n"

if os.name == "posix":
    OS = "LINUX"

    def clear(historique: str, effect='italic', color='white'):
        os.system("clear")
        print_color(banniere.center(centery, ' '), color='green', effect='bold')
        print_color(f"OS: {OS}".center(centery, ' '), color='violet', effect='bold')
        print_color(historique, color=color, effect=effect)
else:
    OS = "WINDOWS"

    def clear(historique: str, effect='italic', color='white'):
        os.system("cls")
        print_color(banniere.center(centery, ' '), color='green', effect='bold')
        print_color(f"OS: {OS}".center(centery, ' '), color='violet', effect='bold')
        print_color(historique, color=color, effect=effect)


def TD_decode(password: str, string: str) -> str:
    password = password.lower()
    lowercase = s.ascii_lowercase
    uppercase = s.ascii_uppercase
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]
        if char in lowercase:
            result += lowercase[lowercase.index(char) - lowercase.index(password[i % password_len])]
        elif char in uppercase:
            result += uppercase[uppercase.index(char) - lowercase.index(password[i % password_len])]
        else:
            result += char
    return result


def TD_encode(password: str, string: str) -> str:
    password = password.lower()
    lowercase = s.ascii_lowercase
    uppercase = s.ascii_uppercase
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]
        if char in lowercase:
            result += lowercase[(lowercase.index(char) + lowercase.index(password[i % password_len])) % 26]
        elif char in uppercase:
            result += uppercase[(uppercase.index(char) + lowercase.index(password[i % password_len])) % 26]
        else:
            result += char
    return result


def ROT_encode(password: str, string: str) -> str:
    password = password.lower()
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]
        try:
            if char not in s.printable:
                char = no_accent_char(char=char)
            result += s.printable[(s.printable.index(char) + s.printable.index(password[i % password_len])) % len(s.printable)]

        except:
            try:
                result += f"[ERROR string:'{s.printable.index(char)}', password:'{password[i % password_len]}']"
            except:
                result += f"[FATAL ERROR: '{char}']"
    return result


def ROT_decode(password: str, string: str) -> str:
    password = password.lower()
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]

        try:
            if char not in s.printable:
                char = no_accent_char(char=char)
            result += s.printable[(s.printable.index(char) - s.printable.index(password[i % password_len]))]
        except:
            try:
                result += f"[ERROR string:'{s.printable.index(char)}', password:'{password[i % password_len]}']"
            except:
                result += f"[FATAL ERROR: '{char}']"
    return result


def Dencode(password: str, string: str, shift: int, escape_code=True, debug=False):
    result = str()
    password_len = len(password)
    """if escape_code:
        string = str(string).encode('UTF-8')"""
    for i in range(len(string)):
        char = string[i]
        """if debug:
            print(string, string[i])
            time.sleep(0.5)"""
        try:
            encoding = chr((ord(char) + ord(password[i % password_len])) + shift % 1114111)
            result += encoding
        except:
            try:
                result += f"[ERROR string:'{char}', password:'{password[i % password_len]}']"
            except:
                result += f"[FATAL ERROR '{char}']"
    return result


def Ddecode(password: str, string: str, shift: int, escape_code=True):
    result = str()
    password_len = len(password)

    for i in range(len(string)):
        char = string[i]
        try:
            result += chr(ord(char) - ord(password[i % password_len]) - shift)
        except:
            try:
                result += f"[ERROR, string:'{char}', password:'{password[i % password_len]}']"
            except:
                result += f"[FATAL ERROR '{char}']"
    return result


def delta_encode(password, text):
    encode_TD = TD_encode(password, text)
    """encode_hex = str(codecs.encode(encode_TD, "hex"))
    encode_b58 = base58.b58encode(encode_hex)
    result = str(encode_b58)"""
    return encode_TD


def delta_decode(password, text):
    """decode_b58 = str(base58.b58decode(text))
    decode_hex = str(codecs.encode(decode_b58, "hex"))"""
    result = TD_decode(password, text)
    return str(result)

# -- Menu


while True:
    centery = int(chercher(str(shutil.get_terminal_size()), "columns=", ",").replace("columns=", "").replace(",", ""))
    banniere = ' \\\ DELTA // '
    clear(historique=historique)
    choice = input("""     
    [1] Encoder
    [2] Décoder
    [3] Effacer l'historique actuel
    [4] Sauvegarder l'historique
    [5] Effacer la sauvegarde de l'historique
    [6] Redémarrer le programme
    """)

    if choice == '1':
        banniere += "- ENCODE"
        clear(historique=historique)
        choice_encode = input("""
        [1] Rotation avec tous les caractères de l'alphabet
        [2] Rotation avec tous les caractères existants
        [3] Test infaillible
        """)
        if choice_encode == "1":
            clear(historique=historique)
            print_color("/!\ S'il y a une lettre avec un accent dans le texte à encoder ou dans le password, la lettre sera transformée pour qu'il n'y ait pas d'accent (à -> a)", color="yellow", effect='underline')
            Password = input('Password : ')
            Text = input('Texte : ')
            print_color(ROT_encode(Password, Text), color='blue')
            historique += "==ENCODE==\n{Password = " + Password + "}\n{Texte = " + Text + "}\n--> " + ROT_encode(Password, Text) + "\n"
        elif choice_encode == "2":
            clear(historique=historique)
            while True:
                Shift = input('Shift : ')
                try:
                    int(Shift)
                except:
                    print_color("/!\ Veuillez rentrer un nombre", color="red", effect="bold")
                    pass
                else:
                    Shift = int(Shift)
                    break
            Password = input('Password : ')
            Text = input('Texte : ')
            print_color(Dencode(Password, Text, Shift), color='blue')
            historique += "==ENCODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Dencode(Password, Text, Shift) + "\n"
        elif choice_encode == "3":
            print("Développement en cours...")
        else:
            print_color('Invalid choice', color='red', effect='bold')
    elif choice == '2':
        banniere += "- DECODE"
        clear(historique=historique)
        choice_decode = input("""
        [1] Rotation avec tous les caractères de l'alphabet
        [2] Rotation avec tous les caractères existants
        [3] Test infaillible
        """)
        if choice_decode == "1":
            clear(historique=historique)
            Password = input('Password : ')
            Text = input('Texte : ')
            print_color(ROT_decode(Password, Text), color='blue')
            historique += "==DECODE===\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + ROT_decode(Password, Text) + "\n"
        elif choice_decode == "2":
            clear(historique=historique)
            while True:
                Shift = input('Shift : ')
                try:
                    int(Shift)
                except:
                    print_color("/!\ Veuillez rentrer un nombre", color="red", effect="bold")
                    pass
                else:
                    Shift = int(Shift)
                    break
            Password = input('Password : ')
            Text = input('Texte : ')
            print_color(Ddecode(Password, Text, Shift), color='blue')
            historique += "==DECODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Ddecode(Password, Text, Shift) + "\n"
        elif choice_decode == "3":
            print("Développement en cours...")
        else:
            print_color('Invalid choice', color='red', effect='bold')
    elif choice == "3":
        clear(historique=historique, effect='strike')
        time.sleep(0.5)
        historique = "\nL'historique actuelle a été vidé"
        clear(historique=historique, effect='italic')
        time.sleep(0.5)
        historique = "\n"

    elif choice == "4":
        with open("historique.txt", "a", encoding='utf-8') as f:
            f.write(historique)
        print_color("L'historique a été sauvegardé", effect="italic")
        time.sleep(0.5)
        clear(historique=historique)
    elif choice == "5":
        clear(historique=historique, effect='strike', color='red')
        time.sleep(0.5)
        historique = "\n"
        os.remove("historique.txt")
        clear(historique=historique)
        print_color("La sauvegarde de l'historique a été supprimé", effect="italic")
    elif choice == "6":
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif choice == "7":
         clear(historique=historique)
         while True:
                Shift = input('Shift : ')
                try:
                    int(Shift)
                except:
                    print_color("/!\ Veuillez rentrer un nombre", color="red", effect="bold")
                    pass
                else:
                    Shift = int(Shift)
                    break

         Password = input('Password : ')
         Text = input('Texte : ')
         print_color(Dencode(Password, Text, Shift), color='blue')
         historique += "==ENCODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Dencode(Password, Text, Shift) + "\n"
         Text = Dencode(Password, Text, Shift)
         print_color(Ddecode(Password, Text, Shift), color='blue')
         historique += "==DECODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Ddecode(Password, Text, Shift) + "\n"
    elif choice == "8":
        Shift = 0
        Password = "DELTA's TEAM BY DAISSEUR"
        Text = "Je ne sais pas pourquoi le mot de passe est en anglais mais bon. Alors ça marche ?"
        print_color(Dencode(Password, Text, Shift, debug=True), color='blue')
        historique += "==ENCODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Dencode(Password, Text, Shift, debug=True) + "\n"
        Text = Dencode(Password, Text, Shift)
        print_color(Ddecode(Password, Text, Shift), color='blue')
        historique += "==DECODE==\n{Shift= " + str(Shift) + "}\n{Password = " + Password + "}\n{Texte = " + Text + \
                          "}\n--> " + Ddecode(Password, Text, Shift) + "\n"
    else:
        print_color('Invalid choice', color='red', effect='bold')


