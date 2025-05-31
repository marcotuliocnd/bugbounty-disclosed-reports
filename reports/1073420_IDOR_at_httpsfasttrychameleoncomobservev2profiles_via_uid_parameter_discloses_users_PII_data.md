# IDOR at https://fast.trychameleon.com/observe/v2/profiles/ via uid parameter discloses users' PII data

## Report Details
- **Report ID**: 1073420
- **URL**: https://hackerone.com/reports/1073420
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-07T12:15:18.040Z
- **Disclosed**: 2021-02-03T16:56:02.718Z

## Reporter
- **Username**: cankat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:

Hello,

A API on apps.topcoder.com/forums/ exposes the email of any user on topcoder.com and some PIIs (name, surname, id).


## Steps To Reproduce:
1) Create a profile at topcoder.com
2) Go to apps.topcoder.com/forums and login forum
3) Entery any topic (example: https://apps.topcoder.com/forums/?module=Thread&threadID=966515&start=0)
4) Open Intercept and click "Watch Thread" button
5) Catch the request and send to repeater, it will look like this:
F1147918
(This request comes from fast.trychameleon.com, but fast.trychameleon.com is not the cause of the security vulnerability.)
6) Let's go into the profile of any user on topcoder.com. (this is my other user and target user: https://www.topcoder.com/members/nomadex41)
7) Press F12 and search(CTRL-F) "userID"
F1147928
8) Copy the "userID" value and replace it with the "uid" part in the HTTP request.
9) Also give a random value to the title of the request ( POST /observe/v2/profiles/randomvalue HTTP/1.1) and sumbit.
poC: F1147950

Leaked all topcoder users email, name, surname and profile_id information. 
This is not public visible to other users.

This vulnerability is not caused by fast.trychameleon.com, because the userID values ​​are open in the topcoder.

Best Regards.

## Impact

Leaked all topcoder users email
PIIs leak

## Attachments
- topco.png
- topco1.png
- topco2.png
