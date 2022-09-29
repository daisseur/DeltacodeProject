import time
def getHexSplit(string):
    res = []
    for hexa in string[2:].split('0x'):
        res.append('0x' + hexa)
    return res


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

def getHex(string):
    hexa = '0x'
    res = []
    for i in range(2, len(string) - 1):
        if string[i] == '0' and string[i + 1] == 'x':
            res.append(hexa)
            hexa = ''
        hexa += string[i]
    res.append(hexa + string[-1])

    return res

def benchmark(function, loops, *args):
    global results
    t = time.perf_counter()
    for i in range(loops):
        function(*args)
    results.append(f'{function.__name__} : {round((time.perf_counter() - t) * 1000, 5)}')
    return

if __name__ == '__main__':
    results = list()
    string = str()
    for i in "VA TA FAIRE ENCULER TOKA, UI JE TE HAIS":
        string += str(hex(ord(i)))

    benchmark(getHexSplit, 10000, string)
    benchmark(getHex, 10000, string)
    benchmark(fonction_made_in_hex_split, 10000, string)
    print(results)

