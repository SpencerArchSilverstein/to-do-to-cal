from __future__ import print_function
import datetime
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


import os.path

from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('YOUR_TOKEN_FILE.json'):
    creds = Credentials.from_authorized_user_file('YOUR_TOKEN_FILE.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'YOUR_CREDENTIALS_FILE.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('YOUR_TOKEN_FILE.json', 'w') as token:
        token.write(creds.to_json())


#SCOPES = ['https://www.googleapis.com/auth/calendar']

CLIENT_SECRETS_FILE = '~/YOUR_CREDENTIALS_FILE.json'

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)

creds = flow.run_local_server(port=0)

creds = google.oauth2.credentials.Credentials.from_authorized_user_file('YOUR_CREDENTIALS_FILE.json', ['https://www.googleapis.com/auth/calendar'])

service = build('calendar', 'v3', credentials=creds)

CalendarMain = "primary"
CalendarA = "CALENDAR_A_LINK@group.calendar.google.com"
CalendarB = "CALENDAR_B_LINK@group.calendar.google.com"
CalendarC = "CALENDAR_C_LINK@group.calendar.google.com"
CalendarD = "CALENDAR_D_LINK@group.calendar.google.com"

line_num = 0

classnames_MAIN = ["General"]
classnames_A = ["CLASSA"]
classnames_B = ["CLASSB"]
classnames_C = ["CLASSC"]
classnames_D = ["CLASSD"]

def get_cal(subject):
    for sub in classnames_MAIN:
        if sub == subject:
            return CalendarMain
    for sub in classnames_A:
        if sub == subject:
            return CalendarA
    for sub in classnames_B:
        if sub == subject:
            return CalendarB
    for sub in classnames_C:
        if sub == subject:
            return CalendarC
    for sub in classnames_D:
        if sub == subject:
            return CalendarD


twenty_eight_days = ["2", "02"]
thirty_days = ["4", "04", "6", "06" "9", "09", "11"]
thirty_one_days = ["1", "01", "3", "03", "5", "05", "7", "07", "8", "08", "10", "12"]


def type_month(month):
    for m in twenty_eight_days:
        if m == str(month):
            return 28
    for m in thirty_days:
        if m == str(month):
            return 30
    for m in thirty_one_days:
        if m == str(month):
            return 31

def get_day(weekof, day, month):
    days_in_month = type_month(month)
    days_left = days_in_month - weekof
    day_offset = weekof
    new_month = month

    #25 26 27 28 29 30 1 #5 -> 30 - 25 = 5
    #26 27 28 29 30 1 2 #4 -> 30 - 26 = 4
    #27 28 29 30 1 2 3 #3 -> 30 - 27 = 3
    #28 29 30 1 2 3 4 #2 -> 30 - 28 = 2
    #29 30 1 2 3 4 5 #1 -> 30 - 29 = 1
    #30 1 2 3 4 5 6 #0 -> 30 - 30 = 0

    if days_left > 5:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset += 2
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset += 3
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset += 4
            return [new_month, day_offset]
        if day == "Friday" or day == "Fri":
            day_offset += 5
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset += 6
            return [new_month, day_offset]

    if days_left == 5:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset += 2
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset += 3
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset += 4
            return [new_month, day_offset]
        if day == "Friday" or day == "Fri":
            day_offset += 5
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]

    if days_left == 4:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset += 2
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset += 3
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset += 4
            return [new_month, day_offset]
        if day == "Friday" or day=="Fri":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 2
            new_month = month + 1
            return [new_month, day_offset]


    if days_left == 3:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset += 2
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset += 3
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Friday" or day == "Fri":
            day_offset = 2
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 3
            new_month = month + 1
            return [new_month, day_offset]


    if days_left == 2:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset += 2
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset = 2
            new_month = month + 1
            return [new_month, day_offset]
        if "Friday" or day == "Fri":
            day_offset = 3
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 4
            new_month = month + 1
            return [new_month, day_offset]

    if days_left == 1:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset += 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset = 2
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset = 3
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Friday" or day == "Fri":
            day_offset = 4
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 5
            new_month = month + 1
            return [new_month, day_offset]

    if days_left == 0:
        if day == "Sunday" or day == "Sun":
            return [new_month, day_offset]
        if day == "Monday" or day == "Mon":
            day_offset = 1
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Tuesday" or day == "Tues":
            day_offset = 2
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Wednesday" or day == "Wed":
            day_offset = 3
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Thursday" or day == "Thurs":
            day_offset = 4
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Friday" or day == "Fri":
            day_offset = 5
            new_month = month + 1
            return [new_month, day_offset]
        if day == "Saturday" or day == "Sat":
            day_offset = 6
            new_month = month + 1
            return [new_month, day_offset]



def clean_time(time):
    hour_time = [" hour", " hr", "hour", "hr", "HOUR", "HR", " HOUR", " HR"]
    for hr in hour_time:
        time = time.replace(hr, "")
    return time

def hour_split(hour):
    hourz = clean_time(hour)
    minute = 0
    hr = int(hourz)
    for char in hourz:
        if char == ".":
            my_hour = hourz.split(".")
            hr = int(my_hour[0])
            minute = 60 * (int(my_hour[1])/10)
    return [hr, minute]



with open('~/mock_calendar_input.txt', mode = 'r', encoding='utf-8-sig') as f:
    for line in f.readlines():
        data = line.strip()
        data = line.split(", ")
        #think about the edge case of if there's no space or two spaces
        print(f"data",data)
        if line_num == 0:
            month, weekof = data[0].split("/")
            month = int(month)
            weekof = int(weekof)
        else:
            hr, min = hour_split(data[2])
            start_time = datetime.datetime(2023, get_day(weekof, data[0], month)[0], get_day(weekof, data[0], month)[1], 9, 0, 0)
            end_time = datetime.datetime(2023, get_day(weekof, data[0], month)[0], get_day(weekof, data[0], month)[1], 9 + hr, min, 0)
            event = {
                    'summary': data[3],  # Event title
                    'location': "ENTER_YOUR_LOCATION",  # Event location
                    'description': data[4],  # Event description
                    'start': {
                        'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                        'timeZone': 'ENTER_YOUR_TIMEZONE',  # Timezone of the event
                    },
                    'end': {
                        'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                        'timeZone': 'ENTER_YOUR_TIMEZONE',
                    },
                }
            event = service.events().insert(calendarId=get_cal(data[1]), body=event).execute()
        line_num += 1
