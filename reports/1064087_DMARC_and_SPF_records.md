# DMARC and SPF records

## Report Details
- **Report ID**: 1064087
- **URL**: https://hackerone.com/reports/1064087
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-22T03:35:52.983Z
- **Disclosed**: 2020-12-22T07:07:44.999Z

## Reporter
- **Username**: hackz-bhavin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: who-covid-19-mobile-app

## Vulnerability Information
If you are encountering this error of No DMARC Record found, this means that your domain does not have a published DMARC record. DMARC Records are published via DNS as a text(TXT) record. They will let receiving servers know what they should do with non-aligned email received from your domain.


Vulnerable url: whocoronavirus.org


HOW TO REPRODUCE(POC-ATTACHED IMAGE):-

1.GO TO- https://mxtoolbox.com

2.ENTER THE WEBSITE CLICK GO.

3.YOU WILL SEE THE FAULT(No DMARC Record found)

4.In the new page that loads change MXLookup to DMARC Lookup

## Impact

Spammers can forge the "From" address on email messages to make messages appear to come from someone in your domain. If spammers use your domain to send spam or junk email, your domain quality is negatively affected. People who get the forged emails can mark them as spam or junk, which can impact authentic messages sent from your domain

## Attachments
- Screenshot_2020-12-22_at_09.02.41.png
