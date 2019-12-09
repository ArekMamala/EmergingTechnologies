import PIL

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

mnist = tf.keras.datasets.mnist  # 28x 28 image of hand written didgits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# scales values from 0 - 1 makes itg easier for network to learn
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# creating a model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
# 2 hidden layers
model.add(tf.keras.layers.Dense(392, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(392, activation=tf.nn.relu))
# output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)
model.summary()

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()
print(x_train[0])


model.save('AreksModel.model')
new_model = tf.keras.models.load_model('AreksModel.model')
predictions = new_model.predict(x_test)
print(f"xtest Lenght =  { len(x_test) }")
print(f"xtest Lenght of [0][0] =  { len(x_test[0][0]) }")
print(f'Image shape: {x_test.shape}')
print(f'Image shape: {x_test.shape[0]}')

print(predictions)


# tests on model
i=0
for i in range(3):
    print(np.argmax(predictions[i]))
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.show()
    i=i+1


print(np.argmax(predictions[3]))
plt.imshow(x_test[3], cmap=plt.cm.binary)
plt.show()


