from textgenrnn import textgenrnn
from keras import backend as K
def generate(artist):
    result = {}
    textgen = textgenrnn(weights_path=f'models/genrnn/{artist}_weights.hdf5',
                        vocab_path=f'models/genrnn/{artist}_vocab.json',
                        config_path=f'models/genrnn/{artist}_config.json')

    textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

    with open('textgenrnn_texts.txt', 'r') as f:
        result['result'] = f.read()
    print(result)
    K.clear_session()
    
    return result


generate('kanye')