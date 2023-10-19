# __main__.py
import sys


def code():
	"""Encode & Decode"""
	def ui():
		from DeltacodeProject.GUI import GUI
		GUI().run()

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
				from DeltacodeProject.game import playterm
				speed = 0.1
                points = 1
                for level in range(1, 10):
                    # playterm(points=int(round(points)), speed=speed).show()
                    wrapper(playterm(points=int(round(points)), speed=speed).show)
                    speed = speed/7 * 3
                    points = points*1.40
                    # sleep(2)
		
if __name__ == "__main__":
	code()
