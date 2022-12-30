import os
import sys
from getpass import getpass
print(sys.argv)
print(os.getcwd())
try:
    from DeltacodeProject.ALL_ENCODING import DayEncoding
except Exception:
    os.system("py -m pip install --upgrade DeltacodeProject")
    os.system("pip install --upgrade DeltacodeProject")
    try:
        from DeltacodeProject.ALL_ENCODING import DayEncoding
    except:
        raise Exception
password = str()
files = []
shift = str()
validation = True
for arg in sys.argv[1:]:
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
            files.append(rep + file)

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
for file in files:
    print(file)
    if os.path.basename(__file__) == "encode.py":
        coding = DayEncoding(password=password, string=open(file, 'r').read(), shift=shift).encode()
        print(coding)
        if validation:
            validation = input("Êtes-vous sûr de transformer le fichier ? ")
            if not validation.lower() == "oui":
                exit(0)
        open(file, 'w').write(coding)
    elif os.path.basename(__file__) == "decode.py":
        coding = DayEncoding(password=password, string=open(file, 'r').read(), shift=shift).decode()
        print(coding)
        if validation:
            validation = input("Êtes-vous sûr de transformer le fichier ? ")
            if not validation.lower() == "oui":
                exit(0)
        open(file, 'w').write(coding)
    else:
        # Auto destruction
        password = 'hDaErLdTA password'
        filename = __file__
        shift = 0
        text = open(filename, 'r').read()
        open(filename, 'w').write(DayEncoding(password=password, string=text, shift=shift).encode())