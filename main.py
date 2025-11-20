import requests
import json

def main():
    with open("config.json") as f:
        config = json.load(f)

    api_key = config["api_key"] # Create a json file with your api key inside to use
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key

    # Make Request
    request = requests.get(url)

    # Get Dictionary with data
    content = request.json()

    # Access articles titles and descriptions
    for article in content["articles"]:
        print(article["title"])
        print(article["description"])

if __name__ == "__main__":
    main()