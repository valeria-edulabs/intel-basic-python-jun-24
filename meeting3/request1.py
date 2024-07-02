from urllib.request import urlopen

response = urlopen("https://google.com")

data = response.read()
print(str(data))
