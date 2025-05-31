# Authentication Bypass - Chaining two vulnerabilities leads to account takeover at en.instagram-brand.com

## Report Details
- **Report ID**: 209008
- **URL**: https://hackerone.com/reports/209008
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-26T02:41:50.008Z
- **Disclosed**: 2019-06-22T14:12:38.392Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**Product / URL**
https://en.instagram-brand.com/wp-json/brc/v1/login/

**Description and Impact**
An attacker can perform account takeover by leveraging following two vulnerabilities:

Auth Bypass = Username Enumeration + Login Brute Force



A. Username Enumeration:
-------------------------------

For the site https://en.instagram-brand.com/, it is made sure that a malicious user cannot enumerate usernames of the users by implementing CAPTCHAs at Sign Up (https://en.instagram-brand.com/register/signup) and Forgot Password (https://en.instagram-brand.com/register/signin) pages.
This is made the site secure.
But I have found a way to bypass this protection. The endpoint: https://en.instagram-brand.com/wp-json/brc/v1/resend-verify has absolutely no rate limiting, thus a malicious user can take its advantage to enumerate usernames.

**Another thing of concern is that, if a valid username is found, then the Instagram site sends an account verification link to that email. Even if the account is previously verified !! And if those victims try to login, then they can't. The site asks to first verify their account by clicking on the account activation links !!**

An attacker can harvest the usernames and abuse this functionality to bother the victims.

**Following is the analysis:**
1) The endpoint to which the actual request goes - https://en.instagram-brand.com/wp-json/brc/v1/resend-verify
2) The total number of requests/attempts you were able to make - 1001 (you can do it infinite)
3) The time in which you made those requests/attempts - 10 minutes
4) Some demonstration that you weren't actually just silently locked out -Refer the attached exploit.

**Exploit Developed:**
1. Save the files email.txt and InstagramBrandEnumerationExploit.rb in a folder.
2. Run the exploit like this: ruby InstagramBrandEnumerationExploit.rb
3. Observe in the console that the right emails are disclosed within seconds.


**Reproduction Instructions / Proof of Concept**
1. Sign Up using any email address.
2. Attach a local intercepting proxy.
3. After signing up, a resend email button will appear.
4. Click on it and intercept the request.
5. For the parameter, 'email' in the request body, put your payloads i.e. email addresses to need to be enumerated.
6. Send the request.
7. Observe the response. It is verbose and states clearly if the user exists or not.
8. Now try to login using any of the victim's email.
9. Observe that the web app does not let you login.

**The HTTP Request is:**

`POST /wp-json/brc/v1/resend-verify HTTP/1.1
Host: en.instagram-brand.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-WP-Nonce: 30436dbdab
Content-Type: application/x-www-form-urlencoded
Referer: https://en.instagram-brand.com/register/signup
Content-Length: 29
Cookie: pll_language=en; _ga=GA1.2.2112289023.1486871994; _gat=1
Connection: keep-alive`

`email=<your email here>`




B. Login Brute Force
-----------------------

The endpoint https://en.instagram-brand.com/wp-json/brc/v1/login/ does not have any rate limiting. This still allows an attacker to make the following number of guesses from one single system single threaded : 100 per min, 6,000 per hour, 1,44,000 per day or 43,20,000/month. No additional protection mechanism such as Captcha (pre-auth) or account lockout requiring additional email/phone verification (pre- or post-auth) were identified at any time. I could make 1020 attempts in 10 minutes.

**Solution:**
Implement a Captcha after a reasonable number of failed login attempts against one account at the application-layer. The Captcha should not only be shown to offending IP addresses, but to anyone who attempts to login to the account under attack. Another option is to enable an account lockout policy which effectively locks down an account that has been attacked (e.g. after 20 failed consecutive logins) and requires out-of-band validation by the real account owner (e.g. email, mobile) before becoming accessible again.


**Reproduction Instructions / Proof of Concept**
I have developed an exploit in Ruby to demonstrate this attack. 
Its usage:
1. Save the InstagramBrandLoginBruteForce.rb in any folder.
2. Have a long list of passwords in passlist.txt file and keep it in the same folder.
3. On line number 7, enter the name of the victim's email who you want to target. This can also come from username enumeration list fetched from the exploit InstagramBrandEnumerationExploit.rb
4. Using cmd, navigate to that folder and run it like this: ruby InstagramBrandLoginBruteForce.rb
5. Observe the results.


**Additional Note:**
I have used single threading for these attacks, but these can be more powerful if multi threading is used.

## Attachments
- emails.txt
- InstagramBrandBruteForceResults1.PNG
- InstagramBrandLoginBruteForce.rb
- InstagramBrandEnumerationExploit.rb
- InstagramBrandUsernameEnumeration.png
