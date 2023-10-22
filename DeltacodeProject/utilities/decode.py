import os
import sys
from getpass import getpass

print(sys.argv)
print(os.getcwd())
try:
    from DeltacodeProject import DayEncoding
    from DeltacodeProject.scripts import *
except Exception:
    os.system("py -m pip install --upgrade DeltacodeProject")
    os.system("pip install --upgrade DeltacodeProject")
    try:
        from DeltacodeProject import DayEncoding
        from DeltacodeProject.scripts import *
    except:
        raise Exception
password = str()
print_value = True
files = []
hexa = True
shift = str()
validation = True
for arg in sys.argv[1:]:
    if "hexa=" in arg:
        if arg[len("hexa="):].lower() in ["false", "no"]:
            hexa = False

    if "password=" in arg:
        password = arg[len("password="):]
    if "file=" in arg:
        if os.path.exists(arg[len("file="):]):
            files.append(arg[len("file="):])
    if "shift=" in arg:
        try:
            shift = int(arg[len("shift="):])
        except:
            shift = str()
    if "rep=" in arg:
        rep = arg[len("rep="):]
        for file in os.listdir(rep):
            ex = "/" if os.name == "posix" else "\\"
            files.append(rep + ex + file)
            # files.append(rep + ex if rep[-1] != ex else '' + file)
            print(files)
    if "print=" in arg:
        print_value = arg[len("print="):]
        if print_value.lower() in ["false", "no"]:
            print_value = False
        else:
            print_value = True
    if arg.lower() == "valid=false":
        validation = False

if len(password) == 0 or password == "None":
    password = getpass("Mot de passe : ")
if len(files) == 0 or files[0] == "None":
    while True:
        filename = input("Ajouter un fichier à encoder : ")
        if os.path.exists(filename):
            files.append(filename)
        elif filename == '' and len(files) > 1:
            break
if len(str(shift)) == 0 or shift == "None":
    while True:
        shift = input("Shift à appliquer : ")
        if shift == '':
            shift = 0
        try:
            shift = int(shift)
        except:
            continue
        else:
            break


def write_file(filename, data, byte=False):
    if isinstance(data, bytearray):
        open(filename, 'wb').write(data)
    elif byte:
        data = bytearray(ord(i) % 256 for i in data)
        open(filename, 'wb').write(data)
    else:
        open(filename, 'w').write(data)


def get_validation():
    global validation
    if validation:
        validation = input("Êtes-vous sûr de transformer le fichier ? ")
        if not validation.lower() == "oui":
            exit(0)
    return True

for file in files:
    print(file)
    if os.path.basename(__file__) == "encode.py":
        if get_file_ex(file).lower() in bytes_ext:
            coding = DayEncoding(password=password, shift=shift, hexa=False, error_input=False)
            coding = coding.encode_byte(bytearray(open(file, 'rb').read())).byte_array
            if get_validation():
                open(file, 'wb').write(coding)
        else:
            coding = DayEncoding(password=password,
                                 shift=shift, hexa=hexa, error_input=False).encode(open(file, 'r').read()).string
            if get_validation():
                open(file, 'w').write(coding)
        if print_value:
            print(coding)
    elif os.path.basename(__file__) == "decode.py":
        if get_file_ex(file).lower() in bytes_ext:
            coding = DayEncoding(password=password, shift=shift, hexa=False, error_input=False)
            coding = coding.decode_byte(bytearray(open(file, 'rb').read())).byte_array
            if get_validation():
                open(file, 'wb').write(coding)
        else:
            coding = DayEncoding(password=password,
                                 shift=shift, hexa=hexa, error_input=False).decode(open(file, 'r').read()).string
            if get_validation():
                open(file, 'w').write(coding)
        if print_value:
            print(coding)
    else:
        # Auto destruction
        password = 'hDaErLdTA password'
        filename = __file__
        shift = 0
        text = open(filename, 'r').read()
        open(filename, 'w').write(DayEncoding(password=password, shift=shift).encode(text))