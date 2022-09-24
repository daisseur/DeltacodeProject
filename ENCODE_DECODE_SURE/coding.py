import shutil
import codecs
import base58
import base64
import time
from deltacode_class import DayEncoding, ROT


def one_again(integer):
    if integer > 1114111:
        return 1114111 - integer


level = int(input("niveau de sécurité : "))
# string = input("Texte à encoder : ")
# password = input("Mot de passe : ")
string = "Encore et encore, des tests !"
password = "Celui-là il va tenir"
shift = int()
for i in password:
    shift += ord(i) - len(password) - len(string)
shift = 0
coding = string



def range_encoding_level(string_, level=level, debug=True):
    for i in range(level):
        if isinstance(string_, bytes):
            string_ = DayEncoding(password, string_.decode('utf8'), shift, error_input=False, hexa=False).encode()
        else:
            string_ = DayEncoding(password, string_, shift, error_input=False, hexa=False).encode()
        if debug:
            try:
                print(f"\t{repr(string_)[1:-1]}")
            except:
                print("IMPOSSIBLE A AFFICHER")
    string_ = bytes(string_, 'utf-8')
    return string_

def range_decoding_level(string_, level=level, debug=True):
    for i in range(level):
        if isinstance(string_, bytes):
            string_ = DayEncoding(password, string_.decode('utf8'), shift, error_input=False, hexa=False).decode()
        else:
            string_ = DayEncoding(password, string_, shift, error_input=False, hexa=False).decode()
        if debug:
            try:
                print(f"\t{repr(string_)[1:-1]}")
            except:
                print("IMPOSSIBLE A AFFICHER")
    string_ = bytes(string_, 'utf-8')
    return string_

def code_print(code):
    global coding
    coding = code
    print("\t", coding)

print(string)
code_print(bytes(coding, 'utf-8'))


def encode():
    code_print(base58.b58encode(coding))
    code_print(base64.b64encode(coding))
    code_print(range_encoding_level(coding, debug=True))
    code_print(base64.b64encode(coding))
    return f"RESULT=\n{str(coding.decode('utf-8'))}"


def decode():
    code_print(base64.b64decode(coding))
    code_print(range_decoding_level(coding, debug=True))
    code_print(base64.b64decode(coding))
    code_print(base58.b58decode(coding))
    return f"RESULT=\n{str(coding.decode('utf-8'))}"
start = time.perf_counter()
encode = encode()
print("=========================================================")
decode = decode()
end = time.perf_counter()
print(f"{encode}\n{decode}")
print("In", end-start)



