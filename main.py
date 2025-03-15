import requests

# Replace with your actual Facebook credentials
ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN"
PAGE_ID = "YOUR_PAGE_ID"

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Post was successful!")
    else:
        print("Error posting to Facebook:", response.text)

# Example usage
post_to_facebook("Testing my new BookBot assistant!")
