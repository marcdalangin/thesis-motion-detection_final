import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# Load the trained model
model = tf.keras.models.load_model('edensenet.h5')

# Specify the layer names of the desired dense blocks
dense_block_layers = ['conv2d_5']  # Example dense block layer names

# Create a feature extraction model
feature_extraction_model = tf.keras.Model(
    inputs=model.input,
    outputs=[model.get_layer(name).output for name in dense_block_layers]
)

# Prepare input data (assuming you have x_test and y_test)
DATADIR = "train_dataset"
CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Function to load and preprocess the images
def load_images(directory):
    x_data = []
    for category in os.listdir(directory):
        path = os.path.join(directory, category)
        class_label = int(category)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv2.imread(img_path, cv2.COLOR_BGR2RGB)
            img_array = cv2.resize(img_array, (28, 28))
            x_data.append(img_array)
    x_data = np.array(x_data)
    x_data = x_data.astype("float32") / 255.0
    x_data = np.repeat(x_data, 3, axis=-1)  # Repeat grayscale image to create 3 channels
    return x_data


# Load the images
x_test = load_images(DATADIR)

# Pass the input through the feature extraction model
feature_maps = feature_extraction_model.predict(x_test)


# Visualize the feature maps
for i, feature_map_set in enumerate(feature_maps):
    print(f'Feature maps for dense block {i+1}:')
    for j, feature_map in enumerate(feature_map_set):
        print(f'Feature map {j+1}:')
        plt.imshow(feature_map[ :, 0], cmap='gray')
        plt.title(f'Feature map {j+1}')
        plt.colorbar()
        plt.show()

