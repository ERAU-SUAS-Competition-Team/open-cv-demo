"""============================================================================
    Color Spaces Demo   |    RAER SUAS 2023    |    Nov. 7, 2022
    ---------------------------------------------------------------------------
    Demonstration of the differences between color spaces. Please note that
    each color space represents the exact same image, and that if you could
    view those outputs in their proper spaces, they would all look the same.
    The differences seen are because we are mapping each layer of those other
    formats back to RGB (or BGR).

    Using different color spaces can be a very useful tool for differentiating
    components of images. If an input can't easily be differentiated in RGB, it
    could be because there isn't much difference in that space. But in HSV, the
    differences could be extremely clear with a very strong edge. If you're 
    ever processing inputs and can't get a good result, possibly try running 
    the processing in HSV or another space to find a clear output!
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



# ------------------------------- COLOR SPACES --------------------------------
img_bgr = cv.cvtColor(img_smol, cv.COLOR_RGB2BGR)  # RGB to BGR (Reversed)
#cv.imshow("RGB 2 BGR", img_bgr)

# RGB to Hue, Saturation, Value
img_hsv = cv.cvtColor(img_smol, cv.COLOR_RGB2HSV)
#cv.imshow("RGB 2 HSV", img_hsv)

# RGB to L*A*B*, Lightness, A, B (Approximates human vision inputs)
img_lab = cv.cvtColor(img_smol, cv.COLOR_RGB2LAB)
#cv.imshow("RGB 2 L*A*B*", img_lab)

# RGB to Hue, Lightness, Saturation (Like a mixed HSV?)
img_hls = cv.cvtColor(img_smol, cv.COLOR_RGB2HLS)
#cv.imshow("RGB 2 HLS", img_hls)

cv.waitKey()  # Keeps show windows open until keypress
cv.destroyAllWindows()  # Closes all windows after keypress received


# Outputs all changes to images in ./output/ folder
cv.imwrite("./output/bgr.jpg", img_bgr)
cv.imwrite("./output/hsv.jpg", img_hsv)
cv.imwrite("./output/lab.jpg", img_lab)
cv.imwrite("./output/hls.jpg", img_hls)