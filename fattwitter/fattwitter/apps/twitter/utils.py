import twitter 
import pdb
import pprint 


#pdb.set_trace()
api = twitter.Api(
	consumer_key = 'Pol2iZmpYph5qIHhAuaWmf5cL',
	consumer_secret = 'lcrhY1FH13frrmv5LzGeWLfV9ADNwYDSBBlqiWuIUue9MG5erH', 
	access_token_key = '15492735-X3aFd7rLKjzTArONRrOeQ9nI1pKkaQDg2HHiVFLpq', 
	access_token_secret = 'fHIjLJgknmU3tpxTX4VTIRgXPzfdugIEmu2oV4G6Fn1x4'
)

verify_credentials_dict = {}

try:
	verify_credentials_dict =  api.VerifyCredentials()
except Exception, e:
	print e[0][0]['code'] == 32 # Is not authenticated with 



result = api.GetHomeTimeline()
for status in result:
	pdb.set_trace()





