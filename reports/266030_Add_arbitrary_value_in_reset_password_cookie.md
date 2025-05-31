# Add arbitrary value in reset password cookie

## Report Details
- **Report ID**: 266030
- **URL**: https://hackerone.com/reports/266030
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-05T13:23:42.848Z
- **Disclosed**: 2018-02-01T14:41:09.454Z

## Reporter
- **Username**: cuso4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
I recently discovered that we can add arbitery value in reset pass token and compromise the life time unlimitedly ..

After opening a reset password link I got these cookies ....for token expires timeout .

{
    "domain": ".app.legalrobot.com",
    "expirationDate": 1504618468.82726,
    "hostOnly": false,
    "httpOnly": false,
    "name": "tokenExpires",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "Tue%20Sep%2005%202017%2013%3A35%3A30%20GMT%2B0000%20(UTC)",
    "id": 2
}


There was a warning in a page like .....

Your password reset token expires in 21 minutes...

okay so I decoded the value and changed year to 2019 instead of 2017 ...and it's all done ....miracle i got this page  with different warning ...

Your password reset token expires in 2 years

okay there are some issue like content spoofing , attacker can do this again and again , generally after 21 minutes token must experies but after changing to two years it won't ....


attaching screenshot here ....

If you can please take a another look  #265652  i have attached a logical bug with fully video poc 


thanks again

## Attachments
- Screenshot_at_2017-09-05_18-47-54.png
