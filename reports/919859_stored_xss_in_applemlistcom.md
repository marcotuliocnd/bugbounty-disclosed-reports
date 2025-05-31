# stored xss in app.lemlist.com

## Report Details
- **Report ID**: 919859
- **URL**: https://hackerone.com/reports/919859
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-09T17:29:33.440Z
- **Disclosed**: 2020-07-21T14:08:47.344Z

## Reporter
- **Username**: omarelfarsaoui
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
Hi there,
I found a stored xss [app.lemlist.com](https://app.lemlist.com/).

## Steps To Reproduce:

  1. go to https://app.lemlist.com/.
  1. create or edit **campaigns**.
  1. visit tab **Buddies-to-Be**.
  1. click **Add one** on the right Top.
  1. Fill in the input 
  1. add `/><svg src=x onload=confirm(document.domain);>` ** Icebreaker** and **companyName**
  1. click create .
              
## POC
{F901411}

## Impact

Stealing cookies

## Attachments
- Screencast_09-07-20_18_03_40.webm
