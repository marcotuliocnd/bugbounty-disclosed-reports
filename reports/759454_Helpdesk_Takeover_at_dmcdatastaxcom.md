# Helpdesk Takeover at dmc.datastax.com

## Report Details
- **Report ID**: 759454
- **URL**: https://hackerone.com/reports/759454
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-16T15:26:15.365Z
- **Disclosed**: 2020-01-15T17:49:43.120Z

## Reporter
- **Username**: matrixsoftsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: datastax

## Vulnerability Information
## Summary:
DNS record [dmc.datastax.com](dmc.datastax.com) is pointing to stale [dmc-support.zendesk.com](dmc-support.zendesk.com) domain on Zendesk which is available for takeover.

DNS Stale Records: {F661014}


## Proof of Concept:
There was no helpdesk configured at this address, which means that the address was available and anyone could claim it. I was able to claim dmc-support.zendesk.com.

On this page, https://dmc.datastax.com/hc/en-us I haven't made the page public, I'm attaching a screenshot of the webpage:
{F661004} 

## Supporting Material/References:
Login page:
{F661021}

## Impact

Subdomain takeover

## Attachments
- Screenshot_from_2019-12-16_20-20-40.png
- Screenshot_from_2019-12-16_20-31-10.png
- Screenshot_from_2019-12-16_20-39-40.png
