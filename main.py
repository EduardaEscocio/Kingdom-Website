from flask import Flask, render_template, url_for

import os
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    var = get_image_paths()
    return render_template("index.html", images=var)

@app.route("/saudar")
def ola():
    return "<p> Olá, Mundo!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

def get_image_paths():
    """
    Get the paths of all images in the static/imagens directory.
    """
    image_dir = os.path.join(app.static_folder, 'images')
    image_files = os.listdir(image_dir)
    image_paths = [url_for('static', filename=f'/static/images/{img}') for img in image_files]
    return image_paths
# url_for('static', filename='style.css')