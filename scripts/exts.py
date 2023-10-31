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
