"""============================================================================
    Edge Detection Demo   |    RAER SUAS 2023    |    Nov. 7, 2022
    ---------------------------------------------------------------------------
    Demonstration of Canny and Sobel edge detection, as well as using Gaussian
    blur, dilate, erode, and other similar methods. This covers more than seen
    in the presentation or in the main.py file.
    
    Feel free to submit better code for a better sobel output. I genuinely 
    can't figure out how to get a proper output from it that provides any 
    useful data.
"""

import cv2 as cv

# Open the selected image in the object "img"
# The image is read in color format.
img = cv.imread("./images/tree_smol.jpg", cv.IMREAD_COLOR)



# ----------------------------------  SCALE  ----------------------------------
# Resize the image to a smaller size in order to display nicely on your screen.
#    This takes the individual resolutions of 'img' and divides each by 4.
#    The resulting image is 1/16th the size of the initial.
x_scale = img.shape[1] * 0.25
y_scale = img.shape[0] * 0.25
img_smol = cv.resize(img, (int(x_scale), int(y_scale)))

# Uncomment the line below to see the example. This can be done for all
# imshow lines!
# cv.imshow("Resized", img_smol)



# ------------------------------- PRE-PROCESSING ------------------------------
# Gaussian blur with a 5x5 kernel
img_blur = cv.GaussianBlur(img_smol, (5,5), 0)
#cv.imshow("5x5 Gaussian Blur", img_blur)

# Gaussian blur with an 11x11 kernel. Kernels must be made of odd numbers!
img_blur1 = cv.GaussianBlur(img_smol, (11, 11), 0)
#cv.imshow("11x11 Gaussian Blur", img_blur1)

# Convert 11x11 blurred image to grayscale for use in Sobel edge detection
img_gray = cv.cvtColor(img_blur1, cv.COLOR_RGB2GRAY)
#cv.imshow("Grayscale Image", img_gray)


# Dilate image with 3x3 kernel, depth of 3
# You won't see a clear difference here, it affects edge detection though
img_dilate = cv.dilate(img_blur, (3,3), iterations=3)
#cv.imshow("Dilated Image", img_dilate)

# Erode image with 5x5 kernel, depth of 5
# You won't see a clear difference here, it affects edge detection though
img_erode = cv.erode(img_blur, (5,5), iterations=3)
#cv.imshow("Eroded Image", img_erode)

# Threshold the image to specific values. This is hard to explain, you may
# want to do some googling.
sink, img_threshold = cv.threshold(img_gray, 55, 200, cv.THRESH_BINARY)
# This won't output, is broken.
# cv.imread("Thresholded Image", img_threshold)

# Sobel Edge Detection with differences on both x and y directions.
# Kernel size of 3.
# Operates on orignal image but in grayscale
img_sobelxy = cv.Sobel(src=img_gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=3)
#cv.imshow("Sobel Edge Detection", img_sobelxy)

# Canny Edge Detection, threshold of (100, 200)
# Operates on 5x5 Gaussian Blurred image
img_canny = cv.Canny(img_blur, 100, 200)
#cv.imshow("Canny Edge Detection", img_canny)


# Here is Canny Edge Detection on the dilated and eroded images
img_canny_dilated = cv.Canny(img_dilate, 100, 200)
img_canny_eroded = cv.Canny(img_erode, 100, 200)

# Dilated will be thinner, sharper
# Eroded will be wider, smoother
#cv.imshow("Canny Edges Dilated", img_canny_dilated)
#cv.imshow("Canny Edges Eroded", img_canny_eroded)



cv.waitKey()  # Keeps show windows open until keypress
cv.destroyAllWindows()  # Closes all windows after keypress received


# Outputs all changes to images in ./output/ folder
cv.imwrite("./output/sobel.jpg", img_sobelxy)
cv.imwrite("./output/canny.jpg", img_canny)
cv.imwrite("./output/blur.jpg", img_blur)
cv.imwrite("./output/dilate.jpg", img_dilate)
cv.imwrite("./output/erode.jpg", img_erode)
cv.imwrite("./output/thresholded.jpg", img_threshold)