import requests
import argparse
from zad4 import Brewery

def get_breweries(city=None):
    base_url = 'https://api.openbrewerydb.org/breweries'
    params = {'per_page': 20}
    if city:
        params['by_city'] = city

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return [Brewery(brewery_data) for brewery_data in data]
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def print_breweries():
    parser = argparse.ArgumentParser(description="Fetch brewery information from Open Brewery DB API.")
    parser.add_argument('--city', help='Filter breweries by city')

    args = parser.parse_args()
    city_filter = args.city

    breweries = get_breweries(city=city_filter)

    if breweries:
        for brewery in breweries:
            print(brewery)

print_breweries()

# python zad5.py --city Washington