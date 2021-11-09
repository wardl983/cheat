import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint# + query

response = requests.get(url)
breeds = response.json()["message"]

# get a list of all breeds from the API call
all_breeds= breeds.keys()

# loop and print out each key
for breed in all_breeds:
  print(breed)

# get a list of all subbreeds of a breed with at least 3 sub-breeds but NOT bulldogs
# Examples include: poodles, retrievers, terriers, mastiffs, spaniels, setters, & more

# Display all bulldog subbreeds
bulldog_subreeds = breeds["bulldog"]
input("\nPress enter to get all bulldog subbreeds")
for sub in bulldog_subreeds:
  print(sub)