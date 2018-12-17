import json

class CompileLyrics():
    def __init__(self, filename, artist):
        print('Loading preprocess script...')
        print(f'Opening file {filename} ...')

        song_list = []
        with open(filename) as f:
            self.data = json.load(f)

        for song_key in list(self.data):
            song = self.data[song_key]
            # line_list = song.split('\n')
            # remove_tag = [line for line in line_list if '[' not in line]
            # remove_empty = [line for line in remove_tag if '' != line]
            song_list.append(song)
        print(f'Done now saving to {filename} ...')

        artist = artist.replace(' ', '_')
        text_file = open(f"lyrics/{artist}_songs.txt", "w",  encoding="utf-8")
        text_file.write(' '.join(song_list))
        text_file.close()
        print(f'Finished.')

