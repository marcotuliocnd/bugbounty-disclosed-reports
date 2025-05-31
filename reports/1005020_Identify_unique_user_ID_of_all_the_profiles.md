# Identify unique user ID of all the profiles 

## Report Details
- **Report ID**: 1005020
- **URL**: https://hackerone.com/reports/1005020
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-11T09:42:06.286Z
- **Disclosed**: 2020-12-25T10:53:51.918Z

## Reporter
- **Username**: covertlyovert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Through this vulnerability, one can know the unencrypted user ID of all the profiles 


Steps to reproduce:
1. Login to your Bumble profile
2. In the SERVER_GET_USER_LIST API replace the folder ID 0 with 7. This folder contains all the profiles in your deck /which you have right-swiped on (screenshot 1); Through this, we may choose to again swipe left on them if desired.
3. Intercept the response. The unique user ID of the profile is shown in plain text. 
4. Adding additional parameters to the projection field also gives us information like the user vote, etc. 
5. We can even increase the 'count' to get details of more profiles

## Impact

In case of a match, this information can be used by a male's profile to craft a message and initiate the chat, as the 'is_match' field is true and the 'user_id' field is now available. (Screenshot 2)

## Attachments
No attachments
