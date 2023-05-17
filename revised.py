import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.utils import to_categorical
from keras.callbacks import TensorBoard
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Model / data parameters
num_classes = 10  # Number of classes in your dataset
input_shape = (28, 28, 3)
batch_size = 16
epochs = 10
DATADIR = "train_dataset"
CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
NAME = "edensenet{}".format(epochs)
tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))


# Load the data and split it between train and test sets
def load_data():
    x_data = []
    y_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_label = CATEGORIES.index(category)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
            img_array = cv2.resize(img_array, (28, 28))
            plt.imshow(img_array, cmap="gray")
            x_data.append(img_array)
            y_data.append(class_label)

    x_data = np.array(x_data)
    y_data = np.array(y_data)

    return x_data, y_data

x_train, y_train = load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255

# Make sure images have shape (28, 28, 3)
x_train = np.expand_dims(x_train, -1)
x_train = np.repeat(x_train, 3, axis=-1)

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")

# Convert class vectors to binary class matrices
y_train = to_categorical(y_train, num_classes)

# Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

print(x_test.shape[0], "test samples")

def dense_block(input_layer, num_filters, dropout_rate):
    x = layers.BatchNormalization()(input_layer)
    x = layers.Activation("relu")(x)
    x = layers.Conv2D(num_filters, kernel_size=(3, 3), padding='same')(x)
    x = layers.Concatenate()([input_layer, x])  # Concatenate with input layer
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)
    x = layers.Conv2D(num_filters, kernel_size=(3, 3), padding='same')(x)
    x = layers.Concatenate()([input_layer, x])  # Concatenate with input layer
    x = layers.Dropout(dropout_rate)(x)
    return x


model = keras.Sequential()
model.add(keras.Input(shape=input_shape))
model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='same'))
model.add(dense_block(model.layers[-1], 64, 0.3))
model.add(layers.Conv2D(64, kernel_size=(1, 1), padding='same'))
model.add(layers.Conv2D(64, kernel_size=(3, 3), padding='same'))
model.add(layers.AveragePooling2D(pool_size=(2, 2)))
model.add(dense_block(model.layers[-1], 128, 0.4))
model.add(layers.Conv2D(128, kernel_size=(1, 1), padding='same'))
model.add(layers.Conv2D(128, kernel_size=(3, 3), padding='same'))
model.add(layers.AveragePooling2D(pool_size=(2, 2)))
model.add(dense_block(model.layers[-1], 256, 0.5))
model.add(layers.Conv2D(256, kernel_size=(1, 1), padding='same'))
model.add(layers.Conv2D(256, kernel_size=(3, 3), padding='same'))
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(128))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(num_classes, activation="softmax"))

# Train the model
print(model.summary())

