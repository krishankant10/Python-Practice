import cv2

"""
image import,show,write:

functions to use
imread()
imwrite()
imshow()

waitkey()
destroyAllWindows()


"""

a=cv2.imread('1.jpg',0)   #1 mean color image,0 mean grace image
cv2.imshow('image',a)
cv2.imwrite('img.png',a)

x=cv2.waitKey() #till we press a key

print(x)
if(x==97):
    cv2.destroyAllWindows()
