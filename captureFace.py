import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    # Read the frame
    _, img = camera.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    #faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        image= cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('imgage', img)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = img[y:y + h, x:x + w] 
        #cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color) 
    
    # Stop if escape key is pressed
    k = cv2.waitKey(10) & 0xff
    if k==13: 
        break    

cv2.imwrite('Detected_Face.jpg', roi_color) 
camera.release()
cv2.destroyAllWindows()   