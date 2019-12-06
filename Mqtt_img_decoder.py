import paho.mqtt.client as mqtt
import base64
import cv2

def convertImageToBase64(img_string):
    decoded=base64.decodestring(img_string)
    return decoded

def on_message(client, userdata, msg):
    mesg = msg.payload.decode()
    frame=convertImageToBase64(mesg)
    print(type(frame))
    '''
    cv2.imshow('frame',frame)
    '''
        
    
mqtt.Client.connected_flag=False #create flag in class
broker="192.168.29.124"
client = mqtt.Client()
client.on_message=on_message
client.connect(broker,1883,60) 


client.loop_start()
client.subscribe("sam")



