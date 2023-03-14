from unidecode import unidecode

bytes_ext = [
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico',  # Images
    '.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.3gpp',  # Audio
    '.mp4', '.mov', '.avi', '.mkv',  # Vidéos
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.chm',  # Documents
    '.exe', '.dll', '.so', '.o', '.obj', '.pyc', '.msi', '.msix', '.jar', '.rmskin',  # Fichiers binaires
    '.zip', '.tar', '.gz', '.bz2', '.xz', '.rar', '.7z', '.tar.gz',  # Archives
    '.bmp', '.tiff', '.tif', '.svg', '.eps', '.raw',  # Images
    '.aac', '.wma', '.alac', '.mka',  # Audio
    '.mov', '.wmv', '.m4v', '.m2ts', '.mts', '.ts', '.3gp', '.3g2',  # Vidéos
    '.ai', '.psd', '.indd', '.ai', '.eps', '.pdf', '.dwg', '.dxf',  # Documents
    '.tar.bz2', '.tar.xz', '.tgz', '.tbz2', '.txz', '.bz2', '.z', '.arj', '.cab', '.deb', '.rpm',  # Archives
    '.xcf', '.sketch', '.psp',  # Fichiers de conception
    '.dat', '.db', '.dbf', '.sqlite', '.pdb', '.mdb', '.accdb', '.pst', '.ost',  # Fichiers de base de données
    '.iso', '.img', '.dmg', '.toast', '.vhd', '.vhdx', '.qcow', '.qcow2',  # Fichiers d'images de disque
    '.eml', '.msg', '.pst', '.ost', '.mbox', '.dbx', '.mbx',  # Fichiers de messagerie
    '.avi', '.flv', '.wmv', '.rm', '.rmvb', '.asf', '.mpeg', '.mpg',  # Autres formats de vidéos
    '.mid', '.midi', '.kar', '.rmi', '.m4p', '.m4b',  # Autres formats de musique
    '.cr2', '.nef', '.sr2', '.orf', '.rw2', '.pef', '.arw',  # Formats d'images RAW
    '.lnk'  # Raccourci
]

def get_file_ex(filename):
    ext = filename[filename.index("."):]
    return ext

def chercher(txt, premier, deuxieme, replace=False):
    if deuxieme == "'":
        deuxieme = "' "

    result = (txt[txt.find(premier): txt.find(deuxieme)])

    if result == "":
        result = "#La chaîne de caractères n'a pas été trouvée#"

    result = str(result)

    if not result.startswith(deuxieme, 18) and result != "#La chaîne de caractères n'a pas été trouvée#":
        result = result + deuxieme

    if replace:
        result = result.replace(premier, '').replace(deuxieme, '')
    return result

def no_accent_char(char):
    return unidecode(char)

def print_color(*args, color='white', effect='classic', highlight='False') -> None:
    nocolor = "\033[0;0m"
    colors = {
        'black': '0;',
        'red': '1;',
        'green': '2;',
        'yellow': '3;',
        'blue': '4;',
        'violet': '5;',
        'cyan': '6;',
        'grey': '7;',
        'white': '9;'}
    effects = {
        'bold': '1m',
        'classic': '2m',
        'italic': '3m',
        'underline': '4m',
        'strike': '9m'}
    highlights = {
        'False': '\033[3',
        'True': '\033[4'}
    print(highlights[highlight] + colors[color] + effects[effect] + ' '.join(str(arg) for arg in args) + nocolor)