from flask import Flask, Response
import cv2
import numpy as np
from collections import deque
from tensorflow import keras
from hand_detection import HandDetector
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)
# Loading the SL model
model = keras.models.load_model('C:/Users/Kyle/Desktop/REPO/eecs1012labs/final/testRepo/SLInterpreter/Sign_Language_Recognition/smnist.h5')

class PredictionSmoother:
    def __init__(self, window_size=5, label_map=None):
        self.window_size = window_size
        self.predictions = deque(maxlen=window_size)
        self.label_map = label_map if label_map else {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
            'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }

    def add_prediction(self, prediction):
        if prediction in self.label_map:
            self.predictions.append(self.label_map[prediction])
        if len(self.predictions) == self.window_size:
            smoothed_prediction_index = np.bincount(self.predictions).argmax()
            smoothed_prediction = [label for label, index in self.label_map.items() if index == smoothed_prediction_index][0]
            return smoothed_prediction
        return prediction

smoother = PredictionSmoother(window_size=5)

def preprocess_frame(frame, hand_detector):
    _, results = hand_detector.detect_hands(frame)
    cropped_hand = hand_detector.crop_hand(frame, results)
    gray_frame = cv2.cvtColor(cropped_hand, cv2.COLOR_BGR2GRAY)
    enhanced_frame = cv2.equalizeHist(gray_frame)
    resized_frame = cv2.resize(enhanced_frame, (28, 28), interpolation=cv2.INTER_AREA)
    normalized_frame = resized_frame / 255.0
    preprocessed_frame = normalized_frame[..., np.newaxis]
    return preprocessed_frame

def predict_gesture_from_frame(preprocessed_frame):
    input_data = np.expand_dims(preprocessed_frame, axis=0)
    prediction = model.predict(input_data, verbose=0)
    predicted_class = np.argmax(prediction, axis=1)
    predicted_letter = chr(predicted_class[0] + ord('A'))
    return predicted_letter

def generate_frames():
    cap = cv2.VideoCapture(0)
    hand_detector = HandDetector()
    while True:
        success, frame = cap.read()
        if not success:
            break
        try:
            preprocessed_frame = preprocess_frame(frame, hand_detector)
            predicted_letter = predict_gesture_from_frame(preprocessed_frame)
            smoothed_prediction = smoother.add_prediction(predicted_letter)
            cv2.putText(frame, f'Gesture: {predicted_letter}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error processing frame: {e}")
        
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

