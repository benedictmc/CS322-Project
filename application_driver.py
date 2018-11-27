import os 

class AppDriver():
    SQUENCE_LENGTH = 40
    def __init__(self):
        pass

    def get_available_artists(self):
        artist_list = ['Kanye West', 'The Beatles']
        return artist_list
    
    def predict_lyrics(self, artist, sample):

        sentence = "The grass is green and my car is red lik"
        sentence = sentence.lower()
        generated = sentence
        # sys.stdout.write(generated)

        for i in range(LYRIC_LENGTH):
            x = np.zeros((1, AppDriver.SQUENCE_LENGTH, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_to_index[char]] = 1.

            predictions = model.predict(x, verbose=0)[0]
            next_index = helper.sample(predictions, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        pass