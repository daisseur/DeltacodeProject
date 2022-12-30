# __main__.py

import sys

def code():
	"""Encode & Decode"""
	
	if ".ui" in sys.argv:
		from DeltacodeProject.main import main as ui
		ui().run()
	else:
		from DeltacodeProject.Deltacode import main as menu
		menu().run()
		
if __name__ == "__main__":
	code()
