from tkinter import *
from PIL import Image, ImageDraw
from flask import Flask
from flask import render_template
from gevent.pywsgi import WSGIServer


app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    title='Desktop app'
    return render_template('index.html',title=title)

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('localhost', 8000), app)
    http_server.serve_forever()