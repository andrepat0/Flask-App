import requests

# Define the URL of your Flask API endpoint
url = "http://127.0.0.1:5000/analyze"

# Define the input data
data = {
    "text": "I love using Hugging Face models!"
}

try:
    # Make a POST request to the API
    response = requests.post(url, json=data)

    # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()

    try:
        # Try to parse the JSON response
        response_json = response.json()
        print("Response JSON:", response_json)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON:", response.text)

except requests.exceptions.RequestException as e:
    # Handle any request exceptions (network issues, server errors, etc.)
    print(f"An error occurred: {e}")
