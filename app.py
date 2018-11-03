
from flask import Flask, render_template
import application_driver


app = Flask(__name__)

driver = application_driver.AppDriver()

@app.route('/')
def hello_world():
    return render_template('HomePage.html')


def get_artists_list():
        artists_list = driver.get_available_artists()
        print(artists_list)


get_artists_list()  

if __name__ == "__main__":
        app.run()
