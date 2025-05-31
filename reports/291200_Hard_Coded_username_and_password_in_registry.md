# Hard Coded username and password in registry

## Report Details
- **Report ID**: 291200
- **URL**: https://hackerone.com/reports/291200
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-11-17T14:33:24.774Z
- **Disclosed**: 2018-05-06T19:51:42.600Z

## Reporter
- **Username**: bluedangerforyou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kaspersky

## Vulnerability Information
I was using a tool called RegShot to take a snap shot of the registry before and after installation in order to see what changes were being made in the registry and I discovered hard-coded credentials

I have attached the full comparison details of the registry changes

but these are the lines and reg entries where the credentials are stored:

 HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\User: "kavdumps"
HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\Password: "UxzAbKFLufVBSg8Y"
HKLM\SOFTWARE\Wow6432Node\KasperskyLab\AVP17.0.0\environment\dump\FTP: "kavdumps.kaspersky.com"

I was able to open browser and navigate to ftp://kavdumps.kaspersky.com which gave me a login prompt.
I used the username: kavdumps 
and password of: UxzAbKFLufVBSg8Y

I was able to login. The directory was empty however

I have attached a video and the log file

I have seperated the lines so it is easier to find in the file.


## Attachments
- KIS.mp4
