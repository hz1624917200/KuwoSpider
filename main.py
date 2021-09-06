# Default page, will add main script
from typing import List
import pyfiglet
from sys import argv

import Class
import Network

# global variable
rank_lists: List[Class.RankList] = []


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


def print_list(my_list: list) -> None:
	for i, my_item in zip(range(1, len(my_list) + 1), my_list):
		print("{:>2}: {}".format(i, my_item))


def hanging_around():
	print('Constructing...')
	pass


def rank():
	# print('Rank Constructing...')
	global rank_lists

	# rank lists not initialized
	if not rank_lists:
		# rank list is empty, call Network to fill it
		rank_lists = Network.fill_rank_list()

	print_list(rank_lists)


def search(kw: str) -> None:
	import re
	# print("Searching...")

	song_list = Network.search(kw)
	print_list(song_list)

	# Attention, choice == index + 1
	while True:
		choice = input('choose which you want to download (input "q" to return), support section ex "2-5": ')
		# quit
		if choice == 'q':
			return

		if not choice.isnumeric() or int(choice) > len(song_list) or int(choice) < 1:
			res = re.match(r'\d+-\d+', choice)
			if res:
				(start, end, *_) = res.group().split('-')
				if int(start) < 1 or int(end) > len(song_list):
					print('Invalid input, try again.')
				else:
					# valid section input, return iterable
					for i in range(int(start) - 1, int(end)):
						song_list[i].download()
			else:
				print('Invalid input, try again.')
		else:
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
