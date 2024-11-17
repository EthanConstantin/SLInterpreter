import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self):
        # Initialize MediaPipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        """Detect hands in the frame and return the frame with drawn landmarks."""
        # Convert frame to RGB (MediaPipe uses RGB images)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            # For each detected hand, draw landmarks and return the frame
            for landmarks in results.multi_hand_landmarks:  # Each hand has 21 landmarks
                self.mp_drawing.draw_landmarks(frame, landmarks, self.mp_hands.HAND_CONNECTIONS)

        return frame, results

    @staticmethod
    def get_landmarks(results):
        """Extract and return hand landmarks."""
        if not results.multi_hand_landmarks:
            return None

        landmarks = []
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmarks_data = []
            for landmark in hand_landmarks.landmark:
                hand_landmarks_data.append([landmark.x, landmark.y, landmark.z])
            landmarks.append(hand_landmarks_data)
        return landmarks

    @staticmethod
    def crop_hand(frame, results):
        """
        Crop the hand region from the frame using MediaPipe landmarks.
        Returns the cropped frame of the detected hand.
        """
        if not results.multi_hand_landmarks:
            return frame  # Return the original frame if no hand is detected

        h, w, _ = frame.shape
        hand_landmarks = results.multi_hand_landmarks[0]  # Focus on the first detected hand

        # Get bounding box coordinates
        x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
        x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
        y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
        y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)

        # Add padding to the bounding box
        padding = 20
        x_min = max(0, x_min - padding)
        x_max = min(w, x_max + padding)
        y_min = max(0, y_min - padding)
        y_max = min(h, y_max + padding)

        # Crop the hand region
        cropped_hand = frame[y_min:y_max, x_min:x_max]
        return cropped_hand