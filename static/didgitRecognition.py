import PIL

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Reading in the database for images to test
mnist = tf.keras.datasets.mnist
# 28x 28 image of hand written didgits 0-9

# This Load_data() method returns both the training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizing the data
# This scales values from 0 - 1 makes itg easier for network to learn
# For both x_test and x_train
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# printing one of the images from the train set
print(y_train[0])
# getting rid of colour making it black and white
plt.imshow(x_train[0], cmap='Greys')
# printing out image to the screen
plt.show()

# the shame of the images
print(x_train.shape)
print(x_test.shape)
# Each image has the dimensions 28 x 28:

# The y_train of the first 10 values
print(y_train[:9 + 1])

# creating a new sequential model
model = tf.keras.models.Sequential()

# Adding Layers to the model
# Flatten layer to convert into a 1D array
model.add(tf.keras.layers.Flatten())
# 2 hidden dense layers
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# output 4th layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# sparse_categorical_crossentropy loss needed in case we have an integer-dependent variable
# using the adam optimizer
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model using the .fit() method
# Epoch is the amout of time it goes throug this
model.fit(x_train, y_train, batch_size=20, epochs=3, verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
model.summary()

# Saving the Model as AreksModel.model
model.save('AreksModel.model')
# Loading the saved model
# Save it in a variable new_model
new_model = tf.keras.models.load_model('AreksModel.model')
predictions = new_model.predict(x_test)
print(predictions)

# checking the length of x_test
print(f"xtest Lenght =  {len(x_test)}")
# checking the length of x_test [0]
print(f"xtest Lenght of [0] =  {len(x_test[0])}")
# checking the length of x_test [0][0]
print(f"xtest Lenght of [0][0] =  {len(x_test[0][0])}")
# the test image shape
print(f'Image shape: {x_test.shape}')
# the test image shape value
print(f'Image shape: {x_test.shape[0]}')
# Testing the model 3 values
i=0

for i in range(3):
    print(f"prediction = { np.argmax(predictions[i]) }")
# Printing the image after
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.show()
    i = i+1