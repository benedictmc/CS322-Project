import os 
import use_model as generate
class AppDriver():
    SQUENCE_LENGTH = 40
    def __init__(self):
        pass

    def get_available_artists(self):
        artist_list = ['Kanye West', 'The Beatles']
        return artist_list
    
    def predict_lyrics(self, artist, sample):
        return generate.generate(artist)
