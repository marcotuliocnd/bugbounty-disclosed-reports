# DOM based XSS in store.acronis.com/<id>/purl-corporate-standard-IT [cfg parameter]

## Report Details
- **Report ID**: 968690
- **URL**: https://hackerone.com/reports/968690
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-27T13:56:02.232Z
- **Disclosed**: 2020-10-20T14:37:52.054Z

## Reporter
- **Username**: f_m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Hi Acronis team, i found a DOM based XSS in store.acronis.com, this vulnerability arise from a missing escape for the \ character.

## Steps To Reproduce

  1. go to: https://store.acronis.com/837/purl-corporate-standard-IT?cart=201591&deliveryEmail=f_m%2B5%40wearehackerone.com&deliveryFirstname=fmfm&deliveryEmailRetype=f_m%2B5%40wearehackerone.com&deliveryPhone1=fmfm&deliveryLastname=fmfmfm&x-uid=%22%3e%3ctestxss&quantity_201591=1&recommendation=cloud_20off&recommendation=ACPPLP&x-page=https://www.acronis.com/it-it/business/backup/server/purchasing/&tracking=&x-segment=corporate&cfg=\\ciao%27}];prompt();var%20asd=[{%27foo%27:%27bar
  2. a prompt appear

{F965980}

## Impact
since it's in the store subdomain, this can lead to PII stealing

## Recommendations
escape the \ character in \\

## Impact

since it's in the store subdomain, this can lead to PII stealing

## Attachments
- reflected_xss.JPG
