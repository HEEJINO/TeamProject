import cv2

imgfile = 'C:/Users/LG/image/bts.jpg'
cascade_file = "C:/Users/LG/haarcascade_frontalface_default.xml"

image = cv2.imread(imgfile)
cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade.detectMultiScale(image, scaleFactor=1.11, minNeighbors=4, minSize=(50, 50), maxSize = (55,55))

if len(face_list) > 0:    
  color = (0, 0, 255)
  for face in face_list:
    x, y, w, h = face
    # 사각형 그리기
    cv2.rectangle(image,(x,y+int(h/28*8)),(x+w,y+int(h/28*13)),color,-5)

else:
  print("none") 

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()