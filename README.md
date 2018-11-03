# CS322-Project
Project repository for Maynooth final year module CS322, Music Programming. The outline of this project is to get song lyrics using a RNN by feeding a catalog of song lyrics of a particular artist. Note this project is a WIP 


## How to run
First you must have python 3 installed and flask installed ```python -m pip install flask```

  1. Change directory to flask folder ```cd flask```
  2. Run flask application ```python app.py```
  3. App should be running on localhost:5000

## How to run lyrics retrival
The lyric retrival application will download any given artist library of song lyrics. This application uses the genuis.com api to get lyrics. To run:
  1. Change directory to lyrics_retrival folder ```cd lyrics_retrival```
  2. Change last line of ```scape_lyrics.py``` to artists you want to download 
  E.g  ```x = ScapeLyrics('the beatles')```
  3. Application will stored compiled text file of lyrics to the ```lyrics``` folder
