"""============================================================================
    OpenCV Basics Demo    |    RAER SUAS 2023    |    Oct. 31, 2022
    ---------------------------------------------------------------------------
    General demo of the basics of OpenCV. Covers image opening, writing, 
    scaling, rotation, translation, edge detection, contours, and more. See the
    blob detection demo file for specifics about that.
    
    This is very messy code, which will be cleaned up and modified by the time
    it is presented to the software team.
"""

import cv2 as cv

# Open selected image in object "img"
img = cv.imread("./images/tree_smol.jpg", cv.IMREAD_COLOR)

img_smol = cv.resize(img, (int(img.shape[1]*0.25), int(img.shape[0]*0.25)))
# cv.imshow("Resized", img_smol)

# TRANSFORMATION DEMO MATERIAL
# Remove triple quotation marks to let it run
"""
img_rot = cv.rotate(img_smol, cv.ROTATE_180)
# cv.imshow("Rotated", img_rot)

img_crop = img_smol[40:300,150:400]
# cv.imshow("Cropped", img_crop)


# From https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
rows,cols,ch = img_smol.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img_smol,M,(cols,rows))
# cv.imshow("Affine Transform", dst)

cv.imwrite("./output/resized.jpg", img_smol)
cv.imwrite("./output/rotated.jpg", img_rot)
cv.imwrite("./output/cropped.jpg", img_crop)
cv.imwrite("./output/affinetransform.jpg", dst)
"""

# COLOR SPACE DEMO MATERIALS
"""
img_bgr = cv.cvtColor(img_smol, cv.COLOR_RGB2BGR)
img_hsv = cv.cvtColor(img_smol, cv.COLOR_RGB2HSV)
img_lab = cv.cvtColor(img_smol, cv.COLOR_RGB2LAB)
img_hls = cv.cvtColor(img_smol, cv.COLOR_RGB2HLS)

cv.imwrite("./output/bgr.jpg", img_bgr)
cv.imwrite("./output/hsv.jpg", img_hsv)
cv.imwrite("./output/lab.jpg", img_lab)
cv.imwrite("./output/hls.jpg", img_hls)
"""

# EDGE DETECTION / MODIFER DEMO MATERIAL
img_blur = cv.GaussianBlur(img_smol, (5,5), 0)
img_blur1 = cv.GaussianBlur(img_smol, (11, 11), 0)
img_gray = cv.cvtColor(img_blur1, cv.COLOR_RGB2GRAY)

img_dilate = cv.dilate(img_blur, (3,3), iterations=3)
img_erode = cv.erode(img_blur, (5,5), iterations=3)
img_threshold, sink = cv.threshold(img_gray, 55, 200, cv.THRESH_BINARY)

img_sobelxy = cv.Sobel(src=img_gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=3)
img_canny = cv.Canny(img_blur, 100, 200)
cv.imshow("Thresholded", sink)
cv.imshow("Dilated", img_dilate)
cv.imshow("Eroded", img_erode)
#cv.imshow("Sobel Edges", img_sobelxy)
#cv.imshow("Canny Edges", img_canny)

cv.imwrite("./output/sobel.jpg", img_sobelxy)
cv.imwrite("./output/canny.jpg", img_canny)
cv.imwrite("./output/blur.jpg", img_blur)
cv.imwrite("./outputdilate.jpg", img_dilate)
cv.imwrite("./output/erode.jpg", img_erode)
cv.imwrite("./output/thresholded.jpg", sink)


cv.waitKey()
cv.destroyAllWindows()