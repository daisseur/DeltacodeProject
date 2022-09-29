from deltacode_class import DayEncoding
import time
import string as s
def verif(english_french, result):
    for i in english_french:
        if i in result:
            return True
    return False

string = "DELTA's PROJECT"
password = ""
english = []
french = []

with open('ord_exceptions.txt', 'r', encoding='UTF-8') as f:
    exceptions = str(f.read()).split(",")

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
ifdoc = s.ascii_lowercase
done = False
while not done:
    for i1 in ifdoc:
        print(i1)
        start_for = time.perf_counter()
        for i2 in ifdoc:
            print("i2", i2)
            for i3 in ifdoc:
                print("i3", i3)
                for i4 in ifdoc:
                    print("i4", i4)
                    for i5 in ifdoc:
                        print("i5", i5)
                        for i6 in ifdoc:
                            print("i6", i6)
                            for i7 in ifdoc:
                                print("i7", i7)
                                for i8 in ifdoc:
                                    print("i8", i8)
                                    for i9 in ifdoc:
                                        print("i9", i9)
                                        for i10 in ifdoc:
                                            print("i10", i10)
                                            for ord_ in range(11141110):
                                                print(ord_)
                                                test = DayEncoding(password=i1 + i10 + i9 + i8 + i7 + i6 + i5 + i4 + i3 + i2 + i1, string=string, shift=ord_, hexa=False, error_input=False).encode()
                                                if test in french:
                                                    print("Trouvé : ")
                                                    print(test)
        end_for = time.perf_counter()
        print(end_for - start_for)
    break
end0 = time.perf_counter()

print("Starting (english) : ", end1 - start1)
print("Starting (french) : ", end2 - start2)
print("Principal (english): ", end - start)
print("Principal (french): ", end0 - start0)