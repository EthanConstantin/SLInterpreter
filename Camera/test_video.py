import cv2
from camera_capture import capture_frame


def test_video_feed():
    frame_generator = capture_frame()  # Create a generator to fetch frames

    # Capture frames continuously from the generator
    while True:
        try:
            frame = next(frame_generator)  # Get the next frame from the generator

            # Display the captured frame
            cv2.imshow("Video Feed", frame)

            # Print FPS for debugging purposes (optional)
            # If you want to print actual FPS, uncomment the line below
            # fps = cap.get(cv2.CAP_PROP_FPS)
            # print(f"Actual FPS: {fps}")

            # Exit the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except StopIteration:
            print("Camera capture stopped.")
            break

    # Release resources and close window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_video_feed()