import cv2


def capture_frame():
    # Initialize the webcam capture
    cap = cv2.VideoCapture(0)  # Use 0 for default webcam

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return None

    # Set a lower resolution to capture faster
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    desired_fps = 30  # Example: 30 FPS
    cap.set(cv2.CAP_PROP_FPS, desired_fps)

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        return None

    # Release the camera
    cap.release()

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Actual FPS: {fps}")

    return frame