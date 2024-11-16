import cv2
from camera_capture import capture_frame


def test_camera_capture():
    # Create a generator to fetch frames
    frame_generator = capture_frame()

    # Capture a single frame from the generator
    try:
        frame = next(frame_generator)  # Get the first frame from the generator

        if frame is not None:
            # Display the captured frame in a window
            cv2.imshow("Captured Frame", frame)

            # Wait for a key press to close the window
            cv2.waitKey(0)  # 0 waits indefinitely for a key press
            cv2.destroyAllWindows()

        else:
            print("No frame captured.")
    except StopIteration:
        print("Camera capture stopped.")


if __name__ == "__main__":
    test_camera_capture()
