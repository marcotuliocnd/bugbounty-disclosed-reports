# TabNabbing issue (due to taget=_blank)

## Report Details
- **Report ID**: 260278
- **URL**: https://hackerone.com/reports/260278
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-15T11:02:27.983Z
- **Disclosed**: 2017-08-16T04:58:46.256Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi team,

i get to know in this particular url 
https://app.legalrobot-uat.com/dmca-safe-harbor  and i found one 3rd party url.

Issue lies Here :
```
<a href="https://eff.org" target="_blank">Electronic Frontier Foundation</a>
```
Here i can see you are using target=_blank and  no more rel tag.
Here , target=_blank means it will open in another new tab. but due to tabnabbing it can change parent tab as well (Legalrobot).
so as per security principal , don't trust much on 3rd party. and be at your safe sight,

i can recommend you to add rel="noreferer, ,noopener" to avoid this issue.

So final tag for that particular anchor tag will be:
``
<a href="https://eff.org" target="_blank" rel="norefere,noopener">Electronic Frontier Foundation</a>
```

more safe !!
Please let me know for more information.

Thanks,
Vishal

## Attachments
No attachments
