from flask import Flask, render_template

app = Flask(__name__)

artist_list = ['Kanye', 'The Beatles']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home(): 

    return render_template('home.html')

@app.route('    ')
def retrive_songs():
    return str(artist_list)

if __name__ == '__main__':
    app.run(debug=True)