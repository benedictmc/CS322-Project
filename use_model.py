from textgenrnn import textgenrnn
from keras import backend as K


def generate(artist):
    result = {}
    textgen = textgenrnn(weights_path=f'models/genrnn/{artist}/{artist}_weights.hdf5',
                        vocab_path=f'models/genrnn/{artist}/{artist}_vocab.json',
                        config_path=f'models/genrnn/{artist}/{artist}_config.json')

    textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

    with open('textgenrnn_texts.txt', 'r') as f:
        result['result'] = f.read()
    # print(result['result'])
    print(result['result'].upper().find(result['result'].upper()))
    for i,c enumerate(result['result']):
        if c.isupper():
         i-1
    K.clear_session()
    
    return result


generate('kanye')