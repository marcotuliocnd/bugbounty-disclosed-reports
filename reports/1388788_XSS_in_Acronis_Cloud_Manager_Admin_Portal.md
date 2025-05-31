# XSS in Acronis Cloud Manager Admin Portal

## Report Details
- **Report ID**: 1388788
- **URL**: https://hackerone.com/reports/1388788
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-02T07:02:11.083Z
- **Disclosed**: 2022-12-02T19:48:03.112Z

## Reporter
- **Username**: mooimacow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello,

Hope you are doing well. I wanted to report the following security vulnerability:

The Acronis Cloud Manager Admin Portal default swagger UI is vulnerable to cross site scripting. I have the API running locally on my machine. I have attached screenshots of the XSS

The URL is:
https://localhost:16080/swagger/index.html?url=███/xss/index.html

Documentation on how to access the API is available here:
https://kb.acronis.com/content/64702

If you would like to reproduce this, you need to setup the Cloud Manager admin portal. To do so, you can take the following steps:
1) Download the cloud manager here (free trial): https://www.acronis.com/en-us/products/cloud-manager/
Once you do that, you will need to install the Acronis Cloud Manager console and the Acronis Cloud Manager web portal. The guide is available here:

https://dl.acronis.com/u/rc/GSG_AcronisCloudManager_5.0_EN-US.pdf?fbclid=IwAR0yOcDjRDPgkXlwNX5Qj0-B4wjOK2d9s76IipnmE_jZiRY_2CSZy3AuJMk

I recommend unzipping the download file in the email and installing this directly on a Windows system rather than using the ISO. I think that will be easier.

In order to get those setup, you need a valid database to connect to. You can use the following links to get one setup.
2) Download sql server express  (https://go.microsoft.com/fwlink/?linkid=866658)
3) Download sql server management studio (https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)

Once you have it sql server setup, you need to create a user that you can use to connect to the database from the Acronis setup guide, to get everything working. Once it is setup, the default swagger url available to all installations, is vulnerable to XSS.

## Impact

The swagger site allows you to enter in different credentials to test API methods via the Authorize Button on the right side. The methods in scope are very sensitive based on the nature of this application and generally only admins would be testing the API methods with their credentials.

With XSS here we would have the opportunity to target admin users and access very sensitive data. More information on XSS is available here: https://www.packetlabs.net/cross-site-scripting-xss/

If someone were to deploy this API to the cloud or another location, it would be an easy target. Right now I just have it running locally.

The swagger instance running is using an older version of dom-purfiy. If you upgrade the instance, that should fix this issue.

Let me know if you have questions. Thanks!
Ben

## Attachments
- what_you_need_to_install.PNG
