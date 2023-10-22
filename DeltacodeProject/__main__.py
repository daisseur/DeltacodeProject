# __main__.py
import sys


def code():
    """Encode & Decode"""
    def ui():
        from .gui import App
        App().mainloop()

    def new():
        from .DeltacodeNew import main as menu
        from .encodings import Cesar, ROT, DayEncoding
        menu(Cesar, ROT, DayEncoding, copy=True).run()

    def old():
        from .Deltacode import main as menu
        menu().run()

    if "-ui" in sys.argv:
        ui()
    elif "-new" in sys.argv:
        new()
    elif "-old" in sys.argv:
        old()
    else:
        from DeltacodeProject.DeltacodeNew import main as menu
        match input(menu(copy=False).create_menu(1, ["Nouveau (adaptatif + byte) ==> DeltacodeNew", "Ancien ==> Deltacode"])):
            case "1":
                    new()
            case "2":
                    old()
            case other:
                    from DeltacodeProject.game.play import play
                    play()


if __name__ == "__main__":
    code()
