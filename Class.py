from os.path import exists, expanduser


class Song:
	default_download_path = '{}/Music/'.format(expanduser('~'))

	# Instance initialize
	def __init__(self, title: str, rid: str, singer: str, album: str, introduction: str) -> None:
		self.title = title
		self.rid = rid
		self.singer = singer
		self.album = album
		self.introduction = introduction

	# Download a song, including uri searching and downloading
	def download(self, path=default_download_path) -> None:
		from Network import rid2uri, download_mp3

		mp3_data = download_mp3(rid2uri(self.rid))
		if mp3_data == b'':
			return
		full_name = '{}{}.mp3'.format(path, self.title)
		if exists(full_name):
			if not input('File {}.mp3 already exists, overwrite it(y/n y)?') in ['n', 'no']:
				return
		with open('{}'.format(full_name), 'wb') as f:
			f.write(mp3_data)
		print("Downloading success, file saved to {}".format(full_name))


# Class function test
if __name__ == "__main__":
	test_song = Song('安河桥', '3453727', '宋东野', '安河桥北', '')
	test_song.download()
