from urllib.request import urlopen
import json

url = "https://random.dog/woof.json"
response = urlopen(url)

if response.getcode() == 200:
    data = json.loads(response.read())
    image_url = data['url']
    print(image_url)
    img = urlopen(image_url)
    data = img.read()
    with open("dog.jpeg", "wb") as f:
        f.write(data)
else:
    print("Error fetching dog image")