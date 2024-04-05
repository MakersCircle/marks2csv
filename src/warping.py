# warp the input image
# import the necessary packages
import numpy as np
import cv2
import imutils
from skimage.filters import threshold_local

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return warped

def warp(image):
    img = image
    big_img = cv2.imread(img)

    ratio = big_img.shape[0] / 500.0
    org = big_img.copy()
    img = imutils.resize(big_img, height = 500)

    gray_img = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img,(5,5),0)
    edged_img = cv2.Canny(blur_img,75,200)


    cnts,_ = cv2.findContours(edged_img.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*peri,True)
        if len(approx)==4:
            doc = approx
            break
            
            
    p=[]
    for d in doc:
        tuple_point = tuple(d[0])
        cv2.circle(img,tuple_point,3,(0,0,255),4)
        p.append(tuple_point)

    warped = four_point_transform(org, doc.reshape(4, 2) * ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    #USE WARPED IN THE NEXT STEP OF THE CODE, The output datatype is a numpy array

    #cv2.imwrite('warpped.jpg', warped)         #This line is used to save the warpped (not scanned) image as jpg file.


    #T = threshold_local(warped, 11, offset = 10, method = "gaussian")
    #warped = (warped > T).astype("uint8") * 255
    #cv2.imwrite('scanned.jpg', warped)         #This line is used to save the scanned image as jpg file.