# Domain spoofing in redirect page using RTLO

## Report Details
- **Report ID**: 299403
- **URL**: https://hackerone.com/reports/299403
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-19T16:42:34.965Z
- **Disclosed**: 2018-01-30T03:46:00.489Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello,

Domains can be spoofed on redirect page using RTLO. 


**Description (Include Impact):**

Using  `http://username@domain.com` & `RTLO` method, i found a way where redirect page host detection can be spoofed

#Steps
 1. Insert this on report  `[Just Click Here](https://google.com@%E2%80%AE@moc.rettiwt)`
2. On click of link, it will redirect to `/redirect` page . Here you will see that `Twitter.com` is highlighted domain. see screen shot below
3. Ideally, if there is any malformed url, it shows some kind of warning but not in this case.
4. Click on `Proceed` button and you will be redirected `https://moc.rettiwt/` instead


### Browser version, Device, etc
Tested on chrome for Mac but should work in all browsers
 
#POC link

https://google.com@%E2%80%AE@moc.rettiwt

###Screenshots

 {F248121}

## Impact

This can be used to spoof urls on hackerone 

Regards,
Ashish

## Attachments
- Screen_Shot_2017-12-19_at_10.08.08_PM.png
