# __main__.py

import sys
from DeltacodeProject import main

def main():
	"""Encode & Decode"""
	if len(sys.argv) > 1:
		print("A venir...")
	else:
		main().run()
if __name__ == "__main__":
	main()
