# URL filter bypass in Enterprise Grid

## Report Details
- **Report ID**: 500348
- **URL**: https://hackerone.com/reports/500348
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-24T01:56:33.033Z
- **Disclosed**: 2020-02-14T00:18:18.397Z

## Reporter
- **Username**: akaki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
# URL filter bypass in Enterprise Grid

## Description

Slack Enterprise Grid seems to be able to add arbitrary column to the profile of the account. In my company there is a おすすめランチ (My Favorite Lunch) column, and we can set the URL of the website and Display text.

{F429131}
{F429132}

Only the `http:` or `https:` scheme can be set in the URL, and other schemes can not be set by input validation.

{F429133}

However, since input validation exists on the client side, we can bypass this validation by changing the profile setting request.

```diff
 POST /api/users.profile.set HTTP/1.1
 Host: example-corp.slack.com
 ...

 -----------------------------7110134921404748136166706634
 Content-Disposition: form-data; name="profile"

-{"real_name":"Akaki Tsunoda","title":"","phone":"03-9999-0000","fields":{"XfABVBP467":{"value":"https://www.mcdonalds.com","alt":"McDonald's"}}}
+{"real_name":"Akaki Tsunoda","title":"","phone":"03-9999-0000","fields":{"XfABVBP467":{"value":"tel://03-9999-0000","alt":"McDonald's"}}}
 -----------------------------7110134921404748136166706634
 ...
```

{F429134}

I took screenshots on browser, so an illegal URL is displayed, but it is not displayed in mobile apps.

## Impact

In the case of using the `tel:` scheme, the victim who clicked on the link included in the attacker's profile inadvertently call the attacker. In the future attackers may exploit Slack or other app's deep linking (Custom URL Scheme).

**Note:** I could not execute JavaScript because I could not use `javascript:` or `data:` scheme by server side input validation.

## Attachments
- Screen_Shot_2019-02-24_6.25.02.png
- Screen_Shot_2019-02-24_6.43.48.png
- Screen_Shot_2019-02-24_6.22.59.png
- Screen_Shot_2019-02-24_7.18.52.png
