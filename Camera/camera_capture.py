import cv2
from ..DetectHand.hand_detection import HandDetector


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

        # Uncomment to check FPS for debugging
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # print(f"Actual FPS: {fps}")

        # Return the captured frame for testing without stopping the function
        yield frame

    cap.release()
