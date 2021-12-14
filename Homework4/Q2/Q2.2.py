import time
import cv2

image = cv2.imread(r'C:\Users\jadha\CU--AuE-8930-HW\Homework4\Q2\Flower.jpg')
start_time = time.time()
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("flowergray.png",grayimage)
print("%s seconds" % (time.time() - start_time))
