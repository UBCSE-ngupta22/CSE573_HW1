# Reguired Libraries
import cv2
import numpy as np
import math

# Image path
image = cv2.imread('image.png')

# Dimensions of the image
height, width, channels = image.shape

# Check if the image is RGB or not
if channels == 3:
    print("Its a RGB image")
else:
    print("Its a grayscale image")

# Manually convert the image to grayscale
"""
uint8 - unsigned 8-bit integer, each pixel in the
array will be in the range of 0-255
"""
grayImage = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        r, g, b = image[i, j]
        """
        Multiply r,g,b with individual color weightage 
        sensitive to human eye. Green being the highest
        """
        grayPixel = 0.299 * r + 0.587 * g + 0.114 * b
        grayImage[i, j] = int(grayPixel)

# Save the obtained grayscale image
cv2.imwrite('gray image.png', grayImage)

# Reduce the grayscale image size to half (256x128)
scaled_image = grayImage[::2, ::2]

# Save the obtained grayscale scaled image
cv2.imwrite('gray image scaled.png', scaled_image)

# Create a blank image
translatedImage = np.zeros_like(grayImage)

# Translate the image by 50 pixels to both right and down
for i in range(50, height):
    for j in range(50, width):
        translatedImage[i, j] = grayImage[i - 50, j - 50]

# Save the translated grayscale result
cv2.imwrite('gray image translated.png', translatedImage)

# Flip along horizontal axis or reverse rows
flippedHorizontalImage = grayImage[::-1, :]

# Save the horizontally flipped image
cv2.imwrite('gray image flip horizontal.png', flippedHorizontalImage)

# Flip along vertical axis or reverse columns
flippedVerticalImage = grayImage[:, ::-1]

# Save the vertically flipped image
cv2.imwrite('gray image flip vertical.png', flippedVerticalImage)

"""
Changes all the dark areas to light areas and vice versa.
0 means black.
255 means white.
Values in between represent different shades of gray (128 is a medium gray).
The operation 255 - gray_image takes each pixel value in the gray_image and subtracts it from 255.
"""
# Invert grayscale image
invertedImage = 255 - grayImage

# Save the result
cv2.imwrite('gray image inversion.png', invertedImage)

# Create a blank image
rotatedImage = np.zeros_like(grayImage)

# Center of the image
center_x, center_y = width // 2, height // 2

# Rotation matrix for 45 degrees clockwise
"""
Since we need a clockwise rotation, 
the angle is negative
"""
angle = -45 * (math.pi / 180)
cos_theta = math.cos(angle)
sin_theta = math.sin(angle)

for i in range(height):
    for j in range(width):
        # Translate points to the origin
        x, y = j-center_x, i-center_y
        
        # Apply the rotation matrix
        x_bar = int(x * cos_theta - y * sin_theta + center_x)
        y_bar = int(x * sin_theta + y * cos_theta + center_y)
        
        """
        Check if the new coordinates are 
        within the image dimension bounds
        """
        if 0 <= x_bar < width:
            if 0 <= y_bar < height:
                rotatedImage[y_bar, x_bar] = grayImage[i, j]

# Save the result
cv2.imwrite('gray image rotated.png', rotatedImage)

# Reduce the original image size to half (256x128)
scaled_org_image = image[::2, ::2]

# Save the obtained original scaled image
cv2.imwrite('image scaled.png', scaled_org_image)

# Create a blank image
translated_org_image = np.zeros_like(image)

# Translate the original image by 50 pixels to both right and down
for i in range(50, height):
    for j in range(50, width):
        translated_org_image[i, j] = image[i - 50, j - 50]

# Save the translated original image result
cv2.imwrite('image translated.png', translated_org_image)

# Flip along horizontal axis or reverse rows
flipped_horizontal_org_image = image[::-1, :]

# Save the horizontally flipped original image
cv2.imwrite('image flip horizontal.png', flipped_horizontal_org_image)

# Flip along vertical axis or reverse columns
flipped_vertical_org_image = image[:, ::-1]

# Save the vertically flipped original image
cv2.imwrite('image flip vertical.png', flipped_vertical_org_image)


