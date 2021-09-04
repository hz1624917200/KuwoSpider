import requests
from bs4 import BeautifulSoup
from requests.utils import dict_from_cookiejar
from retrying import retry

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


@retry(stop_max_attempt_number=3, wait_random_min=3000, wait_random_max=5000)
# self defined requests.get function, before return response, update cookies and CSRF token
def my_get(url: str, params: dict = None):
	response = requests.get(url, params, headers=request_headers, cookies=cookies)
	cookies.update(dict_from_cookiejar(response.cookies))
	if 'kw_token' in cookies:
		request_headers.update({"CSRF": cookies['kw_token']})
	return response


# region Song_Download
# convert a song's rid to uri, using kuwo api
def rid2uri(rid: str) -> str:
	base_url = 'https://www.kuwo.cn/url'
	params = {'format': 'mp3', 'rid': rid,
	'response': 'url', 'type': 'convert_url3', 'br': '128kmp3', 'from': 'web'}

	response = requests.get(base_url, params=params, headers=request_headers)
	return eval(response.content.decode('utf-8'))['url']


# Simple Download function, return mp3 bytes
def download_mp3(url: str) -> bytes:
	try:
		response = my_get(url)
		return response.content
	except requests.ConnectionError:
		print('mp3 downloading error, have tried 3 times, please check your internet connection')
# end region


def search(keyword: str) -> None:
	from Class import Song

	param = {"key": keyword}
	try:
		# Get kw_token and csrf token
		# Without these, music list api will raise error
		base_url = "https://www.kuwo.cn/search/list"
		my_get(base_url, param)

		# Get Music List
		base_url = "https://www.kuwo.cn/api/www/search/searchMusicBykeyWord"
		response = my_get(base_url, param)

		soup = BeautifulSoup(response.text, features="html.parser")

	except requests.ConnectionError:
		print("search error, have tried 3 times, please check your internet connection")


if __name__ == "__main__":
	# uri = rid2uri('3453727')
	# print(uri)
	# download_mp3(uri)

	search("宋东野")
