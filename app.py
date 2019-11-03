from flask import Flask, render_template, url_for
import keras as kr
import tensorflow as ts

app = Flask(__name__)


@app.route('/', methods=["GET"])
def Canvas():
    return render_template(url_for('cnavas.html'))


if __name__ == '__main__':
    app.run()
