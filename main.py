import pic_it
import tweet_it
import txt_it
import drop_it
import pin
import time


"""
This is the main program that will use pin to id inputer from raspberry pi using RPi.GPIO
If input from IR motion sensor is positive, camera will be activated, photo snapped and saved locally
Photo will be tweeted and then uploaded to dropbox
A text message using Twilio will be sent to contact list with twitter link and dropbox direct link
"""


#while True():

for z in range(15)

	print("Sensor null, run = {0}".format(z))

	if pin.status:
		time_snap = "{0}:{1}".format(time.localtime().tm_hour, time.localtime().tm_min)
		name = "Bambus_pije_o: " + time
		
		pic_it.snap(name)
		tweet_it.send(name)
		drop_it.upload(name)
		
		txt_it.go(name)
	
	time.sleep(5)

		
		
		
		
	


