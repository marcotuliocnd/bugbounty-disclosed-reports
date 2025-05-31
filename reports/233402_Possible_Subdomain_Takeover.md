# Possible Subdomain Takeover

## Report Details
- **Report ID**: 233402
- **URL**: https://hackerone.com/reports/233402
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-30T21:50:10.773Z
- **Disclosed**: 2017-05-31T03:24:37.053Z

## Reporter
- **Username**: z3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
None of the weakness categories really fit this so I apologize for that.

The subdomain `sales.mixmax.com` points to `151.101.16.229`, a `webflow.io` proxy server. Because it 404s, this leads me to believe that a subdomain takeover is possible through the webflow service as whatever this is pointing to is unused. 

Due to odd DNS configurations I'm not 100% sure on this but thought I'd make you aware just in case.

## Attachments
No attachments
