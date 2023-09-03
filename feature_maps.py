import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model, Model
import cv2

# Load the trained model
model = load_model('model/trained_model_0903.h5')

# Define the layer from which you want to visualize feature maps
layer_name = 'dense '  # Change this to the desired layer name

# Create a new model that outputs the feature maps of the selected layer
visualization_model = Model(inputs=model.input, outputs=model.get_layer(layer_name).output)

# Load and preprocess an example image for visualization
example_image_path = 'validation_dataset/1/Sign_1_25.png'
example_image = cv2.imread(example_image_path)
example_image = cv2.resize(example_image, (28, 28))
example_image = cv2.cvtColor(example_image, cv2.COLOR_BGR2RGB)
example_image = example_image.astype('float32') / 255.0
example_image = np.expand_dims(example_image, axis=0)  # Add batch dimension

# Get the feature maps for the example image
feature_maps = visualization_model.predict(example_image)

# Number of feature maps in the selected layer
num_feature_maps = feature_maps.shape[-1]

# Create a grid to display the feature maps
rows = num_feature_maps // 8  # Adjust the number of rows and columns as needed
cols = 8
plt.figure(figsize=(16, 16))

# Plot each feature map
for i in range(num_feature_maps):
    plt.subplot(rows, cols, i + 1)
    plt.imshow(feature_maps[0, :, :, i], cmap='viridis')  # Change the colormap as desired
    plt.axis('off')

# Save the visualization as a .jpg file
plt.savefig('visualization/flatten_visualization_sign-1-25.jpg', bbox_inches='tight')

# Display the visualization
plt.show()

