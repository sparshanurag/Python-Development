import requests
from send_email import send_email


topic = "tesla"
api_key = "921a15f6978740a5b6435509c61517ab"

url = "https://newsapi.org/v2/everything?" \
f"q={topic}&" \
"sortBy=publishedAt&" \
"apiKey=921a15f6978740a5b6435509c61517ab&" \
"language=en"

#Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = ""

# Initialize the 'body' variable
body = ""

# Loop through each article in the content
for article in content["articles"][:20]:
    # Ensure title, description, and url are strings
    title = article["title"] if article["title"] is not None else ""
    description = article["description"] if article["description"] is not None else ""
    url = article["url"] if article["url"] is not None else ""
    
    # Check if the title is not an empty string
    if title:
        # Concatenate the title, description, and URL to the body string
        body += "Subject: Today's news" + title + "\n" + description + "\n" + url + "\n\n"

print(body)



body = body.encode("utf-8")

send_email(message=body)