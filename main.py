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
	colors=random.choice(list(pyfiglet.COLOR_CODES.keys())), width=120)
	# Use a breakpoint in the code line below to debug your script.
	print(f'By {name}.\n')  # Press Ctrl+F8 to toggle the breakpoint.


def menu() -> str:
	print("Type to search something: (type 'quit()' to quit and 'rank()' to view ranking board)")
	print('tips: input nothing to hang around\n')
	return input()


def print_list(song_list: list) -> None:
	for i, song_i in zip(range(1, len(song_list) + 1), song_list):
		print("{:>2}: {}".format(i, song_i))


def hanging_around():
	print('Constructing...')
	pass


def rank():
	print('Constructing...')
	pass


def search(kw: str) -> None:
	# print("Searching...")

	song_list = Network.search(kw)
	print_list(song_list)

	# Attention, choice == index + 1
	choice = 1
	while True:
		choice = input('choose which you want to download (input "q" to return): ')
		if choice == 'q':
			return
		if not choice.isnumeric() or int(choice) > len(song_list) or int(choice) < 1:
			print('Invalid input, try again.')
			continue
		song_list[int(choice) - 1].download()


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
