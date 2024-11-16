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
