# IDOR in marketing calendar tool

## Report Details
- **Report ID**: 797685
- **URL**: https://hackerone.com/reports/797685
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-16T17:18:34.404Z
- **Disclosed**: 2020-04-02T09:35:56.290Z

## Reporter
- **Username**: a_d_a_m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
#INTRODUCTION

##_I used two accounts to search for this vulnerability:_
**Id:** █████ **Email:** ██████
**Id:** ███ **Email:** ███

##_IP used:_
**78.194.169.36**

##_Endpoint URL:_
https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=CALENDAR_ID

#EXPLOITATION

##_Description of Security Issue:_
When a marketing calendar is loaded in the browser, the site sends a request such as this: {F718449}.
This request returns information such as if the owner has connected a google analytic account and the owner's user id associated with the calendar with the id pass in parameter. The problem comes from the fact that it is not verified that the user making the request has the calendar or that the person is invited to consult it.

#RESOLUTION
Check that the user making the request has the calendar or that the person is invited to consult the calendar.

## Impact

##_Exploit scenario for this vulnerability:_

 - A user such as a concurrent service could by bruteforcing the "calendar_id" parameter establish a list of all calendars and the number of unique users who have created calendars. It will also know the number of users who have connected their google analytic account on it. This represents bussiness data.

 - A user who knows someone's user_id (because he was invited to a calendar owned by the victim for example) can by bruteforcing the parameter "calendar_id" establish the number of calendar owned by the victim and the number of calendar being linked to a google analytic account.

## Attachments
- Capture.PNG
