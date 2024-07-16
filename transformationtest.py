import cv2
import numpy as np
import math

# Load the image
#image = cv2.imread("imagetest.jpg")

# # Get image dimensions
# height, width = image.shape[:2]

# # Define the angle of inclination (in degrees)
# angle = -15

# # Calculate the perspective transformation matrix
# fov = 90  # Field of view in degrees
# focal_length = width / (2 * np.tan(fov / 2 * np.pi / 180))  # Focal length calculation
# M = np.float32([
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, -1 / focal_length, 0]
# ])

# # Apply the perspective transformation to the image
# warped_image = cv2.warpPerspective(image, M, (width, height))

# # Display the original and warped images
# imgdis = cv2.resize(image, (480, 270))   
# img2dis = cv2.resize(warped_image, (480, 270))   
# cv2.imshow("Original Image", imgdis)
# cv2.imshow("Warped Image", img2dis)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
####################################
def angle_to_shift(angle):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle)
    # Calculate the horizontal shift based on the angle
    shift = math.tan(angle_radians)
    return shift

desired_angle = 14

# Calculate the horizontal shift based on the desired angle
angle_shift = angle_to_shift(desired_angle)

img = cv2.imread('imagecalibration.jpg')
rows, cols, ch = img.shape    
pts1 = np.float32(
    [[cols*.25, rows*.95],
     [cols*.90, rows*.95],
     [cols * (.10 + angle_shift), 0],
     [cols * (1 - angle_shift), 0]]
)
pts2 = np.float32(
    [[cols*0.1, rows],
     [cols,     rows],
     [0,        0],
     [cols,     0]]
)    
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))


scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resizedorg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
resizedwrp = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Original Image', resizedorg)
cv2.imshow('Warped Image', resizedwrp)
cv2.waitKey()
########################################


# # Load the image
# img = cv2.imread('imagecalibration.jpg')
# height, width, channels = img.shape

# # Define the tilt angle (15 degrees in this example)
# tilt_angle = -1 

# # Define the scaling factor (vertical scaling to simulate top-down view)
# vertical_scale = 1 / np.cos(np.radians(tilt_angle))

# # Perform scaling to simulate top-down view
# scaled_img = cv2.resize(img, None, fx=1, fy=vertical_scale, interpolation=cv2.INTER_LINEAR)

# # Perform perspective transformation to correct the angle
# tilt_matrix = np.float32([[1, 0, 0], [0, 1, 0], [0, np.tan(np.radians(tilt_angle)), 1]])
# tilted_img = cv2.warpPerspective(scaled_img, tilt_matrix, (width, height))

# # Display the original and tilted images
# # cv2.imshow('Original Image', img)
# # cv2.imshow('Tilted Image', tilted_img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
##########################################




# scale_percent = 40 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)

# resizedorg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# resizedwrp = cv2.resize(tilted_img, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow('Original Image', resizedorg)
# cv2.imshow('Warped Image', resizedwrp)
# cv2.waitKey()

# #cv2.imwrite('zen.jpg', dst)
