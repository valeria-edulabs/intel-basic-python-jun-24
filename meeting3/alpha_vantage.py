from urllib.request import urlopen
import json
from pprint import pprint

API_KEY = ""  # Get your free API key from Alpha Vantage
keyword = "INT"
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={API_KEY}'
result = urlopen(url)

http_response_code = result.getcode()
response_body = result.read()
response_as_dictionary = json.loads(response_body)

print(http_response_code)
print(response_body)
pprint(response_as_dictionary)


