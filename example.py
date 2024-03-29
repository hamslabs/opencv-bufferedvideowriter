import cv2
from BufferedVideoWriter import BufferedVideoWriter

def main():
    # Initialize the videocapture
    cap = cv2.VideoCapture(0)
    
    rec=None

    # Check if the videocapture opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the video capture.")
        return

    # Loop to capture and display frames from the webcam
    while True:
        # Capture frame from webcam
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Error: Unable to capture frame.")
            break
        
        if not rec:
            h,w,_=frame.shape
            rec=BufferedVideoWriter("test.mp4",cv2.VideoWriter_fourcc(*'mp4v'), 15, (w, h))
            rec.start()

        if rec:
            rec.write(frame)

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Wait for 1 millisecond for the ESC key to exit
        if cv2.waitKey(1) == 27:
            break
        
    

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    rec.stop()

if __name__ == "__main__":
    main()
