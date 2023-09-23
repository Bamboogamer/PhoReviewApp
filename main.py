import smartsheet
import logging
import os

def getLogin():
    loginInfo = open("login.txt", "r") \
                 .readline() \
                 .split(";")

    return loginInfo[0], loginInfo[1], loginInfo[2]

print("Starting ...")

# Initialize client. Uses the API token in the environment variable "SMARTSHEET_ACCESS_TOKEN"
smart = smartsheet.Smartsheet(access_token=getLogin()[2])
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)


if __name__ == '__main__':
    pass