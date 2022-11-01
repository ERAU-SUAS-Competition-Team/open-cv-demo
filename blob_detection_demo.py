"""============================================================================
    Blob Detection Demo    |    RAER SUAS 2023    |    Oct. 31, 2022
    ---------------------------------------------------------------------------
    Requires a basic knowledge of OpenCV Python, please see other files for a
    good introduction to more of that.
    
    Make sure to download the images from the good drive! They are too big to 
    put on Github simply. The images should be placed into the provided
        ./images/
    folder.
"""

# OpenCV Import, alias to cv
import cv2 as cv

# i is for the file naming
# size (distance from blob coordinate)
i = 0
size = 70

# Index of pictures. Not good practice for import but it works well enough.
pics = ['26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg',
        '47.jpg', '49.jpg', '65.jpg', '66.jpg', '67.jpg', '68.jpg']

for p in pics:
    img = cv.imread('./images/'+str(p), cv.IMREAD_COLOR)  # Import color image
    img = cv.cvtColor(img, cv.COLOR_RGB2HSV)  # Convert to HSV matrices
    
    # - - - - - -

    # Setup SimpleBlobDetector parameters.
    params = cv.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 1600
    #params.maxArea = 3600

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.4

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.5

    # Create a detector with the parameters
    det = cv.SimpleBlobDetector_create(params)

    # Re-open image in color (for little cropped output)
    col_img = cv.imread('./images/'+str(p), 3)

    i_check = i
    key = det.detect(img)
    for keeb in key:
        x = keeb.pt[1]
        y = keeb.pt[0]
        outs = col_img[int(x-size):int(x+size),int(y-size):int(y+size)]
        cv.imwrite('./output/out'+str(i)+'.jpg', outs)
        i += 1

    if i_check == i:
        img = cv.cvtColor(img, cv.COLOR_HSV2RGB)
        key = det.detect(img)
        for keeb in key:
            x = keeb.pt[1]
            y = keeb.pt[0]
            outs = col_img[int(x-size):int(x+size),int(y-size):int(y+size)]
            cv.imwrite('./output/out'+str(i)+'.jpg', outs)
            i += 1
    """
    # (Draw circles around the blobs and draws them on the image. 
    # Commented out because it doesn't work too well on images this big)    
    #keyimg = cv.drawKeypoints(img, key, np.array([]), (0,0,255), 
    #    cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    #w = img.shape[1] * 0.25
    #h = img.shape[0] * 0.25
    #res = cv.resize(img, (int(w), int(h)))
    #cv.imshow('title', res)
    """
    
    # UNCOMMENT THESE IF YOU ARE DISPLAYING IMAGES
    #cv.waitKey()
    #cv.destroyAllWindows()

print("DONE") 