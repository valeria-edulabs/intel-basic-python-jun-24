from urllib.request import urlopen
import json

url = "https://random.dog/woof.json"
response = urlopen(url)

if response.getcode() == 200:
    data = json.loads(response.read())
    image_url = data['url']
    size = data['fileSizeBytes']
    print(image_url, size)

    # Download the picture
    img_response = urlopen(image_url)
    if img_response.getcode() == 200:
        data = img_response.read()
        print(data)
        with open("dog.jpeg", "wb") as f:
            f.write(data)
else:
    print("Error fetching dog image")