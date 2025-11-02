import requests

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        return joke_data.get("value")
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"

if __name__ == "__main__":
    joke = get_random_joke()
    print("Here's a random Chuck Norris joke:")
    print(joke)
