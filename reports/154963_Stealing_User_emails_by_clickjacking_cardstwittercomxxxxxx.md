# Stealing User emails by clickjacking cards.twitter.com/xxx/xxx

## Report Details
- **Report ID**: 154963
- **URL**: https://hackerone.com/reports/154963
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-07-29T15:50:43.743Z
- **Disclosed**: 2017-02-03T16:14:43.940Z

## Reporter
- **Username**: akhil-reni
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Hello**

In twitter you can create cards to generate leads.
For example:
https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357

If you visit the above URL and click the button your email and username is sent to my domain.

Since this page is missing X-FRAME-HEADERS,
a user could simply iframe the URL and could steal victim's emails.

**Proof of concept code**
```
<html>
<iframe src=https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357>
</html>
```

**Regards,
Akhil**

## Attachments
No attachments
