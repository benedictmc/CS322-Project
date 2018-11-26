
from flask import Flask, render_template, jsonify
import application_driver
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

driver = application_driver.AppDriver()

@app.route('/')
def hello_world():
    return render_template('HomePage.html')

@app.route('/API/artists')
def get_artists_list():
        artists_list = driver.get_available_artists()
        return jsonify(artists_list)

# TODO Need to finsihed
@app.route('/API/post-artists', methods=['POST'])
def post_generated_lyrics():
        print(request.data)
        generated_lyrics = ['this', 'is' ,'sample' ,'generated', 'lyrics']
        return jsonify(generated_lyrics)



# @app.route('/API/samples/<id>')
# def get_artists_list(id):
#         samples = []
#         # if id == 'the_beatles':
#         #         samples = ['I am he as you are he as you are me and we are all together','A crowd of people stood and stared Theyd seen his face ', 'When I think of love as something new']
#         # if id == 'kanye':
#         #         samples = ['So your Duncan Hines is irrelevant, woo ','''Don't sell me apartment, I'll move in the lobby''', '''' I wanna wake up with you in my... Beautiful mornin'''']
#         # else:
#         #         samples = f'Error artist with {id} not found.'
#         return jsonify(samples)      

if __name__ == "__main__":
        app.run()


@app.route('/form-example', methods=['POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        sample = request.form.get('sample')
        artist = request.form['artist']
        print(sample)
        print(artist)

 
