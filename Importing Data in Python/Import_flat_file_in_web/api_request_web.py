import requests

url = 'http://www.omdbapi.com?apikey=72bc447a&t=the+social+network'
#second url api
# url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'


# pull the data into web
r = requests.get(url)

# convert into json type
json_data = r.json()

# print in text
# print(r.text)
print(json_data['Title'])
#or
# for key in json_data.keys(): 
#     print(key + ": ", json_data[key])
