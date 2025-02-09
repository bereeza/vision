import cv2 as cv

WIN_NAME = "img2gray"

src = cv.imread('ford.png')
img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow(WIN_NAME, img)
cv.waitKey(0)