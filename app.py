from flask import Flask, render_template, request
from keras.models import load_model
import base64
import numpy as np
import tensorflow as tf

# PIL (Python Image Library)
from PIL import Image, ImageOps
import cv2

app = Flask(__name__)
model = tf.keras.models.load_model('static/epic_num_reading.model-test')

# model = load_model('epic_num_reading.mode-test')

# THE WIDTH AND THE HEIGHT OF THE IMAGES 28pixels
Height = 28
Width = 28
size = Height, Width


@app.route('/home')
def index():
    return app.send_static_file('static/canvas.html')


@app.route('/digit', methods=['GET', 'POST'])
def Image():
    imageB64 = request.values.get("imageBase64", "")

    decodeImage = base64.b64decode(imageB64[22:])

    with open("drawnNumber.png", "wb") as f:
        f.write(decodeImage)

    originalImage = Image.open("drawnNumber.png")
    newImage = ImageOps.fit(originalImage, size)

    newImage.save("resized.png")

    cv2Image = cv2.imread("resizedUserDigit.png")

    grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)

    grayArray = np.array(grayImage).reshape(1, 28, 28, 1)

    setPrediction = model.predict(grayArray)
    getPrediction = np.array(setPrediction[0])

    predictedNumber = str(np.argmax(getPrediction))
    print(predictedNumber)

    return predictedNumber


if __name__ == '__main__':
    app.run(debug=True)
