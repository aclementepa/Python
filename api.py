import requests
from requests.models import HTTPBasicAuth


response = requests.get("http://api.open-notify.org/astros.json")
print(response)

print("content: " + response.content())
print("text: " + response.text())
print("json: " + response.json())

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

response = requests.post('https://httbin.org/post', data = {'key':'value'})
requests.put('https://httpbin.org/put', data = {'key':'value'})
print(response.json())

print(response.headers["date"])

# http errors
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
elif (response.status_code == 404):
    print("Result not found!")

# above should return error 404

# If you want requests to raise an exception for all error codes (4xx and 5xx), 
# you can use the raise_for_status() function and catch specific errors using Requests built-in exceptions. 

try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)