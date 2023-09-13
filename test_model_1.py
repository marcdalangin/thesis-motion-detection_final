import tensorflow as tf
import cv2
import numpy as np
import keras
import os

# Load your trained model (Latest trained model should be used here)
model = keras.models.load_model('model/trained_model_0903v2.h5')

# Define the class labels for hand gestures
CATEGORIES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to preprocess a single input image
def preprocess_image(image):
    # Resize the image to the input shape of the model
    image = cv2.resize(image, (28, 28))
    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Normalize the image
    image = image.astype('float32') / 255.0
    return image

# Function to predict hand gestures for multiple images
def predict_hand_gestures(images):
    predictions = []

    for image in images:
        # Preprocess the image
        processed_image = preprocess_image(image)
        # Make the prediction
        prediction = model.predict(np.array([processed_image]))
        # Get the predicted class index
        predicted_class_index = np.argmax(prediction)
        # Get the predicted class label
        predicted_class_label = CATEGORIES[predicted_class_index]
        # Get the confidence score of the prediction
        confidence = prediction[0][predicted_class_index]
        predictions.append((predicted_class_label, confidence))

    return predictions

# Directory containing validation dataset images
validation_dir = 'custom_dataset/'

# Initialize lists to store correct labels and user input images
correct_labels = []
user_input_images = []

# Loop through the subdirectories (one for each class) in the validation directory
for category in CATEGORIES:
    category_dir = os.path.join(validation_dir, category)
    
    # Loop through all image files in the current category directory
    for filename in os.listdir(category_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load and preprocess the image
            image_path = os.path.join(category_dir, filename)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (28, 28))
            user_input_images.append(image)
            correct_labels.append(category)

# Predict hand gestures for all user input images
predicted_labels_and_confidences = predict_hand_gestures(user_input_images)

# File to save the results
output_file = 'results_custom_dataset.txt'

# Open the file for writing
with open(output_file, 'w') as f:
    # Write the predicted labels, correct labels, and confidences to the file
    for i, (predicted_label, confidence) in enumerate(predicted_labels_and_confidences):
        correct_label = correct_labels[i]
        confidence_percentage = f'{confidence * 100:.2f}%'
        result_line = f'Image {i + 1}: Predicted Gesture: {predicted_label}, Correct Gesture: {correct_label}, Confidence: {confidence_percentage}\n'
        f.write(result_line)

    # Write the average confidence rate to the file
    average_confidence = np.mean([confidence for _, confidence in predicted_labels_and_confidences])
    average_confidence_percentage = f'{average_confidence * 100:.2f}%'
    f.write(f'Average Confidence Rate: {average_confidence_percentage}\n')

print(f'Results saved to {output_file}')
