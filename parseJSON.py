import json

with open('./tracks.json') as tracks:
    data = json.load(tracks)

arr = set()
for i in data['trackArr']:
    arr.add(i['track']['id'])
print(arr)