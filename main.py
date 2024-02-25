import argparse

# We are creating an app that takes in a zip and returns the weather accordingly using an weather API.

# def valid_zip(user_input):
#   while True:
#       if not user_input.isnumeric():
#          user_input = input("That was not a number. Please input a Zip code: ")
#     elif len(user_input) != 5:
#        user_input = input("That is not a valid zip code. Please input a 5-digit zip code: ")
#   else:
#      return user_input

def main():
    parser = argparse.ArgumentParser(description='Get weather forecast based on ZIP code.')
    parser.add_argument('zip_code', metavar='ZIP', type=str, nargs='?', help='ZIP Code')
