# Default page, will add main script
from typing import List
import pyfiglet

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


#  List rank lists, make user choose one
def list_rank():
	# print('Rank Constructing...')
	global rank_lists

	# rank lists not initialized
	if not rank_lists:
		# rank list is empty, call Network to fill it
		rank_lists = Network.fill_rank_list()
	print_list(rank_lists)

	while True:
		choice = input("select the list you want to view")

		if choice.isnumeric():
			choice_num = int(choice)
			if 1 <= choice_num <= len(rank_lists):
				rank(rank_lists[choice_num - 1])
		else:
			print('Invalid input, try again')


# General list display function
def display_list(song_list: List[Class.Song], res_length: int, page_func=None) -> None:
	"""

	:param song_list: list of songs to display
	:param res_length: the result's full length, for paging
	:param page_func: Page turning function, used to refresh the list, lambda
	:return: None
	"""
	import re

	print_list(song_list)
	start = 1

	# Attention, choice == index + 1
	while True:
		choice = input('choose which you want to download\n (input "q" to return, \
	"d" to pagedown, "u" to pageup, "h" to back head), support section ex "2-5": ')

		# Special keyword
		# quit
		if choice == 'q':
			return
		# pageup
		if choice in 'udh':
			if choice == 'u':
				if start > 1:
					start -= 1
			elif choice == 'd':
				if start < (res_length + 29) // 30:
					start += 1
			elif choice == 'h':
				start = 1
			song_list, res_length = page_func(start)
			print_list(song_list)
			continue

		# download music by id section
		if not choice.isnumeric() or int(choice) > len(song_list) or int(choice) < 1:
			res = re.match(r'\d+-\d+', choice)
			if res:
				(start, end, *_) = res.group().split('-')
				if int(start) < 1 or int(end) > len(song_list) or int(start) > int(end):
					print('Invalid input, try again.')
				else:
					# valid section input, return iterable
					for i in range(int(start) - 1, int(end)):
						song_list[i].download()
			else:
				print('Invalid input, try again.')
		else:
			# single number
			song_list[int(choice) - 1].download()


# Get the specified rank, and display it
def rank(rank_list: Class.RankList) -> None:
	"""

	:param rank_list: RankList object in Class, stands for a rank
	:return: None
	"""
	song_list, res_length = Network.search_by_list(rank_list)
	if not song_list:
		exit(-1)

	display_list(song_list, res_length, lambda page: Network.search_by_list(rank_list, page))


def search(kw: str) -> None:
	"""

	:param kw: search keyword
	:return: None
	"""
	# print("Searching...")

	song_list, res_length = Network.search(kw)
	if not song_list:
		exit(-1)
	display_list(song_list, res_length, lambda page: Network.search(kw, page))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	# print a banner
	print_hi('ZhengHuang and HeQi')

	while True:
		keyword = menu()

		# special keywords
		if keyword == 'quit()':
			print('Bye.')
			exit()
		elif keyword == '':
			hanging_around()
		elif keyword == 'rank()':
			list_rank()
		else:
			# normal keyword search
			search(keyword)
