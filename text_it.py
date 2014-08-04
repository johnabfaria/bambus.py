from twilio.rest import TwilioRestClient 
 

def go(name):
	ACCOUNT_SID =
	AUTH_TOKEN = 
 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	
	client.messages.create(
	to="8474449672", 
	from_="+18474570275", 
	body= name,  
	)
 
 
