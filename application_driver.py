import os 

class AppDriver():
    
    def __init__(self):
        self.get_available_artists()


    def get_available_artists(self):
        list_ = os.listdir('lyrics_retrival\lyrics')
        artist_list = ['Kanye West', 'The Beatles']
        return artist_list
    
