import cv2

# Tracker Boosting was the most effective api in my tests
# This may fail here if there are older ( different ) versions of cv2 installed.
tracker = cv2.TrackerBoosting_create()
tracker_name = 'JTk is Tracker Boosting...'

# This VideoCapture(0) means its looking for the first camera on the bus
# You can replace that 0 with a videofilename.mp4 if no cam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Not looping yet so that cap above is just grabbing one frame
# Special function allows us to select desired ROI manually on the very first frame
roi = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box (roi)
ret = tracker.init(frame, roi)


while True:

    ret, frame = cap.read()

    # if its able give the tracker a new frame to relocate selected roi
    success, roi = tracker.update(frame)

    # roi variable is a tuple of 4 floats; we need int of each
    (x, y, w, h) = tuple(map(int,roi))

    # Draw Rectangle as Tracker moves
    if success:
        # Tracking success
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (135,133,6), 2)
    else :
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(59,83,237), 3)

    # Display tracker type on frame and then display it
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (52,177,242),2);
    cv2.imshow(tracker_name, frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 :
        break

cap.release()
cv2.destroyAllWindows()
