# Pixel Flood Attack leads to Application level DoS

## Report Details
- **Report ID**: 970760
- **URL**: https://hackerone.com/reports/970760
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-30T15:13:07.634Z
- **Disclosed**: 2020-11-05T11:05:47.954Z

## Reporter
- **Username**: mr_vrush
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hello Team,
      I had gone through your policy and I saw that DoS is out of scope but I am not sure about Application level DoS. The another reason to report  this attack because it affects  real customers who want to chat with your support team. I had tested this with two accounts 

1. From Account 1 I had tried to send 64K * 64K resolution image 
2. Simultaneously from Account 2 I had tried to  send normal image (with different Internet Connection).
3. The response was 502 for both images.

## Steps To Reproduce:
1.  Go to cs.money and login with Account1, Login Account2 on different device with different Internet Connection.
2.  Now Find Support symbol.
3.  Click on attachments and upload "lottapixel.jpg"  from Account1. 
4. Simultaneously upload normal image from Account2.  


## Supporting Material/References:
https://hackerone.com/reports/752073
https://hackerone.com/reports/752010
If you need more information please let me know.

  * [attachment / reference]
From: Device 1,  Account1 
Image "lottapixel.jpg" is Payload
Image "502.PNG" is proof of attack is successful.

From: Device 2, Account2
Image "upload timing from account2.png" and "Account2.png"  is proof that real users are also affected.

## Impact

Real User are not able to send images to the support team.  It affects to the availability  of resource.  I had recorded 1.2 min downtime. 
Thanks

## Attachments
- lottapixel.jpg
- 502.PNG
- upload_timing_from_account2.png
- Account2.png
