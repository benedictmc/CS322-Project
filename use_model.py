from textgenrnn import textgenrnn

def generate():
    result = {}
    textgen = textgenrnn(weights_path='models/genrnn/colaboratory_weights.hdf5',
                        vocab_path='models/genrnn/colaboratory_vocab.json',
                        config_path='models/genrnn/colaboratory_config.json')

    textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

    with open('textgenrnn_texts.txt', 'r') as f:
        result['result'] = f.read()
    
    return result
