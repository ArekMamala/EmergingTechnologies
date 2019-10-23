import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist  # 28x 28 image of hand written didgits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# scales values from 0 - 1 makes itg easier for network to learn
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# creating a model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
# 2 hidden layers
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
#print(val_loss, val_acc)

#plt.imshow(x_train[0], cmap=plt.cm.binary)
#plt.show()
#print(x_train[0])

model.save('epic_num_reading.model')
new_model = tf.keras.models.load_model('epic_num_reading.model')
predictions = new_model.predict(x_test)
print(predictions)

i=0
for i in range(1000):
    print(np.argmax(predictions[i]))
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.show()
    i=i+1


print(np.argmax(predictions[3]))
plt.imshow(x_test[3], cmap=plt.cm.binary)
plt.show()
