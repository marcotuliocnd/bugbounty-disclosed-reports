# Zomato.com Reflected Cross Site Scripting

## Report Details
- **Report ID**: 303522
- **URL**: https://hackerone.com/reports/303522
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-09T13:17:16.049Z
- **Disclosed**: 2018-04-08T12:01:08.363Z

## Reporter
- **Username**: akamble937
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
zomato.com/php/liveSuggest.php takes various field input to show customized out put for the users.
The data entered to entity_id field is not santized or html encoded which allows user to add payloads via this parameter which will be reflected to user.

Steps to reproduce :

Please click on below link to check the poc . Also please find attached poc for reference

https://www.zomato.com/php/liveSuggest.php?type=keyword&search_bar=1&q=ad&online_ordering=&search_city_id=5&entity_id=confirm(1)%20%3C%20%22%22%27%22ss%22%20onerror%3E;confirm(1)%3Cvideo%20src=x%3E%3Cvideo%20src=%22&entity_type=%22;%20onerror

## Impact

An attacker can craft a malicious link and send to users , which can then lead to session hijacking , redirecting to malicious or fake websites etc.

## Attachments
- zomato_xss.mp4
