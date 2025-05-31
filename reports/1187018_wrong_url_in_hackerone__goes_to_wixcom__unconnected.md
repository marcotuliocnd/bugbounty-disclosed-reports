# wrong url in hackerone > goes to wix.com > unconnected

## Report Details
- **Report ID**: 1187018
- **URL**: https://hackerone.com/reports/1187018
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-06T19:48:31.761Z
- **Disclosed**: 2021-05-07T18:44:11.928Z

## Reporter
- **Username**: mhohlfeld
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
Hi there, this is a very small issue out of scope. 
Your current domain name in your hackerone program is wrong: http://sifchain.finance and moves to wix.com

## Steps To Reproduce:
  1. Login as a researcher
  2. Open the program from sifchain: https://hackerone.com/sifchain?type=team
  3. click on the public url: http://sifchain.finance
4. you will be redirected to wix.com and see message "not connected"

## Supporting Material/References:
  * screen movie: F1291486

## Impact

I think there is no impact.

**But maybe** (Maybe - because i don't know how wix.com works):
An attacker can create a new website and give his wix-project the name "sifchain.finance" *or* can connect an external domain "sifchain.finance".
The attacker can create a copy/paste fake website.
Than all researchers who click here on hackerone.com on the link will come to a fake website.
The attacker maybe can steal sifchain login data from the researchers.

## Attachments
- Bildschirmaufnahme_2021-05-06_um_21.39.06.mov
