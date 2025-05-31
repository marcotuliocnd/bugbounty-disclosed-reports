# Stored xss

## Report Details
- **Report ID**: 156373
- **URL**: https://hackerone.com/reports/156373
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-03T20:56:27.457Z
- **Disclosed**: 2016-09-07T12:14:22.510Z

## Reporter
- **Username**: rishi62
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Hi,i have found an stored xss which is reflected at https://www.algolia.com/explorer#?index=getstarted_actors&tab=explorer

Steps to produce:
1) Go to https://www.algolia.com/explorer#?index=getstarted_actors&tab=explorer and add "><img src=x onerror=alert(document.cookie);> as an attribute and keep it at top as in screenshot1

2) Go to  https://www.algolia.com/explorer#?index=getstarted_actors&tab=ranking and take the cursor on the ranking info(the trophy icon),and you will see a pop up alert of xss. (Screenshot2)
 I have tested it on Chrome and firefox its works on both.


P.S: I dont know why but my ip got banned when i was uploading the script to test could you unban me?


## Attachments
- screenshot_1.png
- Screenshot_2.PNG
