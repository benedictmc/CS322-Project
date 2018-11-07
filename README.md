# CS322-Project
Project repository for Maynooth final year module CS322, Music Programming. The outline of this project is to get song lyrics using a RNN by feeding a catalog of song lyrics of a particular artist. Note this project is a WIP 


## How to run
First you must have python 3 installed and flask installed ```python -m pip install flask```

  1. Run flask application ```python app.py```
  2. App should be running on localhost:5000

## How to run angular application
To develop on the angular application you must first have npm and node installed. Then install the angular cli: 
  - ```npm install -g @angular/cli```

  1. Change directory to the angular application ```cd angular_app\```
  2. Run npm install (May take a few minutes) ```npm install```
  3. Run the application ```npm run ng serve```
  4. Application should be running on localhost:4200

## How to run lyrics retrival
The lyric retrival application will download any given artist library of song lyrics. This application uses the genuis.com api to get lyrics. To run:
  1. Change directory to lyrics_retrival folder ```cd lyrics_retrival```
  2. Change last line of ```scape_lyrics.py``` to artists you want to download 
  E.g  ```x = ScapeLyrics('the beatles')```
  3. Application will stored compiled text file of lyrics to the ```lyrics``` folder
