# Open redirection bypass in /www/admin/campaign-modify.php

## Report Details
- **Report ID**: 794144
- **URL**: https://hackerone.com/reports/794144
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-12T06:20:31.895Z
- **Disclosed**: 2020-03-12T12:54:37.811Z

## Reporter
- **Username**: hoangn14
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
### Description
- There is an open redirect on /www/admin/campaign-modify.php?return_url= {F713773}
- By using //// at the start of the link, you can bypass the open redirect filter.

- example: `/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Fhackerone.com`

## Impact

This vulnerability can be used for phishing attacks

## Attachments
- open_re.png
