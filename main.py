# Default page, will add main script
import pyfiglet
from sys import argv
import Network


def print_hi(name):
	import random
	import time

	random.seed(time.time())

	# print(pyfiglet.FigletFont.getFonts())
	# print(pyfiglet.COLOR_CODES)

	my_font = """clb8x10
				cli8x8
				basic
				colossal
				contessa
				cosmic
				doom
				slant
				5lineoblique""".replace('\t', '').split('\n')

	pyfiglet.print_figlet('Kuwo-Spider', font=random.choice(my_font),
	colors=random.choice(list(pyfiglet.COLOR_CODES.keys())), width=100)
	# Use a breakpoint in the code line below to debug your script.
	print(f'By {name}.\n')  # Press Ctrl+F8 to toggle the breakpoint.


def menu() -> str:
	print("Type to search something: (type 'quit()' to quit and 'rank()' to view ranking board)")
	print('tips: input nothing to hang around\n')
	return input()


def hanging_around():
	print('Constructing...')
	pass


def rank():
	print('Constructing...')
	pass


def search(kw: str) -> None:
	print("Searching...")
	pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	# print a banner
	print_hi('ZhengHuang and HeQi')

	if len(argv) > 1:
		...
		exit()

	while True:
		keyword = menu()

		# special keywords
		if keyword == 'quit()':
			print('Bye.')
			exit()
		elif keyword == '':
			hanging_around()
		elif keyword == 'rank()':
			rank()
		else:
			# normal keyword search
			search(keyword)
