import logging, pickle
from rauth import OAuth1Service
import webbrowser

logger = logging.getLogger('testing_logger')
logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler('oauthTesting.log', mode='w')
handler = logging.FileHandler('oauthTesting.log')
logger.addHandler(handler)
logger.debug('--------------')

etrade = OAuth1Service(
    name="etrade",
    consumer_key='97b529bd9d7e1c757f6bd9b33e3a8e34',
    consumer_secret='8a3da2b90e1d091478465bae480bdebd091c71a687512a654747f0f7e22bce5c',
    request_token_url="https://api.etrade.com/oauth/request_token",
    access_token_url="https://api.etrade.com/oauth/access_token",
    authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
    base_url="https://api.etrade.com")

etradeTest = OAuth1Service(
    name="etrade",
    consumer_key='97b529bd9d7e1c757f6bd9b33e3a8e34',
    consumer_secret='8a3da2b90e1d091478465bae480bdebd091c71a687512a654747f0f7e22bce5c',
    request_token_url="https://api.etrade.com/oauth/request_token",
    access_token_url="https://api.etrade.com/oauth/access_token",
    authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
    base_url="https://api.etrade.com")

# request token, expires after 5 minutes
request_token, request_token_secret = etrade.get_request_token(
    params={"oauth_callback": "oob", "format": "json"})
logger.debug('request_token       : %s' % request_token)
logger.debug('request_token_secret: %s' % request_token_secret)

# authorize using token
authorize_url = etrade.authorize_url.format(etrade.consumer_key, request_token)
logger.debug('authorize_url:\n%s' % authorize_url)
webbrowser.open(authorize_url)
text_code = input("code: ")
logger.debug('text_code: %s' % text_code)

oauth_session_data = [request_token, request_token_secret, text_code]

print('------------')
print(type(request_token))
print(request_token)
print(type(request_token_secret))
print(request_token_secret)
print(type(text_code))
print(text_code)

print('------------')
print(type(oauth_session_data[0]))
print(oauth_session_data[0])
print(type(oauth_session_data[1]))
print(oauth_session_data[1])
print(type(oauth_session_data[2]))
print(oauth_session_data[2])

with open('oauth_session_data.pickle', 'wb') as f:
    pickle.dump(oauth_session_data, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('oauth_session_data.pickle', 'rb') as f:
    oauth_session_data_get = pickle.load(f)

print('------------')
print(type(oauth_session_data_get[0]))
print(oauth_session_data_get[0])
print(type(oauth_session_data_get[1]))
print(oauth_session_data_get[1])
print(type(oauth_session_data_get[2]))
print(oauth_session_data_get[2])

sessionTest = etrade.get_auth_session(oauth_session_data_get[0],
    oauth_session_data_get[1],
    params={"oauth_verifier": oauth_session_data_get[2]})

# session = etrade.get_auth_session(request_token,
#                                 request_token_secret,
#                                 params={"oauth_verifier": text_code})

# etrade.get_access_token(request_token, request_token_secret)