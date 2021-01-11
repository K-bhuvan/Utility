import cv2

cam1 = cv2.VideoCapture(2)
cam2 = cv2.VideoCapture(4)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame1 = cam1.read()
    ret, frame2 = cam2.read()
    cv2.imshow("test", frame1)
    cv2.imshow("test", frame2)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite("brown_dataset/left_starB/" + img_name, frame1)
        cv2.imwrite("brown_dataset/right_starB/" + img_name, frame2)
        print("{} written!".format(img_name))
        img_counter += 1

cam1.release()
cam2.release()

cv2.destroyAllWindows()