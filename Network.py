import requests

# request headers from edge(chromium)
request_headers_raw = '''Pragma: no-cache
Cache-Control: no-cache
Sec-Ch-Ua: "Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84
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
		response = requests.get(url, headers=request_headers)
		return response.content
	except:
		print('mp3 downloading error.')


if __name__ == "__main__":
	uri = rid2uri('3453727')
	print(uri)
	download_mp3(uri)
