"""
Library to use
import cv2

function to use
video capture this function captures the content of a video argument integer value depend on ur camera.(0 for main camera,1 ,2,3 other camera)
read:read the content in the form of frames.if true reading
write:write the content of frame to make a video
VideoWrite_fourcc:use to select the codec XVID
VideoWriter:use to select the video to make,codec,frame/sec,pixel
flip: to flip the frame
waitkey(argument(only integer value))
release: this will release the resources used by python.
destroyAllWindows:close all open windows

"""
import cv2
cap=cv2.VideoCapture(0)
#while(cap.isopen()):
flag,frame=cap.read()
cv2.imshow('image',frame)
cv2.waitKey(1)
cap.release
cv2.destroyAllWindows()
"""

import
