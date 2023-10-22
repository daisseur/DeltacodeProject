import sys
from .loading import loading


def signal_handler(signal, *args):  # signal, frame
    if signal == 88:
        sys.exit(0)
    else:
        loading("Sortie du programme...")
        sys.exit(0)
