import logging, json, pickle
import configparser
import webbrowser
# from logging.handlers import RotatingFileHandler
from rauth import OAuth1Service

# loading configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# logger settings
logger = logging.getLogger('testing_logger')
logger.setLevel(logging.DEBUG)
# handler = RotatingFileHandler("testing.log", maxBytes=5*1024*1024, backupCount=3)
handler = logging.FileHandler('testingC.log', mode='w')
# handler = logging.FileHandler('testing.log')
# FORMAT = "%(asctime)-15s %(message)s"
# fmt = logging.Formatter(FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
# handler.setFormatter(fmt)
logger.addHandler(handler)

etrade = OAuth1Service(
    name="etrade",
    consumer_key=config["DEFAULT"]["CONSUMER_KEY"],
    consumer_secret=config["DEFAULT"]["CONSUMER_SECRET"],
    request_token_url="https://api.etrade.com/oauth/request_token",
    access_token_url="https://api.etrade.com/oauth/access_token",
    authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
    base_url="https://api.etrade.com")

base_url = config["DEFAULT"]["PROD_BASE_URL"]

# Step 1: Get OAuth 1 request token and secret
request_token, request_token_secret = etrade.get_request_token(
    params={"oauth_callback": "oob", "format": "json"})

# Step 2: Go through the authentication flow. Login to E*TRADE.
# After you login, the page will provide a text code to enter.
authorize_url = etrade.authorize_url.format(etrade.consumer_key, request_token)
webbrowser.open(authorize_url)
text_code = input("Please accept agreement and enter text code from browser: ")

# Step 3: Exchange the authorized request token for an authenticated OAuth 1 session
session = etrade.get_auth_session(request_token,
                                request_token_secret,
                                params={"oauth_verifier": text_code})

# params = {'detailFlag': 'MF_DETAIL'}
# headers = {'Connection': 'close'}

# # Make API call for GET request
# symbols = 'VITAX'
# url = base_url + "/v1/market/quote/" + symbols + ".json"
# logger.debug("HTTP GET      : %s", url)
# # response = session.get(url, params=params, headers=headers)
# response = session.get(url)
# logger.debug("Request Header: %s", response.request.headers)
# logger.debug("Status Code   : %s", response.status_code)
# if response is not None and response.status_code == 200:
#     testje = response.json
#     response.
#     parsed = json.loads(response.text)
#     logger.debug("testje       : %s", json.dumps(parsed, indent=4, sort_keys=True))
#     logger.debug("parsed       : %s", json.dumps(parsed, indent=4, sort_keys=True))
#     logger.debug("Response Body: %s", json.dumps(parsed, indent=4, sort_keys=True))

# # Make API call for GET request
# symbols = 'ABIMX'
# url = base_url + "/v1/market/quote/" + symbols + ".json"
# logger.debug("HTTP GET      : %s", url)
# # response = session.get(url, params=params, headers=headers)
# response = session.get(url)
# logger.debug("Request Header: %s", response.request.headers)
# logger.debug("Status Code   : %s", response.status_code)

# if response is not None and response.status_code == 200:
#     parsed = json.loads(response.text)
#     logger.debug("Response Body: %s", json.dumps(parsed, indent=4, sort_keys=True))

# url = base_url + "/v1/market/quote/ABIMX.json"
url = base_url + "/v1/market/quote/VITAX.json"
# params = {'detailFlag': 'ALL'}
params = {'detailFlag': 'MF_DETAIL'}
logger.debug('HTTP GET: %s' % url)
response = session.get(url, params=params)
# response = session.get(url)
if response is not None and response.status_code == 200:
    parsed = json.loads(response.text)
    logger.debug('Response Body:\n%s' % json.dumps(parsed, indent=4, sort_keys=True))
    data = response.json()
    with open('ABIMX.pickle', 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    if 'QuoteResponse' in data:
        qdata = data['QuoteResponse']['QuoteData']
        logger.debug('QuoteData type: %s' % type(qdata))

else:
    logger.debug('Unsucsessful HTTP GET: %s' % url)

with open('ABIMX.pickle', 'rb') as f:
    data = pickle.load(f)

if 'QuoteResponse' in data:
    qdata = data['QuoteResponse']['QuoteData']
    for qitem in qdata:
        if 'Product' in qitem:
            logger.debug('Product.symbol      : %s' % qitem['Product']['symbol'])
            logger.debug('Product.securityType: %s' % qitem['Product']['securityType'])

