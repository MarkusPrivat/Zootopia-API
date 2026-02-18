import os
from dotenv import load_dotenv
import requests


# Checks for API KEY in .env
load_dotenv()
NINJA_API_KEY = os.getenv("NINJA_API_KEY")
if NINJA_API_KEY is None:
    raise ValueError("NINJA_API_KEY environment variable not set in .env file")


def request_animals_data(name: str = 'fox'):
    """
    Request data from API-Ninja V1 animals API.
    The API returns up to 10 results matching the input name parameter.
    :param name: str to search with the animals API default = 'fox'
    :return: List of dictionaries containing animals data
    """
    animals = requests.get(
        f"https://api.api-ninjas.com/v1/animals?name={name}",
        headers={"X-Api-Key": NINJA_API_KEY}
    ).json()
    return animals


def main():
    """
    Main function
    :return: None
    """
    print(request_animals_data())


if __name__ == '__main__':
    main()