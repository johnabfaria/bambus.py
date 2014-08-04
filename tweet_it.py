from twython import Twython

APP_KEY = 'u48b5AGW9RxJwkM2IsJHYn8Hg'
APP_SECRET = 'RdzWbiNK0e3Hr0dNs7JCJT3VBwhg5i7JgqwQQ2Ckk5uf6SC6dJ'

OAUTH_TOKEN = '801097652-DkCvT8a7LD5RlRNTvXP8FP2pAYOYg7BNEouW9HsS'
OAUTH_TOKEN_SECRET = 'OrlEWnda2oozLGvbOc2GPteTEv8Vti93xIBWhBJ8T38lZ'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def send(name)
	photo = open("""C:\Pyhon33\Bambus\"""+name+".jpg", 'rb')
	twitter.update_status_with_media(status=name, media=photo)
	photo.close()

    

