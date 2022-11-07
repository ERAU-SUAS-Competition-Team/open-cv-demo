"""============================================================================
    Contour Detection Demo   |    RAER SUAS 2023    |    Nov. 7, 2022
    ---------------------------------------------------------------------------
    Demonstration of built-in contour detection. Feel free to add to or correct
    this, as it is fairly rushed.
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


# Make the image grayscale for thresholding
img_gray = cv.cvtColor(img_smol, cv.COLOR_RGB2GRAY)


# apply binary thresholding
ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
#cv.imshow('Binary image', thresh)

# Run the findContours method on the thresholded image. We are using the
# default mode and method from a tutorial found on 
# https://learnopencv.com/ , which is a useful resource for basic 
# tutorials and documentation, if you need it.
contours, h = cv.findContours(image=thresh, mode=cv.RETR_TREE, 
                              method=cv.CHAIN_APPROX_NONE)

# Make a copy for the final output. Only really necessary if you want both seen
img2 = img_smol.copy()

# Draw the contours on the copy image, using the generated contours above.
# ContourIDx of -1 means ALL
# Color is the outline color
# Thickness is line thickness
# Linetype is how it draws lines. AA is anti-aliased, which looks nicer
showcontours = cv.drawContours(image=img2, contours=contours, contourIdx=-1, color=(255,0,0), thickness=1, lineType=cv.LINE_AA)

#cv.imshow("CONTOURS!", showcontours)

cv.waitKey(0)
cv.destroyAllWindows()

# Writes all the outputs to dedicated files in the ./output/ folder.
cv.imwrite("./output/threshold.jpg", thresh)
cv.imwrite("./output/contours.jpg", img2)