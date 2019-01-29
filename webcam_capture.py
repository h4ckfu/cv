# This is a very simple, minimal python script to capture video through
# a webcam and save it to a hard drive. Use a filename to test w/o webcam.

import cv2

cap = cv2.VideoCapture(0) # need a webcam for this to work or replace 0 w/ filename

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Your VideoWriter Codec may vary info here:
# https://www.pyimagesearch.com/2016/02/22/writing-to-video-with-opencv/

writer = cv2.VideoWriter('captured.avi', cv2.VideoWriter_fourcc(*'XVID'),20,(w,h))

while True:
    ret,frame = cap.read()
    writer.write(frame)

    cv2.imshow('frame',frame)

    # hit the q key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
