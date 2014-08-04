from twython import Twython

APP_KEY = 
APP_SECRET = 

OAUTH_TOKEN = 
OAUTH_TOKEN_SECRET = 

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def send(name)
	photo = open("""C:\Pyhon33\Bambus\"""+name+".jpg", 'rb')
	twitter.update_status_with_media(status=name, media=photo)
	photo.close()

    

