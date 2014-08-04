from twilio.rest import TwilioRestClient 
 

def go(name):
	ACCOUNT_SID = "AC2ff2e876b84089d08d6390f68dfdba24" 
	AUTH_TOKEN = "70881c6f610f4ae6ab9697f9681feb5a" 
 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	
	client.messages.create(
	to="8474449672", 
	from_="+18474570275", 
	body= name,  
	)
 
 
