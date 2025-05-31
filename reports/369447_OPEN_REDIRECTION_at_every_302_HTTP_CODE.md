# OPEN REDIRECTION at every 302 HTTP CODE

## Report Details
- **Report ID**: 369447
- **URL**: https://hackerone.com/reports/369447
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-21T05:30:11.374Z
- **Disclosed**: 2018-08-07T22:45:56.022Z

## Reporter
- **Username**: ulalalaunana
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
#Summary
i guess every 302 HTTP CODE on 
>https://publishers.basicattentiontoken.org
possible to OpenRedirection

## Steps To Reproduce:

1. I edited the request when i got redirected from this request url

>https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca

587fb66a-9fdb-4419-9d05-f38ce41666ca = PUBLISHER_ID

>https://publishers.basicattentiontoken.org/publishers/587fb66a-9fdb-4419-9d05-f38ce41666ca

2. Add this header to the request and page willbe direct to injectedurl

>X-FORWARDED-HOST : injectedurl.com

Proof :
{F310965}

## Supporting Material/References:

  * BurpSuite
  * TextEditor

## Impact

A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.

## Attachments
- Screenshot_from_2018-06-21_12-27-19.png
