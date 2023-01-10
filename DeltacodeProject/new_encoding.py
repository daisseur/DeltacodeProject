from encodings2 import *
import base64
import base58
def eq(string, n):
    if n > len(string):
        return
def encode(string="Hey salut les gens ce message est top secret et ne doit pas..", password="Mon mot de passe hard !!!"):
    base = DayEncoding(password)
    result = str()
    for charp in range(len(password)):
        result += base58.b58encode(string[(charp % len(string))+1].encode('UTF-8')).decode('UTF-8')
        print(result)
    string = result
    for charp in range(len(password)):
        result = DayEncoding(password + result[charp % len(string)], hexa=False, error_input=False).encode(result).string
    for charp in range(len(password)):
        result += base64.b64encode(string[charp % len(string)].encode('UTF-8')).decode('UTF-8')
    print(result)
    return base.encode(result).string

def decode(string, password="Mon mot de passe hard !!!"):
    result = DayEncoding(password).decode(string).string
    for charp in range(len(password)):
        result += base64.b64decode(string[charp % len(string)].encode('UTF-8')).decode('UTF-8')
    for charp in range(len(password)):
        result = DayEncoding(password + result[charp % len(string)], hexa=False, error_input=False).decode(result).string
    print(result)
    for charp in range(len(password)):
        result = base64.b64decode(result.encode("UTF-8"))
        print(result)

        print(len(result))
    return result.decode('UTF-8')


enc = encode()
print(enc)
print("".center(100, "="))
dec = decode(enc)
print(dec)
