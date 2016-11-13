# Labeling tool for creating the hand tracking dataset for Dranimate
# 
# Author: Pratik Prakash
#
# Program reads images from a given directory and lets the user draw points on
# the image with their mouse. These selected (x,y) coordinates are then saved
# into a text file in a user specified output directory. The program stores all
# the text files in a directory called labels.
#
# To run in command line: 
# python labeler.py --input <InputDir> --output <OutputDir>
# Ex. python labeler.py --input <path/to/images/> --output <path/>
#
# Press 'd' to move on to the next image
# Press 'esc' to quit the program
#
# The data is stored in textfile as the (x,y) coordinates of the fingers in this order
# 	(x1,y1) => pinky
# 	(x2,y2) => ring
# 	(x3,y3) => middle
# 	(x4,y4) => index
# 	(x5,y5) => thumb

import cv2
import numpy as np
import glob
import argparse
import os

### Mouse event to save x,y pixel coordinates ###
def savePixelCoordinate(event, x, y, flags, param):
	global points
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img,(x,y),5,(255,0,0),-1)
		points.append((x,y))
		print(points)
	pass

### Display the image ###
def displayImage(img):
	global points
	quit = False

	while(1):
		# Show the image in a new window
		cv2.imshow('image', img)

		# Wait for a key press
		k = cv2.waitKey(1) & 0xFF
		if k == ord('d'): # Press d for done
			break
		elif k == 27:
			quit = True
			break

	# Destroy the window
	cv2.destroyAllWindows()
	return quit

#### MAIN ####
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='image input directory')
parser.add_argument('--output', help='textfile output directory')
args = parser.parse_args()

# Create output directory
outDirectory = args.output + "labels/"
if not os.path.exists(outDirectory):
    os.makedirs(outDirectory)

points = [];

for imgPath in glob.glob(args.input + "*.jpg"):
	# Read the image using the path
	img = cv2.imread(imgPath)
	cv2.namedWindow('image')

	# Intialize mouse callback
	cv2.setMouseCallback('image', savePixelCoordinate)

	# Show image in a new window
	done = displayImage(img)

	# Check if we can quit the program
	if done:
		break

	# Save points to text file
	fileName = os.path.basename(imgPath)
	fileName = os.path.splitext(fileName)[0]
	np.savetxt(outDirectory + fileName + '.txt', points, fmt='%i')

	# Reset points for next image
	points = [];

print('bye bye!')
