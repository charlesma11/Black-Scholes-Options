import requests
import config
import sys

headers = {'Authorization': 'Bearer {}'.format(config.ACCESS_TOKEN), 
        'Accept': 'application/json'
}
options_url = '{}markets/options/chains'.format(config.API_BASE_URL)

response = requests.get(options_url,
    params={'symbol': 'TSLA', 'expiration': '2020-12-18', 'greeks': 'true'},
    headers=headers
)
json_response = response.json()

sys.stdout = open("tsla.txt", "w")

print(json_response)

sys.stdout.close()

tsla_call_symbol = "TSLA201218C00014000"
# response = requests.get('{}markets/quotes'.format(config.API_BASE_URL),
#     params={'symbols': 'AAPL', 'greeks': 'false'},
#     headers={'Authorization': 'Bearer {}'.format(config.ACCESS_TOKEN), 'Accept': 'application/json'}
# )
# json_response = response.json()
# print(response.status_code)
# print(json_response)