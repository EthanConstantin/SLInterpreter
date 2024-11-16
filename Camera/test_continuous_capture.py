import cv2
from camera_capture import capture_frame


def test_continuous_capture():
    while True:
        # Capture a frame from the webcam
        frame = capture_frame()

        if frame is not None:
            # Display the captured frame in a window
            cv2.imshow("Live Video Feed", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: No frame captured.")
            break

    # Release resources and close window
    cv2.destroyAllWindows()


if __name__ == "__main__":
    test_continuous_capture()