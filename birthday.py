import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import random
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

COMPANY_NAME = os.environ.get("COMPANY_NAME")
SLACK_HOOK_URL = os.environ.get("SLACK_HOOK_URL")


# Function to generate a random birthday greeting

def generate_birthday_greeting(name):
    greetings = [
        f"Happy Birthday, {name}! 🎉🎂 On this special day, {COMPANY_NAME} wishes you an abundance of joy, love, and all the things you cherish most. May your year ahead be filled with exciting adventures, personal growth, and the fulfillment of your dreams. You deserve nothing but the best!",
        f"Happy Birthday, {name}! 🎈🎁 Today marks another chapter in your remarkable journey, and {COMPANY_NAME} is grateful to be a part of it. May the coming year bring you moments of pure happiness, countless opportunities, and the strength to overcome any challenges. Wishing you a fantastic day!",
        f"Happy Birthday, {name}! 🎂🎉 Your birthday is a reminder of the incredible person you are and all the positive energy you bring into the world. As you celebrate another year of life, may it be filled with laughter, love, and unforgettable memories. Here's to a year of growth and achievements with {COMPANY_NAME}!",
        f"Happy Birthday, {name}! 🥳🎂 Another year has passed, and it's a perfect time to reflect on your accomplishments and set new goals for the future. May your birthday be the start of a new chapter filled with boundless opportunities, good health, and the fulfillment of your deepest desires. {COMPANY_NAME} is excited to celebrate with you!",
        f"Happy Birthday, {name}! 🎊🍰 Today, we celebrate the wonderful person you are and the positive impact you have on everyone around you. May your special day be a mosaic of joy, laughter, and love, surrounded by your closest friends and family. Here's to a year of unforgettable moments with {COMPANY_NAME}!",
        f"Happy Birthday, {name}! 🎉🎁 On your birthday, {COMPANY_NAME} wants to express appreciation for your friendship and the incredible person you are. May your year ahead be filled with amazing experiences, personal growth, and all the happiness your heart can hold. You deserve every joy in the world!",
    ]
    return random.choice(greetings)

# Function to check and send birthday greetings


def send_birthday_greetings(name, dob):
    today = datetime.date.today()
    if today.month == dob.month and today.day == dob.day:
        # It's the same month and day, so it's the birthday
        message = generate_birthday_greeting(name)
        payload = {
            "text": message,
            "unfurl_links": True,
            "channel": "#general",
        }
        response = requests.post(
            SLACK_HOOK_URL,
            json=payload,
        )
    else:
        message = f"{name}'s birthday is on {dob}"
        print(message)


# Loop through the dictionary and send greetings
def lambda_handler(event=None, args=None):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    # Replace 'birthday.json' with the path to your service account key JSON file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'birthday.json', scope)

    gc = gspread.authorize(credentials)

    # Open the Google Sheets spreadsheet by its title
    # Replace with your spreadsheet title
    spreadsheet_title = 'Employees DOB'
    worksheet_name = 'Employee Info'  # Replace with the name of the worksheet
    worksheet = gc.open(spreadsheet_title).worksheet(worksheet_name)

    # Read data from the worksheet
    data = worksheet.get_all_records()

    # Dictionary to store names and birthdays
    birthdays = {}

    for row in data:
        name = row['Name']
        dob_str = row['DOB']
        dob = datetime.datetime.strptime(dob_str, "%d/%m/%Y").date()
        birthdays[name] = dob

    if birthdays.items():
        for name, dob in birthdays.items():
            send_birthday_greetings(name, dob)


lambda_handler()
