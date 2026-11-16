import requests

url ="https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Joke:", data["setup"])
    print("Answer:", data["punchline"])

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Internet connection error!")

except requests.exceptions.HTTPError :

    print("Joke: Why did the computer gp to school?:")
    print("Answer: To improve its skills !")

except requests.exceptions.RequestException as e:
    print("Error:", e)

except ValueError:
    print("Invalid JSON data!")