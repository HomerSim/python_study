import cv2
import requests
import numpy
from PIL import Image


# PIL RGB, width : height
# OPENCV BGR height: width

pil_image = Image.open("sample.jpg")
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

cv2.imshow("a", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# url = "https://cdn.pixabay.com/photo/2020/04/11/14/42/historic-center-5030692_960_720.jpg"
# arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8)
# img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

# cv2.imshow("A", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
