# Hard-coded API keys at NordVpn Android App

## Report Details
- **Report ID**: 792850
- **URL**: https://hackerone.com/reports/792850
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-02-11T00:42:03.520Z
- **Disclosed**: 2020-03-27T10:50:58.537Z

## Reporter
- **Username**: dantt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Hello NordVpn,

**APK Version : 4.6.2**
**API'S at res/values/strings.xml**

>**Google**
>google_api_key = ███
**Stripe**
>stripe_publishable_api_key = ██████████

**Referance;** 
>https://stripe.com/docs/keys

## Impact

Cleartext Storage of Sensitive Information

## Attachments
No attachments
