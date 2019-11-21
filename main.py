import random
import time
import os
import requests
import json

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

token = "YOUR TOKEN"

while True:
  message = input("Enter message: ")
  message2 = message

  loop = ""
  for n in message:
      loop += n
      status_data = json.dumps(
          {
              "custom_status":
              {
                  "text": loop
              }
          }
      )

      r = requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={"Authorization": token, "Content-Type": "application/json"}, data=status_data)
      print(loop + "\r", end="")
      time.sleep(0.1)

  message = " " + message + " "

  for n in message:
      count = 2
      while count > 0:
          message += message[0]
          message = message[1:]
          count -= 1
          
          status_data = json.dumps(
              {
                  "custom_status":
                  {
                      "text": message
                  }
              }
          )

          r = requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={"Authorization": token, "Content-Type": "application/json"}, data=status_data)
          print(message + "\r", end="")
          time.sleep(0.09)

  message = message2

  for n in range(len(message)):
      message = message.replace(message[random.randint(0, len(message) - 1)], " ")
      status_data = json.dumps(
          {
              "custom_status":
              {
                  "text": message
              }
          }
      )

      r = requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={"Authorization": token, "Content-Type": "application/json"}, data=status_data)
      print(message + "\r", end="")
      time.sleep(0.2)
