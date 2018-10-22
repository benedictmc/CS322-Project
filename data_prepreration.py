import json


class Preprocess():
    def __init__(self):
        song_list = []
        with open('kanye_songs.json') as f:
            self.data = json.load(f)

        for song_key in list(self.data):
            song = self.data[song_key]
            line_list = song.split('\n')
            remove_tag = [line for line in line_list if '[' not in line]
            remove_empty = [line for line in remove_tag if '' != line]
            song_list.append(' '.join(remove_empty))
        print(' '.join(song_list))

        

        text_file = open("kanye_songs.txt", "w",  encoding="utf-8")
        text_file.write(' '.join(song_list))
        text_file.close()

x = Preprocess()