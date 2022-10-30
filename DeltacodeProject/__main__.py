# __main__.py

import sys
from DeltacodeProject.DeltacodeProject import main as menu
from DeltacodeProject import main as ui

def code():
	"""Encode & Decode"""
	
	if ".ui" in sys.argv:
		ui().run()
	else:
		menu().run()
		
if __name__ == "__main__":
	code()
