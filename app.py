import numpy as np
import tensorflow as tf

# PIL (Python Image Library)
import PIL.ImageOps
import PIL.Image
import cv2
import base64
import flask as flask

app = flask.Flask(__name__)

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


    #grayImage = tf.keras.utils.normalize(grayImage)
    print(f"gray image Lenght =  {len(grayImage)}")
    print(f"gray image Lenght [0] =  {len(grayImage[0])}")

    grayImageArray = np.array(grayImage, dtype=np.float32).reshape(1, 784)
    grayImageArray /= 255

    print(f'Image shape: {grayImage.shape}')

    # prediction = model.predict(grayImage)
    # print(prediction)

    model = tf.keras.models.load_model('AreksModel.h5')
    #model.summary()

    setPrediction = model.predict(grayImageArray)
    getPrediction = np.array(setPrediction[0])
   # prediction = model.predict(grayImageArray)

    predictedNumber = str(np.argmax(getPrediction))

    print(f"prediction of drawing ====  {predictedNumber}")

    return predictedNumber


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)