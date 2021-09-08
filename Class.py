import json
from os.path import exists, expanduser
from typing import List


class Song:
	default_download_path = '{}/Music/'.format(expanduser('~'))

	# Instance initialize
	def __init__(self, title: str, rid: str, singer: str = '', album: str = '',
	introduction: str = '', is_free: bool = True, duration: int = 0) -> None:
		self.title = MyString.web_replace(title)
		self.rid = MyString.web_replace(rid)
		self.singer = MyString.web_replace(singer)
		self.album = MyString.web_replace(album)
		self.introduction = MyString.web_replace(introduction)
		self.free = is_free
		self.duration = duration

	def __str__(self):
		import time
		# title, if non-free, will add '*' after title
		s = MyString.chinese_format(self.title + ('' if self.free else '*'), 15)
		s += MyString.chinese_format(self.singer, 7)
		s += MyString.chinese_format(self.album, 7)
		# s = '{:{space}<15}'.format(Chinese.format(self.title) + ('' if self.free else '*') + ' ',
		# space=Chinese.full_len_space)
		# s += '{:{space}<7}'.format(Chinese.format(self.singer) + ' ', space=Chinese.full_len_space)  # singer
		# s += '{:{space}<7}'.format(Chinese.format(self.album) + ' ', space=Chinese.full_len_space)  # album

		# has duration
		if self.duration != 0:
			s += time.strftime('%H:%M:%S' if self.duration >= 3600 else '%M:%S', time.gmtime(self.duration))
		return s

	# Get main page's url of a song
	def page_url(self) -> str:
		base_url = 'https://www.kuwo.cn/play_detail/'
		return base_url + self.rid

	# Download a song, including uri searching and downloading
	def download(self, path=default_download_path, index: int = 0) -> None:
		from Network import rid2uri, download_mp3

		mp3_data = download_mp3(rid2uri(self.rid))
		if mp3_data == b'':
			return

		index_str = f'({index})' if index > 1 else ''
		full_name = f'{path}{self.title}{index_str}.mp3'
		if exists(full_name):
			if not input('File {}.mp3 already exists, overwrite it(y/n n)?'.format(self.title)) in ['y', 'yes']:
				# rename the download name
				i = 2
				while exists('{}{}({}).mp3'.format(path, self.title, i)):
					i += 1
				full_name = '{}{}({}).mp3'.format(path, self.title, i)
		with open('{}'.format(full_name), 'wb') as f:
			f.write(mp3_data)
		print("Downloading success, file saved to {}".format(full_name))


class RankList:
	def __init__(self, name: str, lid: str, parent: str):
		self.name = name
		self.lid = lid
		self.parent = parent

	def __str__(self):
		s = MyString.chinese_format(self.name, 15)
		s += self.parent
		return s


class MyString:
	full_len_space = chr(12288)

	def chinese_format(s: str, length: int) -> str:
		alpha_count = 0
		for i in s:
			# if i != ' ' and ord(i) < 128:
			if ord(i) < 128:
				alpha_count += 1
		return '{:{space}<{length}} '.format(s, space=MyString.full_len_space, length=length) + \
			' ' * (alpha_count // 2 + 1) + '\t'

	def web_replace(s: str) -> str:
		replace_dict = {'&nbsp;': MyString.full_len_space, '&apos;': '\''}
		temp_s = s
		for i in replace_dict:
			temp_s = temp_s.replace(i, replace_dict[i])
		return temp_s


# Class of word cloud, 1 instance when running program
class WordCloud:
	def __init__(self):
		if exists('word_cloud'):
			with open('word_cloud', 'r') as f:
				self.dict = json.loads(f.read())
		else:
			self.dict = {}

	def update(self, rank_lists: List[RankList]) -> None:
		import Network
		from jieba.analyse import extract_tags
		import time
		import random
		"""
		update word lists

		:return:
		"""
		print("Database Updating...")
		start = time.time()
		random.seed(start)

		# only randomly select one rank list in rank_lists
		rank_list = random.choice(rank_lists)
		song_list, _ = Network.search_by_list(rank_list)
		for song, ind in zip(song_list, range(len(song_list))):
			introduction = Network.get_introduction(song.rid)
			if introduction:
				tags = extract_tags(introduction, 5)
				# print(tags)

				for tag in tags:
					self.dict[tag] = self.dict.get(tag, 0) + 1

			# Progress Bar
			rate_progress = round((ind + 1) / len(song_list) * 100)
			print("{:3}%[".format(rate_progress), end='')
			print("{:-<50}".format('*' * (rate_progress // 2)), end='')
			print("]{:.2f}s".format(time.time() - start), end='\r')
			time.sleep(0.01)
		print('\nDatabase updated successfully!')


# Class function test
if __name__ == "__main__":
	# test_song = Song('安河桥', '3453727', '宋东野', '安河桥北', '')
	# test_song = Song('我不难过', '95769')
	# test_song.download()
	pass
