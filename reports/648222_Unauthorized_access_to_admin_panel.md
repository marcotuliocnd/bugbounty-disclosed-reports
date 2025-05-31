# [██████████] Unauthorized access to admin panel

## Report Details
- **Report ID**: 648222
- **URL**: https://hackerone.com/reports/648222
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-17T18:15:38.779Z
- **Disclosed**: 2020-05-14T16:52:06.670Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
In previous reports, I described vulnerabilities in a panel to which I had access. 

 #512269
 #512693
 #512695

I could log in to this site and then perform some attacks, such as SQL injection\XSS or other bugs. But before the above vulnerabilities were considered by you, the possibility to bypass authorization on the site was disabled. And after that, the vulnerabilities could not be reproduced and I was forced to close my reports.

Recently, I began to explore this site again. And I found that the developers have poorly implemented the restriction of authorization on the site. 

I can still get the contents of an authorized site. How? When I visit some pages of the site, I get a redirect to the authorization form. But in addition to the redirect, the response body also contains HTML code of auth site.

Look this pages:
> https://███████/mission.php
> https://██████████/personnel.php
> https://███████/index.php

### Steps to reproduce
1) Turn on Live Interception in burp (Proxy-Intercept)
2) Intercept request. Press right mouse button-> Do intercept -> Response this request
█████████
3) Delete this redirection
████

Here I can see a lot of private information

> https://█████████/personnel.php

█████

> https://███/index.php

███████

## Impact

Incorrect access restriction to the authorized interface of the site leads to information leakage.

## Attachments
No attachments
