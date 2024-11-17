import cv2
import numpy as np
from collections import deque

import keras

from hand_detection import HandDetector

# Loading the SL model
model = keras.models.load_model('../Sign_Language_Recognition/smnist.h5')

class PredictionSmoother:
    def __init__(self, window_size=5, label_map=None):
        self.window_size = window_size
        self.predictions = deque(maxlen=window_size)
        # Define a mapping from string labels to integer indices
        self.label_map = label_map if label_map else {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
            'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }

    def add_prediction(self, prediction):
        # Convert string prediction to integer index
        if prediction in self.label_map:
            self.predictions.append(self.label_map[prediction])
        else:
            # Handle unexpected prediction
            print(f"Warning: Unexpected prediction '{prediction}'")
            return prediction  # Return original prediction if it's unexpected

        if len(self.predictions) == self.window_size:
            # Apply np.bincount to get the most common prediction
            smoothed_prediction_index = np.bincount(self.predictions).argmax()
            # Reverse map to get the string label
            smoothed_prediction = [label for label, index in self.label_map.items() if index == smoothed_prediction_index][0]
            return smoothed_prediction
        return prediction  # Return original prediction if window size not met
# Initialize smoother
smoother = PredictionSmoother(window_size=5)

def preprocess_frame(frame, hand_detector):
    """
    Preprocess a video frame to match the model's input requirements (28x28 grayscale).
    Uses HandDetector to crop the hand region.
    """
    # Step 1: Detect hands
    _, results = hand_detector.detect_hands(frame)

    # Step 2: Crop the hand region
    cropped_hand = hand_detector.crop_hand(frame, results)

    # Step 3: Convert to grayscale
    gray_frame = cv2.cvtColor(cropped_hand, cv2.COLOR_BGR2GRAY)

    # Step 4: Enhance contrast
    enhanced_frame = cv2.equalizeHist(gray_frame)


    # Step 5: Resize to 28x28
    resized_frame = cv2.resize(enhanced_frame, (28, 28), interpolation=cv2.INTER_AREA)

    # Step 6: Normalize pixel values to range [0, 1]
    normalized_frame = resized_frame / 255.0

    # Add a channel dimension
    preprocessed_frame = normalized_frame[..., np.newaxis]

    return preprocessed_frame


def predict_gesture_from_frame(preprocessed_frame):
    """
    Use the pre-trained model to predict the ASL gesture from the preprocessed frame.
    """
    # Add a batch dimension (1, 28, 28, 1)
    input_data = np.expand_dims(preprocessed_frame, axis=0)

    # Perform prediction
    prediction = model.predict(input_data, verbose=0)
    predicted_class = np.argmax(prediction, axis=1)

    # Convert class index to corresponding letter (A-Z)
    predicted_letter = chr(predicted_class[0] + ord('A'))
    return predicted_letter

def capture_frame():
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
    hand_detector = HandDetector()

    # Ensure that the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return None

    # Set the resolution for faster capture (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
    # Setting the FPS (set to 30 as an example)
    cap.set(cv2.CAP_PROP_FPS, 30)


    # Return the frame as long as the webcam is working
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break


        # Preprocess the frame
        try:
            preprocessed_frame = preprocess_frame(frame, hand_detector)
        except Exception as e:
            print(f"Preprocessing error: {e}")
            continue  # Skip this frame if preprocessing fails

        predicted_letter = predict_gesture_from_frame(preprocessed_frame)
        smoothed_prediction = smoother.add_prediction(predicted_letter)

        # Display the predicted gesture on the frame
        cv2.putText(frame, f'Gesture: {predicted_letter}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame with hand landmarks
        cv2.imshow("Hand Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_frame()
