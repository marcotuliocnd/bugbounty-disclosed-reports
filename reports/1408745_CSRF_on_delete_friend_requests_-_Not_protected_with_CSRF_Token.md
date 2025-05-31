# CSRF on delete friend requests - Not protected with CSRF Token

## Report Details
- **Report ID**: 1408745
- **URL**: https://hackerone.com/reports/1408745
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-11-24T03:04:41.439Z
- **Disclosed**: 2021-11-26T22:19:11.747Z

## Reporter
- **Username**: sbakhour
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
## Summary:
Hello XVideos Security Team,

The is a possibility of CSRF on the POST method when deleting friend requests that are sent by the users. Any user can send the malicious contents to perform the post method in order to delete a friend request for a specific member.

## Steps To Reproduce:

  1. Login with your XVideos account and add the X user as a friend
  2. Go to your friends request sent and validate that the request is there on https://www.xvideos.com/account/friends/requests/sent 
  3. Select the user X that you want to delete then click on the button next to Cancel: "Checked" or "All"
  4. Intercept the request when the pop up message appear & after you click OK.
  5. Notice that this POST request to cancel the friend request is not protected by a CSRF token
  6. Using Burp Professional , right click on this request and under engagement tools select "Generate CSRF POC"
  7. Copy the HTML contents into a new HTML page as a proof of concept.
  8. Send this CSRF HTML page to the victim to delete the friend request of this specific X user
  9. Notice that the request deletes the Friend request.

## Supporting Material/References:
Refer to the attached video for more details

##Mitigation:
Add a CSRF token for the POST method to cancel or delete friend requests so it can be done only by the logged in user to confirm the activity.

## Impact

Attackers can send Victims this malicious content to victims to delete sent friend requests of specific users before they get accepted.

## Attachments
- Friend_Request_delete_XVideos.mp4
