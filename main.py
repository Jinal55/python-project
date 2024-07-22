import cv2

img = cv2.imread("plant.jpg", cv2.IMREAD_UNCHANGED)
# r represents raw string it treats \ in path as literal characters
scale_percent = int(input("enter scale percent"))
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(img, dsize)
cv2.imwrite("plant.jpg", output)
cv2.imshow("plant image", img)
cv2.waitKey(0)
