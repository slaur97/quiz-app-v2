import requests

json={}

response=requests.get("https://opentdb.com/api.php?amount=40&category=21&difficulty=easy&type=multiple")
response.raise_for_status()
data=response.json()['results']

