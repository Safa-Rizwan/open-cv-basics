# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,default='tom.jpg',
	help="path to input image")
args = vars(ap.parse_args())

# load the image from disk via "cv2.imread" and then grab the spatial
# dimensions, including width, height, and number of channels
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print(f"width: {w} pixels")
print(f"height: {h}  pixels")
print(f"channels: {c}")

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
cv2.imwrite("newimage2.png", image)