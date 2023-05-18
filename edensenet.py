import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.utils import to_categorical
from keras.utils import plot_model
from keras.callbacks import TensorBoard
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from IPython.display import Image
from ann_visualizer.visualize import ann_viz

# Model / data parameters
num_classes = 10  # Number of classes in your dataset
input_shape = (28, 28, 3)
batch_size = 16
epochs = 50
DATADIR = "rgb_mixed_dataset"
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
            # print(img_array)
            x_data.append(img_array)
            y_data.append(class_label)

    x_data = np.array(x_data)
    y_data = np.array(y_data)

    return x_data, y_data

x_train, y_train = load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255

# Make sure images have shape (28, 28, 3)
# x_train = np.expand_dims(x_train, -1)
# x_train = np.repeat(x_train, 3, axis=-1)

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")

# Convert class vectors to binary class matrices
y_train = to_categorical(y_train, num_classes)

# Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

print(x_test.shape[0], "test samples")

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        # First Conv2D layer
        layers.Conv2D(64, kernel_size=(3, 3), padding='same'),
        # First Dense block (BN-ReLU-Conv2D x 2)
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(64, kernel_size=(3, 3), padding='same'),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(64, kernel_size=(3, 3), padding='same'),
        layers.Dropout(0.3),
        # First transition layer
        layers.Conv2D(64, kernel_size=(1, 1), padding='same'),
        layers.Conv2D(64, kernel_size=(3, 3), padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        # Second Dense block (BN-ReLU-Conv2D x 2)
        layers.Conv2D(128, kernel_size=(3, 3), padding='same'),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(128, kernel_size=(3, 3), padding='same'),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(128, kernel_size=(3, 3), padding='same'),
        layers.Dropout(0.4),
        # Second transition layer
        layers.Conv2D(128, kernel_size=(1, 1), padding='same'),
        layers.Conv2D(128, kernel_size=(3, 3), padding='same'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        # Third Dense block (BN-ReLU-Conv2D x 2)
        layers.Conv2D(256, kernel_size=(3, 3), padding='same'),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(256, kernel_size=(3, 3), padding='same'),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Conv2D(256, kernel_size=(3, 3), padding='same'),
        layers.Dropout(0.5),
        # Third transition layer
        layers.Conv2D(256, kernel_size=(1, 1), padding='same'),
        layers.Conv2D(256, kernel_size=(3, 3), padding='same'),
        layers.GlobalAveragePooling2D(),
        # Final Dense layer
        layers.Dense(128),
        layers.BatchNormalization(),
        layers.Activation("relu"),
        layers.Dropout(0.5),

        layers.Dense(num_classes, activation="softmax"),
    ]
)



# Train the model
model.summary()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,  callbacks=[tensorboard])
score = model.evaluate(x_test, y_test, verbose=0)
model.save('edensenet.h5')
# plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True, show_trainable=True)
# # Image(filename='model.png')
# # ann_viz(model, filename='edensenet.gv',  title="Enhanced Dense Convolutional Neural Network")

print("Test loss:", score[0])
print("Test accuracy:", score[1])