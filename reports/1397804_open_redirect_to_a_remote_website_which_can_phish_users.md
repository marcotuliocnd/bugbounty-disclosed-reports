# open redirect to a remote website which can phish users

## Report Details
- **Report ID**: 1397804
- **URL**: https://hackerone.com/reports/1397804
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-10T19:58:19.110Z
- **Disclosed**: 2022-11-25T18:08:35.649Z

## Reporter
- **Username**: adrian_t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
By Adding some extra headers in the request I noticed that  the user is redirected to a remote website. This can lead to stealing a user credentials (phishing) on a remote server.

These headers can be added either using a MITM attack or by chaining with another vulnerability such as request smuggling, header injection more commonly abusing a reverse proxy that sits in front of the website.

ps:crayons

## Impact

This can lead to stealing a user credentials (phishing) on a remote server or planting malware on the user's computer.

## Attachments
- Open_redirect.png
