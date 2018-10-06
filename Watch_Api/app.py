import requests, json
 
url = "https:http://birdclassifier.herokuapp.com/api"
data = json.dumps({'sl':32.1, 'pl':32.1, 'ws':32.1})

response = requests.post(url,data)

print(response.text)

print("************DONE***********")

