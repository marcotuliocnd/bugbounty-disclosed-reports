# Login to any user account using other facebook app access token 

## Report Details
- **Report ID**: 101977
- **URL**: https://hackerone.com/reports/101977
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-25T09:31:18.682Z
- **Disclosed**: 2017-07-24T04:27:12.727Z

## Reporter
- **Username**: vinothkumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Vulnerable Url: https://api.imgur.com/generatetoken/thirdpartynativeandroid?type=facebook
Vulnerable Param: access_token

Attck:
Hacker can build own facebook app and get victim's facebook access token and use that access token to login into imgur account 

POC: https://drive.google.com/file/d/0B9bnr9ZtF2QsYktlRVFPUDB2SmM/view?usp=sharing

Prevention: Validate access token and check app id is equal to 127621437303857

## Attachments
No attachments
