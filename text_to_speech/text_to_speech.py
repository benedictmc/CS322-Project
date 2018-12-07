
from gtts import gTTS
from pygame import mixer
import os 
import pygame.mixer


# adele_sample= "hello, it's me I was wondering if after all these years you'd like to meet To go over everything They say that time's supposed to heal ya, but I ain't done much healing Hello, can you hear me? I'm in California dreaming about who we used to be When we were younger and free I've forgotten how it felt before the world fell at our feet There's such a difference between us And a million miles Hello from the other side I must've called a thousand times To tell you, I'm sorry for everything that I've done But when I call, you never seem to be home Hello from the outside At least, I can say that I've tried To tell you, I'm sorry for breaking your heart But it don't matter,"
# tts = gTTS(text=adele_sample, lang='en', slow=False)
# tts.save("adele.mp3")


background = 'adele-background.mp3'
backtrack = 'adele.mp3'


for filename in os.listdir("/Users/muznaalrasheed/Desktop/CS322/CS322-Project"):
    if filename.endswith(".mp3"):
        file = filename

pygame.init()
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(30000)

        