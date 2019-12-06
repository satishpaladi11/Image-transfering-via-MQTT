import paho.mqtt.client as mqtt
import base64
import cv2
#cap=cv2.VideoCapture(1)
def convertImageToBase64(img):
    with open(img, "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        return encoded

    
mqtt.Client.connected_flag=False #create flag in class
broker="192.168.29.124"
client = mqtt.Client()   
client.connect(broker,1883,60)
while True:
    client.publish("sam",convertImageToBase64("photo.jpg"))


'''
while True:
    rect, frame = cap.read()
    retval, buffer = cv2.imencode('.jpg', frame)
'''    
    
'''    
cap.release
cv2.destroyAllWindows()
'''
