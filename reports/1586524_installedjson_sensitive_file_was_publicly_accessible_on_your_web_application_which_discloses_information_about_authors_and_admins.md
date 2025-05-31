# installed.json sensitive file was publicly accessible on your web application which discloses information about authors and admins 

## Report Details
- **Report ID**: 1586524
- **URL**: https://hackerone.com/reports/1586524
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-30T16:12:35.644Z
- **Disclosed**: 2022-10-22T18:39:33.897Z

## Reporter
- **Username**: whitehacker18
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
##kindly if you don't accept this issue please close it as informative , thanks in advance 

##Description:
The installed.json file is a sensitive file and it was publicly accessible on your webserver , which discloses some information about your web site and users such as authors like admin as shown below:
`"authors": [
            {
                "name": "Modern Tribe",
                "email": "admin@tri.be"
            }
`

##Steps to Produce:
1. Go to https://blog.yelp.com/vendor/composer/installed.json

##References :
https://www.acunetix.com/vulnerabilities/web/composer-installed-json-publicly-accessible/
https://hackerone.com/reports/461598

##Remediation:
Restrict Access to vendors directory

## Impact

Disclosure of information about components used by the web application.

## Attachments
- POC.PNG
