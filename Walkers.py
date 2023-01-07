import cv2

img = cv2.imread("boy.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boddy_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

boddies = boddy_classifier.detectMultiScale(gray)
print(boddies)

for (x,y,w,h) in boddies:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       cv2.imwrite("class.png",img[y:y+h,x:x+w])       
             
cv2.imshow('img',img)
cv2.waitKey(0)
