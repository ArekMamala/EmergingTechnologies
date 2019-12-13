import PIL
import cv2
import PIL.ImageOps
import PIL.Image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

graph = tf.get_default_graph()

# Reading in the database for images to test
mnist = tf.keras.datasets.mnist
# 28x 28 image of hand written didgits 0-9

# This Load_data() method returns both the training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train = x_train/255
x_test = x_test/255



# the shame of the images
print(x_train.shape)
print(x_test.shape)
# Each image has the dimensions 28 x 28:

# The y_train of the first 10 values
print(y_train[:9 + 1])
tf.reset_default_graph()
model = tf.keras.models.Sequential()# creating a new sequential model


model.add(tf.keras.layers.Dense(28, activation='relu',input_shape=(784,))) # Use input_shape=(28,28) for unflattened data.
model.add(tf.keras.layers.Dense(28, activation='relu'))

# Dropout layer exists to avoid overfitting of model
model.add(tf.keras.layers.Dropout(0.2))

# 10 nuerons in the final layer to coincide with the 10 digits in the MNIST dataset
# softmax maps output to a [0,1] range, it is for probability distribution
model.add(tf.keras.layers.Dense(10, activation='softmax'))


# sparse_categorical_crossentropy loss needed in case we have an integer-dependent variable
# using the adam optimizer
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model using the .fit() method
# Epoch is the amout of time it goes throug this
model.fit(x_train, y_train, batch_size=10, epochs=2, verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
model.summary()

# Saving the Model as AreksModel.model
model.save('AreksModel.h5')
# Loading the saved model
# Save it in a variable new_model
new_model = tf.keras.models.load_model('AreksModel.h5')
predictions = new_model.predict(x_test)
print(predictions)

plt.imshow(x_test[77].reshape(28, 28), cmap="gray")
plt.show()

# Returns normalized output for each digit and also uses argmax to return the actual prediction
# print(loadedModel.predict(test_img[77:78])
"Predicted digit: ", np.argmax(new_model.predict(x_test[77:78]))
print(np.argmax(new_model.predict(x_test[77:78])))


Height = 28
Width = 28
size = Height, Width

originalImage = PIL.Image.open("drawnNumber.png")
newImage = PIL.ImageOps.fit(originalImage, size, PIL.Image.ANTIALIAS)

newImage.save("resized.png")
cv2Image = cv2.imread("resized.png")

grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)

#
grayImage = tf.keras.utils.normalize(grayImage, axis=1)
print(f"gray image Lenght =  {len(grayImage)}")
print(f"gray image Lenght [0] =  {len(grayImage[0])}")

grayImageArray = np.array(grayImage, dtype=np.float32).reshape(1, 784)
grayImageArray /= 255

print(f'Image shape: {grayImage.shape}')

# prediction = model.predict(grayImage)
# print(prediction)

setPrediction = new_model.predict(grayImageArray)
getPrediction = np.array(setPrediction[0])
prediction = model.predict(grayImageArray)

predictedNumber = str(np.argmax(getPrediction))

print(f"prediction of drawing ====  { predictedNumber }")

# checking the length of x_test
print(f"xtest Lenght =  {len(x_test)}")
# checking the length of x_test [0]
print(f"xtest Lenght of [0] =  {len(x_test[0])}")
# checking the length of x_test [0][0]
#print(f"xtest Lenght of [0][0] =  {len(x_test[0][0])}")
# the test image shape
print(f'Image shape: {x_test.shape}')
# the test image shape value
print(f'Image shape: {x_test.shape[0]}')
# Testing the model 3 values
i = 0


