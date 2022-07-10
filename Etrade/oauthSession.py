import logging, pickle, json
from rauth import OAuth1Service

logger = logging.getLogger('testing_logger')
logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler('oauthTesting.log', mode='w')
handler = logging.FileHandler('oauthSession.log')
logger.addHandler(handler)
logger.debug('--------------')

base_url = 'https://api.etrade.com'

etrade = OAuth1Service(
    name="etrade",
    consumer_key='97b529bd9d7e1c757f6bd9b33e3a8e34',
    consumer_secret='8a3da2b90e1d091478465bae480bdebd091c71a687512a654747f0f7e22bce5c',
    request_token_url="https://api.etrade.com/oauth/request_token",
    access_token_url="https://api.etrade.com/oauth/access_token",
    authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
    base_url=base_url)

with open('oauth_session_data.pickle', 'rb') as f:
    oauth_session_data_get = pickle.load(f)

print('------------')
print(type(oauth_session_data_get[0]))
print(oauth_session_data_get[0])
print(type(oauth_session_data_get[1]))
print(oauth_session_data_get[1])
print(type(oauth_session_data_get[2]))
print(oauth_session_data_get[2])

session = etrade.get_auth_session(oauth_session_data_get[0],
    oauth_session_data_get[1],
    params={"oauth_verifier": oauth_session_data_get[2]})

# url = base_url + "/v1/market/quote/VITAX.json"
# logger.debug('HTTP GET: %s' % url)
# response = session.get(url)
# if response is not None and response.status_code == 200:
#     parsed = json.loads(response.text)
#     logger.debug('Response Body:\n%s' % json.dumps(parsed, indent=4, sort_keys=True))
