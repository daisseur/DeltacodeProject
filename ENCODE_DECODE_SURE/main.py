#coding:utf-8

import string as s

def encode(pwd, a_encoder):
    lower = s.ascii_uppercase
    upper = s.ascii_lowercase
    encode = str()
    pwd_len = len(pwd)

    for i in range(len(a_encoder)):
        if a_encoder[i] in upper:
            encode += upper[(upper.index(a_encoder[i]) + lower.index(pwd[i % pwd_len])) % 26]
            print(upper.index(a_encoder[i]), "+", lower.index(pwd[i % pwd_len]), "=", encode)
        elif a_encoder[i] in lower:
            encode += lower[(lower.index(a_encoder[i]) + lower.index(pwd[i % pwd_len])) % 26]
            print(lower.index(a_encoder[i]), "+", lower.index(pwd[i % pwd_len]), "=", encode)
            print(encode)
        else:
            encode += a_encoder[i]
            print(encode)


    print("\n\n\n")
    return encode


def decode(pwd, a_decoder):
    lower = s.ascii_uppercase
    upper = s.ascii_lowercase
    decode = str()
    pwd_len = len(pwd)

    for i in range(len(a_decoder)):
        if a_decoder[i] in upper:
            decode += upper[upper.index(a_decoder[i]) - lower.index(pwd[i % pwd_len])]
            print(upper.index(a_decoder[i]), "-", lower.index(pwd[i % pwd_len]), "=", decode)
        elif a_decoder[i] in lower:
            decode += lower[lower.index(a_decoder[i]) - lower.index(pwd[i % pwd_len])]
            print(lower.index(a_decoder[i]), "-", lower.index(pwd[i % pwd_len]), "=", decode)
            print(decode)
        else:
            decode += a_decoder[i]
            print(decode)

    print("\n\n\n")
    return decode


def debug():
    lower = s.ascii_uppercase
    upper = s.ascii_lowercase
    result = decode(lower, encode(lower, lower))
    validation = lower
    if result != validation:
        print(result, ' != ', validation)
    else:
        print('Passed !')

    result = decode(upper,  encode(upper, lower))
    validation = lower
    if result != validation:
        print(result, ' != ', validation)
    else:
        print('Passed !')

    result = decode(upper, encode(upper, upper))
    validation = upper
    if result != validation:
        print(result, ' != ', validation)
    else:
        print('Passed !')

    result = decode(lower,  encode(lower, upper))
    validation = upper
    if result != validation:
        print(result, ' != ', validation)
    else:
        print('Passed !')


decode_encode = input("Voulez-vous encoder ou decoder ? ")
if "decode" in decode_encode or decode_encode == "d":
    pwd = input("Entrez la clé de decryptage: ")
    a_decoder = input("Texte à décoder: ")
    print("\nDECODE ==>\n")
    print(decode(pwd, a_decoder))
elif "encode" in decode_encode:
    pwd = input("Entrez la clé d'encodage': ")
    a_encoder = input("Texte à encoder: ")
    print("\nENCODE ==>\n")
    print(encode(pwd, a_encoder))










                
