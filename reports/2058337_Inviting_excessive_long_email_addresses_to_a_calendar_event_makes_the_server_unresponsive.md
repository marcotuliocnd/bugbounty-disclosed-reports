# Inviting excessive long email addresses to a calendar event makes the server unresponsive

## Report Details
- **Report ID**: 2058337
- **URL**: https://hackerone.com/reports/2058337
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-09T05:36:23.676Z
- **Disclosed**: 2023-10-16T13:50:04.871Z

## Reporter
- **Username**: shuvam321
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Due to the absence of a character limit in the email address field when sending emails, requests containing lengthy email addresses causes the server to get delay response, ultimately resulting in a denial of service.


## Steps To Reproduce:
1. As, a low privileged user, go to https://serveraddress/apps/calendar/dayGridMonth/now and create a new calendar.

{F2480561}

2. Click on Share link, click on share calendar link via email and intercept the request in burp entering a random email.

3. Send the request to repeater and observe the response time. The server will respond in ~600ms.

{F2480573}

{F2480610}

4. Now, use the attached payload of 50 MB (email_recipient.txt) in email and send the response. You will get response in about 10000 milllisecond. Larger the email length, longer will be the reponse time.



{F2480615}

[Note: you may use the following python script and payload attached below. POC attached :) ]

## Impact

Denial of service

## Attachments
- Screenshot_at_2023-07-09_10-28-20.png
- Screenshot_at_2023-07-09_10-44-28.png
- email_recipient.txt
- Screenshot_at_2023-07-09_11-19-00.png
- Screenshot_at_2023-07-09_11-19-47.png
- time.py
- simplescreenrecorder-2023-07-09_11.16.07.mkv
