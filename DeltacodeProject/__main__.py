# __main__.py
import sys
from DeltacodeProject.Deltacode import main


def code():
	"""Encode & Decode"""
	def ui():
		from DeltacodeProject.main import main as ui
		ui().run()

	def new():
		from DeltacodeProject.DeltacodeNew import main as menu
		from DeltacodeProject.encodings2 import Cesar, ROT, DayEncoding
		menu(Cesar, ROT, DayEncoding, copy=True).run()

	def old():
		from DeltacodeProject.Deltacode import main as menu
		menu().run()

	if "-ui" in sys.argv:
		ui()
	elif "-new" in sys.argv:
		new()
	elif "-old" in sys.argv:
		old()
	else:
		match input(main(copy=False).create_menu(1, ["Nouveau (adaptatif + byte) ==> DeltacodeNew", "Ancien ==> Deltacode"])):
			case "1":
				new()
			case "2":
				old()
			case other:
				from DeltacodeProject.things.more import playterm
				playterm().show()
		
if __name__ == "__main__":
	code()
