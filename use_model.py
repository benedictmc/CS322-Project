from textgenrnn import textgenrnn
from keras import backend as K
import json

artist_map = {
    "Kanye West" : "kanye",
    "The Beatles" : "the_beatles",
    "Arctic Monkeys" : "arctic_monkeys",
    "Taylor Swift" : "taylor_swift"
}

def generate(artist):
    data = {}
    artist = artist_map[artist]
    print("*******************")
    textgen = textgenrnn(weights_path=f'models/genrnn/{artist}/{artist}_weights.hdf5',
                        vocab_path=f'models/genrnn/{artist}/{artist}_vocab.json',
                        config_path=f'models/genrnn/{artist}/{artist}_config.json')

    textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

    with open('textgenrnn_texts.txt', 'r') as f:
       data['result'] = f.read()
    K.clear_session()
    return data


print('Starting generating samples...')
generate_list = ['Kanye West', "The Beatles", "Arctic Monkeys", "Taylor Swift"]
for artist in generate_list:
    print(f'Generating samples for {artist}...')
    sample_dict = {artist: []}
    for i in range(10):
        sample_dict[artist].append(generate(artist))
    with open(f'sample_folder/{artist}.json', 'w') as f:
        json.dump(sample_dict, f)
    print(f'Done for {artist}...')
    