from DeltacodeProject.encodings._encodings2 import DayEncoding
import base64
import base58
from time import perf_counter


def eq(string, n):
    if n > len(string):
        return


def new_encode(string="Hey salut les gens ce message est top secret et ne doit pas..", password="Mon mot de passe hard !!!"):
    base = DayEncoding(password)
    result = ""
    # for charp in range(len(password)):
    #     result += base58.b58encode(string[(charp % len(string) + 1)].encode('UTF-8')).decode('UTF-8')
    string = result
    for charp in range(len(password)):
        result = base.encode(result).string
        result = DayEncoding(password + result[charp % len(result)], hexa=False, error_input=False).encode(result).string
    for charp in range(len(password)):
        result += base64.b64encode(string[charp % len(string)].encode('UTF-8')).decode('UTF-8')
    return result


def level_encode(level=50, string="Hey salut les gens ce message est top secret et ne doit pas..",
                 password="Mon mot de passe hard !!!", base_shift=0):
    start = perf_counter()
    string = DayEncoding(password, shift=base_shift, hexa=False).encode(string).string
    base = DayEncoding(password, hexa=False)
    for lvl in range(level):
        string = base.encode(string).string
    return string, perf_counter() - start


def new_decode(string, password="Mon mot de passe hard !!!"):
    result = DayEncoding(password).decode(string).string
    for charp in range(len(password)):
        result += base64.b64decode(string[charp % len(result)].encode('UTF-8')).decode('UTF-8')
    for charp in range(len(password)):
        result = DayEncoding(password + result[charp % len(result)], hexa=False, error_input=False).decode(result).string
    # for charp in range(len(password)):
    #     result = base64.b64decode(result.encode('UTF-8'))
    return result.decode('UTF-8')


if __name__ == "__main__":
    enc = new_encode()
    print(enc)
    print("".center(100, "="))
    dec = new_decode(enc)
    print(dec)
