import dropbox

"""
Uploads the file to dropbox
Generates download link
Returns download link
https://www.dropbox.com/developers/core/docs/python
"""

def upload(name)

	app_key = 'xasdu3mcasb28iq'
	app_secret = '038cznmg68x1aft'
	token =
	#flow = dropbox.client.DropboxOAuth2FlowRedirect(app_key, app_secret)
	client = dropbox.client.DropboxClient(token)

	f = open("""C:\Python33\Bambus\Golden.jpg""", 'rb')
	response = client.put_file('/Golden.jpg', f)
	print("uploaded: ", response)
	f.close()

	x = client.share('/Golden.jpg')
	print(x)
	print("You can find the file at:")
	print(x["url"])

	return(x["url"])
