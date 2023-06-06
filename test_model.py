import tensorflow as tf
import cv2
import numpy as np
import keras


model = keras.models.load_model('edensenet.h5')

# Define the class labels for hand gestures
CATEGORIES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to preprocess the input image
def preprocess_image(image):
    # Resize the image to the input shape of the model
    image = cv2.resize(image, (28, 28))
    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Normalize the image
    image = image.astype('float32') / 255.0
    return image


# Function to predict the hand gesture
def predict_hand_gesture(image):
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
    return predicted_class_label, confidence

# Load and process the user input image

user_input_image = cv2.imread('train_dataset/10/7.jpeg')
user_input_image = cv2.resize(user_input_image, (28, 28))
predicted_label, confidence = predict_hand_gesture(user_input_image)

# Display the predicted label and confidence
print('Predicted Gesture:', predicted_label)
print('Confidence:', confidence)

