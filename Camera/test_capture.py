import cv2
from camera_capture import capture_frame


def test_camera_capture():
    # Capture a frame using the capture_frame function
    frame = capture_frame()

    if frame is not None:
        # Display the captured frame in a window
        cv2.imshow("Captured Frame", frame)

        # Wait for a key to be pressed, then close the window
        cv2.waitKey(0)  # 0 waits indefinitely for a key press
        cv2.destroyAllWindows()
    else:
        print("No frame captured.")

if __name__ == "__main__":
    test_camera_capture()