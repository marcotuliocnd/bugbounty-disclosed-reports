# UXss on brave browser via scan QR Code

## Report Details
- **Report ID**: 1884042
- **URL**: https://hackerone.com/reports/1884042
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-02-22T21:53:13.229Z
- **Disclosed**: 2023-04-11T21:04:29.553Z

## Reporter
- **Username**: mrzheev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

I found UXss in your browser, and executed Xss on all open domains.
before that I want to tell you a little, that I've found a vulnerability like this in Microsoft Edge :
https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-23258

Oppo browser : (Private/no disclosure)

and now i found it in your application

## Products affected: 

 * Android 13, Brave browser version 1.48.164,  Brave Nightly browser version 1.50.53, Brave Beta Browser version 1.49.106, Chromium 110.5481.100


Payload : {F2191688}
This is a QR Code containing the url : javascript:alert(document.domain);

which the attacker will use to attack the victim


## Steps To Reproduce:
- Open Brave browser
- Open www.google.com

{F2191713}
- Click the url bar and delete the url (click the cross on the Url Bar)

{F2191709}
- You will see a Scan QR Code button

{F2191707}
- Click Scan QR Code button & Scan the QR Code above

{F2191708}

- Xss Executed.

{F2191706}  {F2191705}



## Supporting Material/References:

{F2191774}


https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-23258

## Impact

Attackers can steal the victim's cookies, and as you can see at this point. that this vulnerability does not only affect brave, but will affect all existing domains/websites. and it is very possible that websites such as facebook.com, google.com, microsoft.com are also affected by this vulnerability
example :
https://portswigger.net/daily-swig/microsoft-edge-translator-contained-uxss-flaw-exploitable-on-any-web-page

## Attachments
- QR_Code_AttackerH1.png
- WhatsApp_Image_2023-02-23_at_04.59.46.jpeg
- WhatsApp_Image_2023-02-23_at_04.59.53.jpeg
- WhatsApp_Image_2023-02-23_at_04.57.41.jpeg
- WhatsApp_Image_2023-02-23_at_04.58.28.jpeg
- WhatsApp_Image_2023-02-23_at_04.56.36.jpeg
- WhatsApp_Image_2023-02-23_at_05.07.39.jpeg
- WhatsApp_Video_2023-02-23_at_05.15.38.mp4
- WhatsApp_Video_2023-02-23_at_05.15.38.mp4
