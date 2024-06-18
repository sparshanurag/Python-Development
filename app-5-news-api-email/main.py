import requests

api_key = "921a15f6978740a5b6435509c61517ab"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-18&sortBy=publishedAt&apiKey=921a15f6978740a5b6435509c61517ab"

#Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])