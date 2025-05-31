# Manipulating response leads to free access to Streamlabs Prime 

## Report Details
- **Report ID**: 1070510
- **URL**: https://hackerone.com/reports/1070510
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-03T10:04:21.920Z
- **Disclosed**: 2021-01-21T03:53:02.356Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Heyy team,
I have a found cool bug which allows me to get access to  streamlabs  prime features for free.

Here is the api endpoint which checks whether the user has a prime subscription or not:

https://streamlabs.com/api/v5/user/prime/subscription

```json
{
  "is_active": false,
  "is_pending": false,
  "is_past_due": false,
  "is_canceled": false,
  "is_pro": false,
  "type": "",
  "free_trial_claimed": false,
  "hibernate_claimed": false,
  "free_trial_eligible": false,
  "hibernate_eligible": false,
  "cooldown_eligible": false,
  "cooldown_seconds_past": null
}
```
Everything was set to false, so I decided to use the Burp's *Match and Replace* rule to replace every ocurrence of *false* in the Response body to *true*.
And as expected I got access to some of the prime features, the most interesting one was the streamlabs All Stars rewards, which is available at this url, https://streamlabs.com/dashboard#/streamlabs-rewards?skipPrimeOnboarding=1

When a user which doesn't have the Streamlabs Prime tries to access the streamlabs-reward endpoint the *reedeemed* option won't be there:

{F1142675}

Now after setting the match and replace in burp now if we try to visit the  streamlabs-reward endpoint.

{F1142677}

To confirm that I can actually redeem the reward I went ahead and clicked on the redeem button then it asked for en email and I used my hackerone alias email. Just in few seconds a mail arrived in my inbox with the *code* which I can use to get the Logitech mouse for free

{F1142679}
{F1142680}



I checked other features too like Multistreaming, I was able to get the *RTMP url* and *Stream key*
https://streamlabs.com/dashboard#/multistream/settings

Without match and replace rule set:
{F1142690}

After setting match and replace rule:
{F1142698}

--------------------------------------------------------------------------------------------------------------------------------------------------------


**Steps to Reproduce:**

In your burpsuite *Match and Replace* rule add this two entries:

```
1st.
Type: Response Body
Match: false
Replace: true
``` 
```
2nd.
Type: Response Body
Match: "blocked":true
Replace: "blocked":false
```
Similar to this in the screenshot

{F1142700}

1. Now goto https://streamlabs.com/dashboard#/streamlabs-rewards?skipPrimeOnboarding=1
2. The redeem button should be there, as I have shown above in the screenshots F1142677
3. Click on the button , provide your email and you should get the coupon code

Similar steps for checking the multistreaming endpoint,https://streamlabs.com/dashboard#/multistream/settings


**Note:** It might happen that when you  load this url: https://streamlabs.com/dashboard#/streamlabs-rewards?skipPrimeOnboarding=1, this page might appear where it asks you to connect your paypal acc:

{F1142703}

In that case , provide any fake email id and click on continue and also skip the other options also.Once it done now try to open the streamlab-rewards url in a new tab , if it still doesn't works try loading this url instead https://streamlabs.com/dashboard#/streamlabs-rewards (here I have removed the parameter), keep refreshing the page until you get the right one.

--------------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

An attacker can exploit this to get free access to prime features and also get free items at no cost as many as he wants .

**PS:** If you don't mind can I use that coupon code, for getting that sweet gaming mouse for free (it looks really cool lol) , no worries if your answer is no :)

Thankyou
Regards
Sudhanshu

## Attachments
- XmrdC7NQ1V.png
- 1K1Ow4XZhv.png
- kB9rNTOYcg.png
- M24GT6WyfK.png
- 045dggyVXm.png
- In1bDyLVZV.png
- dRdjCNDNX4.png
- firefox_KZCyY6varS.png
