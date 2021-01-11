import cv2
import numpy as np
import sys

def main():
	video1 = cv2.VideoCapture(2)
	video2 = cv2.VideoCapture(4)

	is_okay, leftImage = video1.read()
	if not is_okay:
		print("Cannot read Video")
		sys.exit();
	is_okay, rightImage = video2.read()
	if not is_okay:
		print("Connot read Video")
		sys.exit();

	count = 0

	while True:
		is_okay, leftImage = video1.read()
		is_okay, rightImage = video2.read()

		cv2.imshow("Left Image", leftImage)
		cv2.imshow("Right Image", rightImage)

		
		cv2.imwrite("left/" + str(count).zfill(6)+'.png',leftImage)
		cv2.imwrite("right/" + str(count).zfill(6)+'.png',rightImage)

		count += 1
		
		keyPressed = cv2.waitKey(1) & 0xFF
		if keyPressed == ord('q') or keyPressed == 27:
			break;

if __name__ == "__main__":
	main()