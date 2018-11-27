
from flask import Flask, render_template, jsonify, request
import application_driver
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

driver = application_driver.AppDriver()

@app.route('/API/artists')
def get_artists_list():
        artists_list = driver.get_available_artists()
        return jsonify(artists_list)

@app.route('/API/post-artists', methods=['POST'])
def post_artists():
        print('Post artists triggered...')
        if request.method == 'POST':  
                json_payload = request.get_json()
        print(json_payload.keys())
        return 'works'

if __name__ == "__main__":
        app.run()




 
