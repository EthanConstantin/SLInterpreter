import cv2

from hand_detection import HandDetector



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

        # Detect hands and extract landmarks
        frame_with_landmarks, results = hand_detector.detect_hands(frame)

        # Optionally, get landmarks for further processing
        landmarks = hand_detector.get_landmarks(results)

        if landmarks:
            print(f"Detected {len(landmarks)} hands.")  # Print number of hands detected

        # Display the frame with hand landmarks
        cv2.imshow("Hand Detection", frame_with_landmarks)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_frame()
