"""============================================================================
    Transformation Demo   |    RAER SUAS 2023    |    Nov. 7, 2022
    ---------------------------------------------------------------------------
    Demonstration of transformation functions in OpenCV. See the README for
    file source location. Affine transform example is copied from opencv.org.
    Citation can be found in the comment alongside of its use.
"""

import cv2 as cv
import numpy as np

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



# --------------------------------  ROTATE  -----------------------------------
# Rotate the image by 180 degrees
img_rot = cv.rotate(img_smol, cv.ROTATE_180)
# cv.imshow("Rotated", img_rot)



# ----------------------------------  CROP  -----------------------------------
# Crops the image to a specific range, defined using standard array handling.
img_crop = img_smol[40:300,150:400]
# cv.imshow("Cropped", img_crop)



# ----------------------------  AFFINE TRANSFORM  -----------------------------
# Base code from
# https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
# Has been properly commented and had the output object changed.

# Defines three variables for different shape attributes
rows,cols,ch = img_smol.shape

# Defines initial set of points, then the final set that it will transform to
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# Gets the transformation matrix, then applies it using the warpAffine method.
M = cv.getAffineTransform(pts1,pts2)
img_affine = cv.warpAffine(img_smol,M,(cols,rows))
# cv.imshow("Affine Transform", img_affine)


cv.waitKey()  # Keeps show windows open until keypress
cv.destroyAllWindows()  # Closes all windows after keypress received

# Writes all the outputs to dedicated files in the ./output/ folder.
cv.imwrite("./output/resized.jpg", img_smol)
cv.imwrite("./output/rotated.jpg", img_rot)
cv.imwrite("./output/cropped.jpg", img_crop)
cv.imwrite("./output/affinetransform.jpg", img_affine)