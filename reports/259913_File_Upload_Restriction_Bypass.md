# File Upload Restriction Bypass

## Report Details
- **Report ID**: 259913
- **URL**: https://hackerone.com/reports/259913
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-14T18:12:51.725Z
- **Disclosed**: 2020-05-14T16:49:59.519Z

## Reporter
- **Username**: ok_bye_now
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A file upload function allows users to specify their own file name on the server, which allows a user to upload as many images as they would like, potentially causing an Application Denial of Service.

**Description:**
The listserv 16.0 server at http://████████ allows users to upload their own logos for their own newsletter. The user can upload up to 10 logos. If you capture the request in a proxy such as Burp Suite Pro, you can examine the POST request and see that imgnum parameter is set at 1-10 based on what logo the user specified. It is possible to modify that parameter to whatever you want. For example; any word or number and that image can be retrieved by browsing to the link provided after it is uploaded. This would allow a user to upload as many images/logos as they want to potentially causing a Application Denial of Service if they were able to fill up the server hard drive. 

## Impact
Denial of Service

## Step-by-step Reproduction Instructions

1. Navigate to http://█████████ and create an account.
2.  Go to Preferences after you login and choose the "Newsletter Profile" tab.
3. On the logos option, keep the default "Slot 1" selected and hit browse to choose an image to upload. 
4.  No go to the bottom and choose Update.
5. In your proxy tool, replay the request with the imgnum paramter changed to "cow" or 50 or whatever you want. 
6. Append the same value to the end of the image data (logo parameter) in the POST request. 
7. Replay the modified request.
8. Navigate to http://█████/scripts/wa.cgi?VL&Y=9e44b517&imgnum=<INSERT MODIFIED VALUE HERE> 
9. For example, if you used "cow", you would navigate to http://█████████/scripts/wa.cgi?VL&Y=9e44b517&imgnum=cow
10. To verify, download the image and look at the image in a text editor, you should see the appended value at the end of the image file.

You many need to change the Y parameter in the URI for your account, this will be displayed after you upload your logo through the web interface.

## Product, Version, and Configuration (If applicable)
LISTSERV 16.0
## Suggested Mitigation/Remediation Actions
Only allow values 1-10 for the imgnum parameter and overwrite images if there is one with that number already.

## Attachments
No attachments
