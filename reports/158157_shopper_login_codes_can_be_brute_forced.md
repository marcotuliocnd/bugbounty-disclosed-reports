# shopper login_code's can be brute forced

## Report Details
- **Report ID**: 158157
- **URL**: https://hackerone.com/reports/158157
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-10T13:29:40.545Z
- **Disclosed**: 2016-09-17T11:56:16.075Z

## Reporter
- **Username**: b6117130df17feef13481e3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi,

I didn't see in the scope of your program, but it is a security weakness, so you must know this. If you don't care about shoppers' accounts then you can just mark this report as informative.

* First I tried to register a shopper account at https://shoppers.instacart.com/
* Used a fake email address and a FAKE phone number, for phone number I entered 888-999-5555
* Then your system sent me my login_code from the url https://shoppers.instacart.com/send_login_code via POST request with the data "utf8=%E2%9C%93&phone=(888)+999-5555"
* And requested me to verify the login_code with the url https://shoppers.instacart.com/verify_login_code via POST request "utf8=%E2%9C%93&phone=(888)+999-5555&login_code=3425&commit=Submit"
* After sending some wrong login_codes, I got the response {"error":"Sorry, but that code is incorrect."} form /verify_login_code with a 404 Header.
* Then I tried to brute force the login code with random numbers ( 5 digits, total possibility 100K )
* login_code was broken on 43K
* response was: {"redirect_to":"/apply"}, and HTTP status was: 200 (changed from 404) 
* tried to login on https://shoppers.instacart.com/login with the phone number, I logged in successfully with the password "instacart" which was sent to my fake email address.
* I also set up a face-to-face interview but canceled later not to make you wait an invisible man :))

These all means you can attack a shopper's accounts by finding by shopper's phone number. 
So, you must limit verifying login code by 3 or 10 attempts (how much you like) to prevent this. 
Then send another code if attacker fails to start over.

Regards.



## Attachments
- insta1.jpg
- insta2.jpg
- insta3.jpg
