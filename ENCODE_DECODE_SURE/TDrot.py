from ord_valid import valid_ord
shift = 15
string = "hey les gens"
result = tuple()
for i in string:
    encoding = hex(ord(i) + shift)
    result += (encoding,)

print(result)
for i in result:
    print(chr(int(i, 16) - shift))

def fonction_made_in_hex_split(string):
    index_temp = 0
    to_tuple = list()
    add_to_list = str()
    nbr = 0
    if isinstance(string, str):
        for i in string:
            if i == "0" and string[index_temp + 1] == "x":
                add_to_list += string[index_temp] + string[index_temp + 1]
                nbr = 2
                while True:
                    try:
                        if string[index_temp + nbr] != "0":
                            try:
                                if string[index_temp + nbr + 1] != "x":
                                    add_to_list += string[index_temp + nbr]
                                    print(add_to_list)
                                    if add_to_list not in string:
                                        return "ERROR"
                            except:
                                to_tuple.append(add_to_list)
                                add_to_list = str()
                                break
                        else:
                            to_tuple.append(add_to_list)
                            add_to_list = str()
                            break
                    except:
                        to_tuple.append(add_to_list)
                        add_to_list = str()
                        break
                    nbr += 1
                nbr = 2
            index_temp += 1
        return to_tuple

def to_hexa(string, tuple: bool):
    if tuple:
        result = str()
        for i in string:
            result += hex(ord(i))
        return result
    else:
        result = list()
        for i in string:
            result.append(hex(ord(i)))
        return tuple(result)

def encode(shift, string, tuple_return: bool, debug=False):
    shift = int(shift)
    result = tuple()
    for i in string:
        encoding = hex(ord(i) + shift)
        if debug:
            print(i, hex(ord(i)), "=", chr(ord(i) + shift), encoding)
        result += (encoding,)
    if tuple_return:
        return result
    else:
        str_result = str()
        for i in result:
            str_result += str(i)
            if debug:
                print(f"+ {i} ({str(i)})  ", end='')
        return str_result

def decode(shift, string, debug=False):
    shift = int(shift)
    to_tuple = list()
    if isinstance(string, str):
        for hexa in string[2:].split('0x'):
            to_tuple.append('0x' + hexa)
    elif isinstance(string, tuple) or isinstance(string, list):
        to_tuple = string
    else:
        return "ERROR with instance"
    try:
        string = tuple(to_tuple)
    except:
        print("error")
    else:
        if debug:
            print(string)
        result = str()
        for i in string:
            letter_ord = int(i, 16)
            result += chr((letter_ord - shift) % 1114111)
            if debug:
                print(chr(int(i, 16)), i, "=", result[-1], hex(int(i, 16) - shift))
                print(result)
        return result

"""shift = input("Shift : ")
string = input("String : ")"""

shift = "1000"
string = "Il était une fois l'histoire d'un chevalier qui sevait sa Reine quand soudain il s'exclama !"
encode = encode(shift, string, tuple_return=False)
print(str(encode))
print(decode(shift, encode))


