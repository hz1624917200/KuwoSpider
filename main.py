# Default page, will add main script
import pyfiglet


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
	print(f'By {name}.')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	print_hi('ZhengHuang and HeQi')
	# print a banner

