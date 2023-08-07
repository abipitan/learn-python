# Find out what an API call is then make a call to the\
# Pokemon API to get some data
# Then I want you to create a program that gets different\
# Pokemon data from the API based on user input

import requests
response = requests.get("https://randomfox.ca/floof")

# print(response.status_code)
# this gives response object, usually is [200]
# print(response.text)
# {"image":"https:\/\/randomfox.ca\/images\/111.jpg","link":"https:\/\/randomfox.ca\/?i=111"}
# print(response.json())
# returns a new dictionary
# fox = response.json() # takes dictionary and puts it in fox object
# print(fox["image"])
# prints https://randomfox.ca/images/22.jpg

# api= application programming interface, it states the rules\
#  for interactions between systems, e.g weather app and weather data.
# or websites that allow you to create accounts.
# they have end points, inputs and unique api keys.
# UI connects to front end, and API connects front end to backend.
# UI = user, API = code

print(requests.content)