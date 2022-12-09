import requests
import datetime
import time

# Replace this with your actual access token - You can get one from https://developer.twitter.com
access_token = ""
# Ask user for a username to look up
username = input("Enter a username to look up: ")
#Twitter's V2 API allows for 300 requests per 15 minutes, that translates to 5 seconds per request. Change this to a higher number if you get rate limited.
seconds = 5

while True:
  # generate a timestamp to use in the response message
  current_time = datetime.datetime.now()
  # use 'requests' library to make the request and see if the name is available
  resp = requests.get(
    f"https://api.twitter.com/2/users/by/username/{username}",
    headers={"Authorization": f"Bearer {access_token}"}
  )

  # Check the response to see if it contains "Could not find user with username" or not
  if "Could not find user with username" in resp.text:
    # If the message is in the response, the username is available and we should print that in bright green
    print(current_time.strftime("%H:%M:%S") + ": \033[32mAVAILABLE!\033[0m")
  else:
    # If the message is not in the response, the username is unavailable. Boo.
    print(current_time.strftime("%H:%M:%S") + ": \033[31mUnavailable\033[0m")

    # Uncomment the line below to print the full response from the API - this would be for debugging purposes.
    # print(resp.json())

  # We want to run this on a loop of x seconds
  time.sleep(5)
