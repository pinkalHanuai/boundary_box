import cv2

# Load the image
image = cv2.imread("image.jpg")

# Define the coordinates of the bounding box
x, y, w, h = 200, 100, 200, 200

# Draw the bounding box on the image
cv2.rectangle(image, (x, y), (x + w, y + h), (100, 255, 200), 2)

# Display the image with the bounding box
cv2.imshow("Image with bounding box", image)
cv2.waitKey(0)
