from Network import rid2uri, Download_mp3
from os.path import exists, expanduser


class Song:
	default_download_path = '{}/Music/'.format(expanduser('~'))

	def __init__(self, title: str, rid: str, singer: str, introduction: str) -> None:
		self.title = title
		self.rid = rid
		self.singer = singer
		self.introduction = introduction

	def download(self, path=default_download_path) -> None:

		mp3_data = Download_mp3(rid2uri(self.rid))
		full_name = '{}{}.mp3'.format(Song.default_download_path, self.title)
		if exists(full_name):
			if not input('File {}.mp3 already exists, overwrite it(y/n y)?') in ['n', 'no']:
				return
		with open('{}'.format(full_name), 'wb') as f:
			f.write(mp3_data)
		print("Downloading success, file saved to {}".format(full_name))


if __name__ == "__main__":
	test_song = Song('安河桥', '3453727', '宋东野', '')
	test_song.download()
