import cv2
import numpy as np
import time
# Set the threshold for detecting blank/black frames
BLANK_FRAME_THRESHOLD = 30

# Set the maximum time to print integers
MAX_PRINTING_TIME = 45

# Capture frames from the camera
cap = cv2.VideoCapture(0)

# Initialize the previous frame as blank
prev_frame_blank = True

# Initialize the start time for printing integers
start_time = None

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale and calculate the mean intensity
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mean_intensity = np.mean(gray)

    # Check if the frame is blank
    is_blank = mean_intensity < BLANK_FRAME_THRESHOLD

    # Wait until a non-blank frame appears after a blank frame
    while is_blank and prev_frame_blank:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean_intensity = np.mean(gray)
        is_blank = mean_intensity < BLANK_FRAME_THRESHOLD

    # If the frame is non-blank and it's the first non-blank frame,
    # start printing integers
    if not is_blank and prev_frame_blank:
        start_time = time.time()
        count = 1
        print(count)
        prev_frame_blank = False

    # If the frame is non-blank and it's not the first non-blank frame,
    # continue printing integers until a new non-blank frame appears
    elif not is_blank and not prev_frame_blank:
        elapsed_time = time.time() - start_time
        if elapsed_time < MAX_PRINTING_TIME:
            count += 1
            print(count)
        else:
            prev_frame_blank = True

    # If the frame is blank, set the previous frame as blank
    else:
        prev_frame_blank = True

    # If a new non-blank frame appears, stop printing integers and wait for
    # the next non-blank frame
    if prev_frame_blank and start_time is not None:
        start_time = None

    # Show the frame
    cv2.imshow('frame', frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
