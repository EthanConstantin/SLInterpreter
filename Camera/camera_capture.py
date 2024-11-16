import cv2
import numpy as np

import keras

from hand_detection import HandDetector

# Loading the SL model
model = keras.models.load_model('../Sign_Language_Recognition/smnist.h5')

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

        # Detect hands and extract landmarks
        frame_with_landmarks, results = hand_detector.detect_hands(frame)

        predicted_letter = predict_gesture_from_frame(preprocessed_frame)

        # Display the predicted gesture on the frame
        cv2.putText(frame, f'Gesture: {predicted_letter}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame with hand landmarks
        cv2.imshow("Hand Detection", frame_with_landmarks)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_frame()
