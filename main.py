import argparse
import requests


# We are creating an app that takes in a zip and returns the weather accordingly using a weather API.
# This will work with a correct API call.

def valid_zip(user_input):
    while True:
        if not user_input.isnumeric():
            user_input = input("That was not a number. Please input a Zip code: ")
        elif len(user_input) != 5:
            user_input = input("That is not a valid zip code. Please input a 5-digit zip code: ")
        else:
            return user_input


def get_weather(zip_code):
    url = f"https://api.weather.gov/points/{zip_code}/forecast"

    #user_agent
    headers = {'User-Agent': 'Xonze'}

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        forecast = data['properties']['periods'][0]['detailedForecast']

        return forecast

    else:
        print("Failed to retrieve weather.")
        print(response.status_code)
        return None


def main():
    parser = argparse.ArgumentParser(description='Get weather forecast based on ZIP code.')
    parser.add_argument('zip_code', metavar='ZIP', type=str, nargs='?', help='ZIP Code')
    args = parser.parse_args()

    if args.zip_code:
        zip_code = valid_zip(args.zip_code)
    else:
        zip_code = valid_zip(input("Please input a zip code: "))

    forecast = get_weather(zip_code)

    if forecast:
        print("Weather forecast", forecast)


if __name__ == "__main__":
    main()
