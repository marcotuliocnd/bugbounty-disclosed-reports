# Able to see Twitter Circle tweets due to improper access control on the "FavoriteTweet" endpoint

## Report Details
- **Report ID**: 1694304
- **URL**: https://hackerone.com/reports/1694304
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-08T05:23:11.525Z
- **Disclosed**: 2024-03-01T22:41:27.301Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** 
Hi,

Twitter Circle is a new feature that allows posting tweets to a specific group selected by the user. However, I noticed any user can like the Twitter Circle tweets by modifying the "like" request.

That's our request to like a tweet :

████

If you change the tweet ID to a Twitter Circle tweet, you're able to like it. That's a bug, but it doesn't have a considerable impact because we cannot see the tweet.
I went to my profile's "Likes" tab but I also couldn't see the tweet on that page. I checked other endpoints but couldn't find anything.
Then I remembered something, on all social media platforms, we can request our data from the company. That data includes everything about our account, so I checked if Twitter has this feature, and, yes!
Twitter allows us to download our data, so I requested my data on https://twitter.com/settings/download_your_data, and waited 24 hours, then I downloaded my data archive.
In my data archive, I could see the liked Tweets, and it also contains the Twitter Circle tweet that I liked!

███

## Steps To Reproduce:

  1.Turn on your proxy program and like any tweet on Twitter
  1. You will send a POST request to the `FavoriteTweet` endpoint
  1. Change the `tweet_id` to a Twitter Circle tweet ID, it should give `200 OK` on the response.
  1. Now go to https://twitter.com/settings/download_your_data and request your data.
  1. Twitter will send an email when the data is ready, so you just need to wait until the data
  1. In the data archive, open the HTML file or check the `data/like.js` file. You will see the content of the Twitter Circle tweet that you liked.

## Impact

Twitter Circle is a feature that limits tweets to a specific group selected by the user. And the user can post sensitive things to his/her Twitter Circle group.
Any attacker can see these tweets by abusing this vulnerability. That leads to information disclosure as these tweets can contain private things.

## Attachments
No attachments
