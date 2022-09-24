from deltacode_class import DayEncoding
import time

def verif(english_french, result):
    for i in english_french:
        if i in result:
            return True
    return False

string = "DELTA's PROJECT"
password = ""
english = []
french = []

start1 = time.perf_counter()
with open('liste_anglais.txt', 'r', encoding='UTF-8') as f_english:
    for line in f_english.readlines():
        english.append(line)
end1 = time.perf_counter()

start2 = time.perf_counter()
with open('liste_francais.txt', 'r', encoding='latin1') as f_french:
    for line in f_french.readlines():
        french.append(line.replace("\n", ''))
end2 = time.perf_counter()

start = time.perf_counter()
while True:
    for i in english:
        test = repr(DayEncoding(i, string, 0, hexa=False).encode()).replace("'", '')
    break
end = time.perf_counter()

start0 = time.perf_counter()
while True:
    for word in french:
        for i in range(len(french)):
            for ord in range(11141110):
                test = repr(DayEncoding(word + ' ' + french[i], string, ord, hexa=False).encode()).replace("'", '')
                for i_ in english:
                    if i_ in test:
                        print("Trouvé :", password, "==>", test)
                        break
    break
end0 = time.perf_counter()

print("Starting (english) : ", end1 - start1)
print("Starting (french) : ", end2 - start2)
print("Principal (english): ", end - start)
print("Principal (french): ", end0 - start0)