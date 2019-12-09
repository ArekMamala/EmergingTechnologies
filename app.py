import numpy as np
import tensorflow as tf

# PIL (Python Image Library)
import PIL.ImageOps
import PIL.Image
import cv2
import base64
import flask as flask

app = flask.Flask(__name__)

model = tf.keras.models.load_model('static/AreksModel.model')
# model = load_model('epic_num_reading.mode-test')

# THE WIDTH AND THE HEIGHT OF THE IMAGES 28pixels
Height = 28
Width = 28
size = Height, Width


@app.route('/')
def index():
    # return 'This is the home page'
    return flask.render_template('canvas.html')


@app.route('/digit', methods=['POST'])
def Image():
    imageB64 = flask.request.values[('imageBase64')]

    decodeImage = base64.b64decode(imageB64[22:])

    with open("drawnNumber.png", "wb") as f:
        f.write(decodeImage)

    originalImage = PIL.Image.open("drawnNumber.png")
    newImage = PIL.ImageOps.fit(originalImage, size, PIL.Image.ANTIALIAS)

    newImage.save("resized.png")

    cv2Image = cv2.imread("resized.png")

    grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)

    grayImage = tf.keras.utils.normalize(grayImage, axis=1)
    print(f"xtest Lenght =  { len(grayImage) }")
    print(f"xtest Lenght [0] =  { len(grayImage[0]) }")
    #print(f"xtest Lenght [0][0] =  { len(grayImage[0][0]) }")

    grayImage = np.array([grayImage])

    print(f'Image shape: { grayImage.shape }')

    prediction = model.predict(grayImage)
    print(prediction)
#grayArray = np.array(grayImage, dtype=np.float32).reshape(1, 784)

#  getPrediction = np.array(setPrediction[0])

#   predictedNumber = str(np.argmax(getPrediction))
#    print(predictedNumber)

    return prediction


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
