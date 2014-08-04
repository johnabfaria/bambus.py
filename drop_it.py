import dropbox

app_key = 'xasdu3mcasb28iq'
app_secret = '038cznmg68x1aft'
token = '_bg2SsPqgsEAAAAAAAAAEGZBA4gaaF3Oo8UGa8_xnvQSGI3oofN7rFu_WlGUyG3K'

flow = dropbox.client.DropboxOAuth2FlowRedirect(app_key, app_secret)
client = dropbox.client.DropboxClient(token)
print(client.account_info())
