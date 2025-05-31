# Password protected rooms total number of viewers disclosure to unauthorized members

## Report Details
- **Report ID**: 411822
- **URL**: https://hackerone.com/reports/411822
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-20T14:55:50.541Z
- **Disclosed**: 2018-09-24T11:22:44.646Z

## Reporter
- **Username**: batee5a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##
Password protected rooms are supposed to be completely private, no information should be exposed if you do not have the room's password, and the UI looks like this.

{F348826}

However, through the following endpoint, It is possible to know the total number of viewers of the room even if it is password protected.
https://chaturbate.com/contest/log/{Username}/

## Steps To Reproduce:

  1.  Create a profile and add a Password to the room, lets say for testing purposes the username is "batee5a123" which is my test username.
  2. Go to users and refresh the user list (Just to make sure your are synced) and see yourself there

{F348830}

  3. Open an Incognito instance in your web browser and visit the following endpoint:
https://chaturbate.com/contest/log/batee5a123/ Or whatever your username is instead of "batee5a123", You'll find the total number of viewers there.

{F348824}

  4. For further testing, I made a second account and gave it the password and logged in, then from another browser instance I visited the same endpoint to see it is enumerating the total views and that it increased to 2 after joining with my other test account.

{F348825}

## Impact

Password protected rooms are supposed to be completely private with no exposure of any information what so ever, If even the least information exposed could be used in social engineering or blackmailing any chaturbate user.

The correct response for this matter should be like this (always give zero):

{F348823}

Or show Unauthorized message.

## Attachments
- pp1.png
- pp2.png
- pp3.png
- pp5.png
