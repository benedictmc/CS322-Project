from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path='colaboratory_weights.hdf5',
                       vocab_path='colaboratory_vocab.json',
                       config_path='colaboratory_config.json')

# x = textgen.generate_to_file(4, temperature=1.0)
textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)

with open('textgenrnn_texts.txt', 'r') as f:
    x = f.read()
print(x)