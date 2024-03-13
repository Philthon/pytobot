import requests


def request_message_from_website():
    url = "https://pytobot-website.vercel.app/api/desktopMessage"

    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print("Error occurred while making request:", e)

    return response


if __name__ == "__main__":
    response = request_message_from_website()
    print(response.text)
