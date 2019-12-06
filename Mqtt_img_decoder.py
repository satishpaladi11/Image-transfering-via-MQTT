#For MQTT connection
import paho.mqtt.client as mqtt
#For encoding the image to ASCII format
import base64
#Image processing library for showing the image
import cv2

#Function for converting the image file to Base64 format
def convertImageToBase64(img_string):
    decoded=base64.decodestring(img_string)
    return decoded

#Function for recieving the mqtt images
def on_message(client, userdata, msg):
    mesg = msg.payload.decode()
    frame=convertImageToBase64(mesg)
    cv2.imshow('frame',frame)
        
#Replace your ipaddress at YOUR_MQTT_BROKER
mqtt.Client.connected_flag=False #create flag in class
broker="YOUR_MQTT_BROKER"
client = mqtt.Client()
client.on_message=on_message
client.connect(broker,1883,60) 

#Can change the topic at TOPIC
client.loop_start()
client.subscribe("TOPIC")



