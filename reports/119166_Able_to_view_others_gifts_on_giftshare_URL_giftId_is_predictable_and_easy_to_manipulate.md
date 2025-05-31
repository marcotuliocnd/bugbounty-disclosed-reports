# Able to view others' gifts on /gift/share URL, giftId is predictable, and easy to manipulate

## Report Details
- **Report ID**: 119166
- **URL**: https://hackerone.com/reports/119166
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-27T18:39:02.265Z
- **Disclosed**: 2017-03-26T00:06:47.666Z

## Reporter
- **Username**: caffeinewriter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
I recently purchased a gift for a friend, and noticed the share URL gift ID was simply numeric. I managed to access other people's gifts simply by incrementing and decrementing the ID by 2, I was able to verify that the price was dropped to "Free", regardless of if I was logged in or not, and I was able to successfully redeem a gift to an account, even if it was not associated with the gift email, or the account that initially purchased the gift. 

### Scope:
This affects Udemy.com at the /gift/share/ endpoint. Reveals name and email of recipient of gift, as well as exposing the gift redemption code.

### Example URLs:
https://www.udemy.com/gift/share/?giftId=559076 (mine)
https://www.udemy.com/gift/share/?giftId=559078 (not mine, but still able to access it [giftId incremented by 2])

### Replication:
1. From a valid URL, increment or decrement the giftId parameter by 2.
2. Visit the course page, and add the `couponCode` parameter with the coupon code as the value to verify the code is valid, or enter it in the "Redeem a Coupon" box. 
3. Check out, and you will be able to redeem another person's gifts.

### Suggested Actions to Rectify Issue:
1. Require user to be authenticated, and only allow them to view their purchased gifts.
2. If you want to give unauthenticated access, use randomly generated IDs instead of sequential IDs. 

## Attachments
- chrome_2016-02-26_15-49-18.png
- chrome_2016-02-26_15-51-37.png
- chrome_2016-02-26_15-52-47.png
- chrome_2016-02-26_15-54-07.png
- chrome_2016-02-27_09-29-56.png
- chrome_2016-02-27_09-36-00.png
