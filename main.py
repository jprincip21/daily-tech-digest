import requests
import json
import send_email

def main():
    with open("config.json") as f:
        config = json.load(f)

    api_key = config["api_key"] # Create a json file with your api key inside to use "api_key": *key*
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key

    # Make Request
    request = requests.get(url)

    # Get Dictionary with data
    content = request.json()

    message = ""

    # Access articles titles and descriptions
    for article in content["articles"]:
        if article["title"] is not None:
            message = message + article["title"] + "\n" + article["description"] + 2*"\n"

    message = message.encode("utf-8")
    send_email.send_email(message)

if __name__ == "__main__":
    main()