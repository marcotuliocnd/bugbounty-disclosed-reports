# Bypassing Content-Security-Policy leads to open-redirect and iframe xss

## Report Details
- **Report ID**: 1166766
- **URL**: https://hackerone.com/reports/1166766
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-16T18:46:12.058Z
- **Disclosed**: 2021-07-30T05:33:21.117Z

## Reporter
- **Username**: echidonut
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
`https://my.stripo.email/cabinet/#/template-editor/.....` has the ff: code to make iframes more secure:
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self';
    frame-src data: *.firebaseapp.com *.stripe.com *.google.com *.facebook.com 'self';
    style-src 'self' 'unsafe-inline' *;
    script-src 'self' 'unsafe-eval' 'unsafe-inline' *.ampproject.org googletagmanager.com *.googletagmanager.com *.amplitude.com api.vk.com *.gstatic.com *.facebook.net *.google.com *.google-analytics.com *.stripe.com *.pingdom.net *.intercom.io *.intercomcdn.com *.stripo.email *.zscalertwo.net *.zscaler.com *.zscaler.net *.pinimg.com *.getsitecontrol.com;
    img-src 'self' data: *;
    connect-src 'self' *;
    child-src blob:;
    font-src 'self' *;
    object-src 'self' *">
```

* <iframe> pointing to other domains won't work but, the whitelist in frame-src data has listed *.firebaseapp.com, a free hosting domain, leading to iframe abuse and redirects

## Steps To Reproduce:

1. Create a new message/template with HTML
2. Using nodeJS, deploy a page in firebaseapp. It's free. [Guide](https://firebase.google.com/docs/hosting/quickstart)
2. Mine is [hackerone-jm.firebaseapp.com](https://hackerone-jm.firebaseapp.com). Add the ff. line: `<iframe src="//hackerone-jm.firebaseapp.com"></iframe>` in the HTML editor
3. A browser popup will show, then redirect after

## Supporting Material/References:
{F1268265}
*Tested in Google Chrome Version 89.0.4389.128 (Official Build) (64-bit)*

## Impact

* This can be used to launch a phishing attack against users of the same organization.
*  `viewstripo.email` is also vulnerable to this making it an open redirect/xss to all users. [POC](https://viewstripo.email/6a8ceb1a-7e45-4304-a93f-0cf4c32fc3111618586929192)
* This also makes editing the message/template almost impossible without disabling javascript in your browser

*this only works assuming the user has allowed `my.stripo.email` to redirect and spawn popups.*

## Attachments
- recording-1618597510622.webm
