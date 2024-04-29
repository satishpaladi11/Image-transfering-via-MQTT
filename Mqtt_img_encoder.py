#For MQTT connection
import paho.mqtt.client as mqtt
#For encoding the image to ASCII format
import base64

#Function for converting the image file to Base64 format
def convertImageToBase64(img):
    with open(img, "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        return encoded

    
#Setting up the MQTT connection
#Changing the broker to your mqtt broker ipaddress at YOUR_MQTT_BROKER
mqtt.Client.connected_flag=False #create flag in class
broker="YOUR_MQTT_BROKER ex:(192.168.29.147)"
client = mqtt.Client()   
client.connect(broker,1883,60)


#You can change your topic at TOPIC
#Change your "photo.jpg" to your location of image
client.publish("TOPIC",convertImageToBase64("photo.jpg"))

#This is my code

