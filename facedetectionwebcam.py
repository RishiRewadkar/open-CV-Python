import cv2

fc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray)

    for (x,y,w, h) in faces:
        cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow ('img',img)
    k = cv2.waitKey (30) & 0xff
    if k==27:
        break

cv2.release()
cv2.destroyAllWindows()
