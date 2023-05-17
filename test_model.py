import tensorflow as tf
import cv2
import numpy as np
import keras


# model = keras.models.load_model('edensenet.h5')

# Define the class labels for hand gestures
# CATEGORIES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# # Function to preprocess the input image
# def preprocess_image(image):
#     # Resize the image to the input shape of the model
#     image = cv2.resize(image, (28, 28))
#     # Convert the image to RGB format
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     # Normalize the image
#     image = image.astype('float32') / 255.0
#     return image


# # Function to predict the hand gesture
# def predict_hand_gesture(image):
#     # Preprocess the image
#     processed_image = preprocess_image(image)
#     # Make the prediction
#     prediction = model.predict(np.array([processed_image]))
#     # Get the predicted class index
#     predicted_class_index = np.argmax(prediction)
#     # Get the predicted class label
#     predicted_class_label = CATEGORIES[predicted_class_index]
#     # Get the confidence score of the prediction
#     confidence = prediction[0][predicted_class_index]
#     return predicted_class_label, confidence

# # Load and process the user input image

# user_input_image = cv2.imread('train_dataset/new/1.jpeg')
# user_input_image = cv2.resize(user_input_image, (28, 28))
# predicted_label, confidence = predict_hand_gesture(user_input_image)

# # Display the predicted label and confidence
# print('Predicted Gesture:', predicted_label)
# print('Confidence:', confidence)

# import numpy as np
# import cv2
# from tensorflow import keras

# Load the trained model
model = keras.models.load_model('edensenet.h5')

# Define the class labels for hand gestures
class_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Function to preprocess the frame
def preprocess_frame(frame):
    # Resize the frame to the input shape of the model
    frame = cv2.resize(frame, (28, 28))
    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Normalize the frame
    frame = frame.astype('float32') / 255.0
    # Expand dimensions to match the input shape of the model
    frame = np.expand_dims(frame, axis=-1)
    return frame

# Function to detect and predict hand gestures from the live video feed
def detect_hand_gestures():
    # Open the video capture device
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video capture device
        ret, frame = cap.read()

        if not ret:
            break

        # Preprocess the frame
        preprocessed_frame = preprocess_frame(frame)

        # Make the prediction
        prediction = model.predict(np.array([preprocessed_frame]))
        # Get the predicted class index
        predicted_class_index = np.argmax(prediction)
        # Get the predicted class label
        predicted_class_label = class_labels[predicted_class_index]

        # Display the predicted label on the frame
        cv2.putText(frame, predicted_class_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Hand Gesture Detection', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture device and close the windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to detect and predict hand gestures
detect_hand_gestures()
