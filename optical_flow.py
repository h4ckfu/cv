import numpy as np
import cv2 # calcOpticalFlowFarneback, cartToPolar

# Optical Flow is the idea that you can figure out patterns of motion by
# determining the differences between frames.  This should change color
# depending on motion - blue is left?  No my left..

# My frames here will eventually be called prev_img and next_img

# get one frame before we start looping and make a grayscale version
cap = cv2.VideoCapture(0)
ret, frame1=cap.read()
prev_img = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('color_flow.avi', cv2.VideoWriter_fourcc(*'XVID'),20,(w,h))

# make a hsV mask and turn the Value column all the way up
# zeros_like - wel played numpy, well played
hsv_mask=np.zeros_like(frame1)
hsv_mask[:,:,1]=255

# the idea is to comapre prev_img to nextImg

while True:

    ret,frame2=cap.read()
    # Right now frame1 is the img before this loop and frame2 is cap now

    next_img = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    #the grayscale version of the image we just captured

    # we now have prvsImg and nextImg and they are greyscale

    flow = cv2.calcOpticalFlowFarneback(prev_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    #right now these  images co-ordinates are the standard cartesian x,y
    # This converts them to "polar" cordinates for magnitude and angle.

    #for every pixel in x and y in flow = flow[:,:] get the horizonatal info [:,:,0]
    # and then for the vertical info for every pix as well
    # and convert them to magnatude and angle
    mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1],angleInDegrees=True)

    #get half of the angles - from 360 to 180 - and then normalize
    hsv_mask[:,:,0] = ang/2
    hsv_mask[:,:,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)

    bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)

    writer.write(bgr)

    cv2.imshow('frame2',bgr)

    # Only the esc key will do...
    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break

    # reset
    prev_img = next_img

# cleanup
cap.release()
cv2.destroyAllWindows()
