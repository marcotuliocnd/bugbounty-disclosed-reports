# stored xss via Campaign Name.

## Report Details
- **Report ID**: 923679
- **URL**: https://hackerone.com/reports/923679
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-14T17:29:59.163Z
- **Disclosed**: 2020-07-21T14:46:35.025Z

## Reporter
- **Username**: omarelfarsaoui
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
## Summary:
Hi,
I found a stored  xss https://app.lemlist.com

## Steps To Reproduce:
1. go to https://app.lemlist.com/.
2. create or edit campaigns.
3. set the payload `/><svg src=x onload=confirm(document.domain);>` in the **Campaign Name**.
4. visit Buddies-to-Be tab .
5. click Add one on the right Top . or click on one of the list of  **Contact**
6. you will see pop-up.

## Poc
{F907302}

## Impact

Stealing cookies

## Attachments
- Poc.webm
