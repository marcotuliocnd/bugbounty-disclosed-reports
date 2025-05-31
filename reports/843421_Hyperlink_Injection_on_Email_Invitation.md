# Hyperlink Injection on Email Invitation

## Report Details
- **Report ID**: 843421
- **URL**: https://hackerone.com/reports/843421
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-08T17:57:42.830Z
- **Disclosed**: 2020-11-24T15:08:32.808Z

## Reporter
- **Username**: eissen5c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
#DESCRIPTION
Found an hyperlink injection of the name of Organization when the attacker invites the victim to his organization with injection hyperlink.

#STEPS
1. Add organization with the name of https://attacker.com and switch it.
2. Go to user and invite the victim using email.
3. victim will seee the invitation with malicious link

#POC IMAGE

* Add organization name as https://attacker.com

{F779678}

* Go to user and invite someone and the victim will see the invitation

{F779676}

* accepted invitation for already registered

{F779677}

## Impact

Open Redirect from hyperlink injection to malicious website.

## Attachments
- 2.JPG
- 3.JPG
- 1.JPG
