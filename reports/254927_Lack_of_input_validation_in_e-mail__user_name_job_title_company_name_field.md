# Lack of input validation in e-mail & user name, job title, company name field

## Report Details
- **Report ID**: 254927
- **URL**: https://hackerone.com/reports/254927
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-30T09:59:47.545Z
- **Disclosed**: 2017-07-31T02:48:01.721Z

## Reporter
- **Username**: smziaurrashid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi,
During sign up input validation didn't deploy properly on e-mail & name field. I've tested inputing following e-mail during sign up:
``hacker~%@gmail.com``
Your system send email to verification the account though the e-mail address is invalid as gmail doesn't allow user to sign up using special characters like ``%,~``  etc.
{F208264}
Another issue is during sign up name field & from account profile edit option name feild, job title, company name field also failed to validate user input and accept special characters like ``$, %, ~,!,{}  ``.  I've tested this using my account ``kazishaheb.me@gmail.com``
{F208268}
{F208270}

Hope you'll deploy a quick fix. I look forward to hear backck from you, thank you!

## Attachments
- Screenshot_2017-07-30-15-37-56.jpg
- Screenshot_2017-07-30-15-55-00.jpg
- Screenshot_2017-07-30-15-55-08.jpg
