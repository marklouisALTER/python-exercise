import requests

# create a variable to store the url
url = "http://www.datacamp.com/teach/documentation"

# we use get request to get the url
r = requests.get(url)

# assign to text variable the response: r then text
text = r.text

#print the text
print(text)