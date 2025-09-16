import requests

target = requests.get('https://www.google.com')

print(target.status_code)

print(target.headers['content-type'])

print(target.encoding)

print(target.text)

print(target.json)