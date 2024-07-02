from urllib.request import urlopen
import json
import os

url = "https://random.dog/woof.json"
dir = "dogs/images"
os.makedirs(dir)
count = 0
while count < 10:
    response = urlopen(url)

    if response.getcode() == 200:
        data = json.loads(response.read())
        image_url: str = data['url']
        size = data['fileSizeBytes']
        print(image_url, size)

        if image_url.lower().endswith(".jpg") or image_url.lower().endswith("jpeg"):
            count += 1
            # os.path.splitext(image_url)
            # Download the picture
            img_response = urlopen(image_url)
            if img_response.getcode() == 200:
                data = img_response.read()
                # print(data)
                with open(f"{dir}/dog_{count}.jpeg", "wb") as f:
                    f.write(data)
    else:
        print("Error fetching dog image")