# Open SonarQube instance leaking internal source code

## Report Details
- **Report ID**: 947946
- **URL**: https://hackerone.com/reports/947946
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-30T16:07:19.572Z
- **Disclosed**: 2020-09-03T05:59:14.045Z

## Reporter
- **Username**: aksquare
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
# Summary
I came across an open SonarQube instance which can be found here: http://34.238.92.229:9000/
In this, there are 10 projects with a total of around 100k lines of code
To identify the owner, I went to the Issues tab and expanded the list of authors. There were 29 people there, and many of them were Equifax employees (I reached this conclusion because they have @equifax.com email id). 
Some of the projects there in the instance are related to authentication and APIs. One of the largest projects there is called zoomv2
Owing to the sensitive nature of the leakage, I did not dig deeper through the source code, however, I believe that this much information is enough for a POC. However, if you need more information, then I will be happy to dig through the source code there and give specific examples of how the information can be misused.

# Steps to recreate:
1. Go to http://34.238.92.229:9000/
2. There you can click on the issues tab, and then on the bottom left corner, click on Author
3. You will see a list of people who have contributed to the projects and can confirm that many of the people are Equifax employees
4. Go to Projects tab and see all the projects and their source code that are leaked 

# Fix
Put the instance behind a login screen, and check if unauthorised users have accessed this instance. If possible revoke access to any API keys or other credentials that were exposed in this instance

*I understand that there were other people from other companies in this instance too, and that this might not be an instance owned by Equifax. However, even though Equifax was not the owner, it still is involved with this particular instance, and thus I decided to report it to you.

## Impact

SonarQube is used to automate finding issues and vulnerabilities in source code. By leaving this instance open, an attacker can get access to all the source code, the issues, and the vulnerabilities that the particular code has. If this code is in a production environment, then this information is extremely dangerous. And even if the project is not in production, this kind of information can have internal APIs, IPs and other sensitive data that can be taken advantage of in other ways.

## Attachments
No attachments
