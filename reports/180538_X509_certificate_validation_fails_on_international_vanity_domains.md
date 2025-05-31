# X.509 certificate validation fails on international vanity domains

## Report Details
- **Report ID**: 180538
- **URL**: https://hackerone.com/reports/180538
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-11-06T20:31:40.455Z
- **Disclosed**: 2017-02-06T22:49:20.097Z

## Reporter
- **Username**: tk0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
This is not an vulnerability, more likely TLS/SSL related configuration issue with certificates noticed during bug bounty testing.

If you try to access any Finnish domain (such as my HackerOne test-profile http://tomitest.yelp.fi/), there will be an certificate related error presented to user. You can try with any other Finn URL's and you'll notice this affects all other too.

Most probably users are not able to access Finnish Yelp domain pages without some extra hassle/confusion. Basically *.com* works fine, but *.fi* doesn't. Anyways, since Yelp provides *.fi* domain if you're are an Finn (like me), I assume both should work for user profiles.

I've added two screenshots to aid this finding:
1. Certificate error presented by Google Chrome.
2. Link from my testpage (Yelp's localized profile page address via get your own url)

Cheers,
-Tomi


## Attachments
- chrome_whine.png
- link.png
