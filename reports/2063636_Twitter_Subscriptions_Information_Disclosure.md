# Twitter Subscriptions Information Disclosure

## Report Details
- **Report ID**: 2063636
- **URL**: https://hackerone.com/reports/2063636
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-11T15:56:49.224Z
- **Disclosed**: 2023-09-18T19:33:19.959Z

## Reporter
- **Username**: mirhat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 

Hi team,
I was scrolling on Twitter connected from US location, and a Tweet appeared on my timeline; I couldn't see the tweet because it is only visible to subscribers. However I was able to extract the images from that tweet even though I'm not a subscriber

**Description:**

A subscriber only tweet of MrBeast appeared on my timeline (which i can't see)
{F2487967}

Clicking on the quotes button revealed the images and the tweet content which should be invisible to me.

**Steps To Reproduce:**

  1.  Go to https://twitter.com/MrBeast/status/1678121172196630531
  1. Ensure that you are not a subscriber therefore cannot see the tweet
  1. Click on quotes button and see the tweet and images

## Supporting Material/References:

POC video:
████

## Impact

Information disclosure

## Attachments
- substi.jpg
