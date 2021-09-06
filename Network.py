import requests
from requests.utils import dict_from_cookiejar
from retrying import retry
import json

from typing import List

import Class

# request headers from edge(chromium)

request_headers_raw = '''Pragma: no-cache
Cache-Control: no-cache
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 \
Safari/537.36 Edg/92.0.902.84
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.kuwo.cn/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: close'''

# build request headers from raw data
request_headers = {}
for line in request_headers_raw.split('\n'):
	key, value = line.split(': ')
	request_headers[key] = value
# print(request_headers)
cookies = {}


# self defined requests.get function, before return response, update cookies and CSRF token
@retry(stop_max_attempt_number=3, wait_random_min=3000, wait_random_max=5000)
def my_get(url: str, params: dict = None):
	try:
		init_url = 'https://www.kuwo.cn/'
		if cookies == {} and url != init_url:
			my_get(init_url)
		response = requests.get(url, params, headers=request_headers, cookies=cookies)
		cookies.update(dict_from_cookiejar(response.cookies))
		if 'kw_token' in cookies:
			request_headers.update({"CSRF": cookies['kw_token']})
		return response
	except ValueError as e:
		# print(e.args)
		if e.args[0] == "check_hostname requires server_hostname":
			print('Proxy setting error, please check your network settings')


# region Song_Download
# convert a song's rid to uri, using kuwo api
def rid2uri(rid: str) -> str:
	base_url = 'https://www.kuwo.cn/url'
	params = {'format': 'mp3', 'rid': rid,
	'response': 'url', 'type': 'convert_url3', 'br': '128kmp3', 'from': 'web'}

	response = requests.get(base_url, params=params, headers=request_headers)
	url = json.loads(response.text).get('url', '')
	return url


# Simple Download function, return mp3 bytes
def download_mp3(url: str) -> bytes:
	if url == '':
		print("url error, please try again")
		return b''
	try:
		response = my_get(url)
		return response.content
	except requests.ConnectionError:
		print('mp3 downloading error, have tried 3 times, please check your internet connection')
# end region


@retry(stop_max_attempt_number=2)
def search(keyword: str, start: int = 1) -> (List[Class.Song], int):
	"""

	:param keyword: search keyword
	:param start: start of return index, if first search, leave it default
	:return: List[Class.song]: list of search result, int: length of all result
	"""
	from Class import Song

	# Get only top 30 records
	param = {"key": keyword, 'pn': str(start), 'rn': str(start + 29)}
	try:
		# We use a stronger and robuster handling system in my_get
		# # Get kw_token and csrf token
		# # Without these, music list api will raise error
		# base_url = "https://www.kuwo.cn/search/list"
		# my_get(base_url, param)

		# Get Music List
		base_url = "https://www.kuwo.cn/api/www/search/searchMusicBykeyWord"
		response = my_get(base_url, param)

		# get data and convert search list to a dict
		search_list = json.loads(response.text)['data']
		# print(search_list['list'][0])
		# print(search_list['list'][-1])
		# print(len(search_list['list']))

		song_list = []
		for record in search_list['list']:
			# Create a new Song instance
			song = Song(record['name'], record['musicrid'].split('_')[-1], record['artist'],
			record['album'], duration=int(record['duration']))

			# This song is not free
			if record['payInfo']['play'] == '1111':
				song.free = False

			song_list.append(song)

		# # For Debug
		# for i in song_list:
		# 	print(i)
		return song_list, search_list['total']
	except requests.ConnectionError:
		print("search error, have tried 3 times, please check your internet connection")


def fill_rank_list() -> List[Class.RankList]:
	from Class import RankList

	base_url = 'https://www.kuwo.cn/api/www/bang/bang/bangMenu?httpsStatus=1'
	response = my_get(base_url)
	if not response:
		exit(0)

	res_list = []
	rank_list_json = json.loads(response.text)['data']
	for parent_rank_lists in rank_list_json:
		parent_rank_name = parent_rank_lists['name']
		for rank in parent_rank_lists['list']:
			temp_rank_list = RankList(rank['name'], rank['sourceid'], parent_rank_name)
			res_list.append(temp_rank_list)

	return res_list


if __name__ == "__main__":
	# uri = rid2uri('3453727')
	# print(uri)
	# download_mp3(uri)

	# # None-Free Song can also downloaded
	# uri = rid2uri('325842')
	# print(uri)

	# search("宋东野")
	# search("Taylor Swift")

	fill_rank_list()
