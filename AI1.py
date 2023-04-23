# read and show image ----

# import OpenCV
import cv2

#Read image from img.jpg file and store it as a variable image
image = cv2.imread("img.jpg")

#Show image
cv2.imshow( "Sea", image)

I = cv2.waitKey(0)

# The window of the image will be closed if we press S or command Esc
if I == 27 or I == ord('s'):
    cv2.destroyAllWindows()
