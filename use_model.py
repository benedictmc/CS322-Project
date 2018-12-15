from textgenrnn import textgenrnn
from keras import backend as K

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