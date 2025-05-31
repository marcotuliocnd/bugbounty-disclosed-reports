# Subdomain takeover on http://fastly.sc-cdn.net/

## Report Details
- **Report ID**: 154425
- **URL**: https://hackerone.com/reports/154425
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T18:52:56.828Z
- **Disclosed**: 2016-08-22T19:46:06.530Z

## Reporter
- **Username**: ebrietas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hey team,

I've found a snapchat cdn domain here which had a test instance of fastly setup but did not remove the dns record when the service was cancelled. This allowed me to create a Fastly instance to take it over. I've confirmed this is a snapchat property via Censys (https://censys.io/certificates/65ba2e172a1eb85eb1071c9fd7a4e8371ef12625409890507c89a54978305558) though the risk here seems minimal at best as this domain does not appear to be used anywhere on any snapchat properties.

Repro steps:

* Visit http://fastly.sc-cdn.net/takeover.html

Recommended fix:
Removal of this record is recommended.


## Attachments
No attachments
