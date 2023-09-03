import tensorflow as tf
import cv2
import numpy as np
import keras

# Load your trained model
model = keras.models.load_model('model/trained_model_0903.h5')

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

# Load and process multiple user input images
image_paths = [
    'validation_dataset/0/Sign_0_54.png',
    'validation_dataset/1/Sign_1_25.png',
    'validation_dataset/2/IMG_4101.JPG',
    # Add more image paths as needed
]

user_input_images = [cv2.imread(image_path) for image_path in image_paths]
user_input_images = [cv2.resize(image, (28, 28)) for image in user_input_images]
predicted_labels_and_confidences = predict_hand_gestures(user_input_images)

# Display the predicted labels and confidences for each image
for i, (predicted_label, confidence) in enumerate(predicted_labels_and_confidences):
    print(f'Image {i + 1}: Predicted Gesture: {predicted_label}, Confidence: {confidence}')
