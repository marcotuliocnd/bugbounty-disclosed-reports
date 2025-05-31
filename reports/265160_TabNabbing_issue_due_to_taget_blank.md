# TabNabbing issue (due to taget=_blank)

## Report Details
- **Report ID**: 265160
- **URL**: https://hackerone.com/reports/265160
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-01T07:01:43.664Z
- **Disclosed**: 2018-04-25T05:50:20.331Z

## Reporter
- **Username**: ursa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Hi team,

i get to know in this particular url 
https://getmonero.org/get-started/what-is-monero/ and i found one 3rd party url.

Issue lies Here :

<a href="https://www.openhub.net/p/monero" target="_blank">

Here i can see you are using target=_blank and no more rel tag.
Here , target=_blank means it will open in another new tab. but due to tabnabbing it can change parent tab as well .
so as per security principal , don't trust much on 3rd party. and be at your safe sight,

i can recommend you to add rel="noreferer, ,noopener" to avoid this issue.

So final tag for that particular anchor tag will be:

<a href="https://www.openhub.net/p/monero" target="_blank rel="norefere,noopener" type="link">

Thanks,

## Attachments
No attachments
