# Creating malformed URLs via new line character in-between two URLs leads to misrepresented hyperlinks in Tweets/DMs

## Report Details
- **Report ID**: 712979
- **URL**: https://hackerone.com/reports/712979
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-12T22:37:45.876Z
- **Disclosed**: 2020-01-24T22:02:45.331Z

## Reporter
- **Username**: zlz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
## Summary
When composing a tweet or a direct message it is possible to use a new line character (`%0d`) to seperate two URLs within the actual hyperlinking process, but not the URL displaying process. The new line character acts as an invisible character that disrupts the actual hyperlinking process, whereas when previewed does not show up. This allows an attacker to create realistic looking phishing URLs via combining `attacker.com` + `%0d` + `website.com`. If an attacker controlled both `itter.com` and `fakewebsite.tw` in the below request, they could trick victim's into browsing to, what they think would be, `fakewebsite.twitter.com`.

```
fakewebsite.tw + %0d + itter.com
```

These two URLs, when put together and displayed, would look like the following on a tweet or a direct message:

{F606210}

But, after being actually clicked, would take you to the following URLs:

{F606211}
* [https://fakewebsite.tw](https://fakewebsite.tw)

{F606212}
* [https://itter.com](https://itter.com)

This is also possible to do in direct messages, as so...

{F606213}

## Description
I don't think this falls under any real classification of issues other than "CRLF injection", but even then, it's definitely not the right category. This is simply abusing Twitter's URL composing process to create fake hyperlinks. Overall I think this is a neat issue that I think would definitely be exploited by bad actors.

## Steps To Reproduce:

1.) Open either (1) direct messages, or (2) composing a tweet
2.) Type out `fakewebsite.twitter.com`, click enter, and intercept the request with Burp Suite
3.) Modify the `status` or `text` parameter (depending on if you're tweeting or DMing) to be `fakewebsite.tw%0ditter.com` like so...

```
POST /1.1/dm/new.json HTTP/1.1
Host: api.twitter.com

text=fakewebsite.tw%0ditter.com&cards_platform=Web-12&include_cards=1&include_composer_source=true&include_ext_alt_text=true&include_reply_count=1&tweet_mode=extended&dm_users=false&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&conversation_id=██████&recipient_ids=false&request_id=&ext=mediaColor,altText,mediaStats,highlightedLabel,cameraMoment
```

4.) Observe the URL is displayed as `fakewebsite.twitter.com` but is actually a hyperlink to both `fakewebsite.tw` and `itter.com`.

## Impact

This could be exploited as a targeted attack or mass phishing attack towards Twitter (the ongoing cryptocurrency scams) by abusing the integrity of Twitter's URL rendering service to create legitimate looking URLs. Although Twitter cannot control the content that is displayed on the other URL, it is possible to control the way URLs are displayed before presenting them to the user.

## Attachments
- google_twitter_com.PNG
- fakewebsite_google.PNG
- fakewebsite_1.PNG
- fakewebsite_2.PNG
- fakewebsite_tw.PNG
