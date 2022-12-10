import cv2

#이미지 파일 읽기
image = cv2.imread('C:/Users/LG/image/para.jpg')
#cascade 파일 읽기
cascade = cv2.CascadeClassifier("C:/Users/LG/haarcascade_frontalface_default.xml")

face_list = cascade.detectMultiScale(image, scaleFactor=1.11, minNeighbors=4, minSize=(50, 50), maxSize = (55,55))

if len(face_list) > 0:    
  color = (0, 0, 255)       # 선글라스 색깔 빨강
  for face in face_list:    # 여러명 얼굴 인식 for문
    x, y, w, h = face       # 얼굴인식 좌표 설정
    # 사각형 그리기 & 사각형 크기 할당
    cv2.rectangle(image,(x,y+int(h/28*8)),(x+w,y+int(h/28*13)),color,-5)

else:
  print("none") 

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()