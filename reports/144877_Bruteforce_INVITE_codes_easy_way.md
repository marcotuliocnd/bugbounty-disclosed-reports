# Bruteforce INVITE codes easy way

## Report Details
- **Report ID**: 144877
- **URL**: https://hackerone.com/reports/144877
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-15T08:20:23.598Z
- **Disclosed**: 2016-07-26T00:52:43.374Z

## Reporter
- **Username**: blinkms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
As soon as i read the vulnerability disclosed on h1 regarding Possibility to brute force invite codes in riders.uber.com "https://hackerone.com/reports/125505" .

I have found similar & easy way to bruteforce invite codes but in different manner .

Also, 1680 public invites are waiting for exploitation .

It was possible to bruteforce the  invite codes for unlimited times during my test , making invite codes vulnerable to rate-limiting vulnerability & an attacker can gain free rides with that code .

To summarize the issue , I have included a POC .

POC :- 

[1] Go to https://get.uber.com/drive/?invite_code=xez7rgs2u
[2] You  will be redirected to https://partners.uber.com/join/?invite_code=xez7rgs2u
[3] You will see , ISAAC sent you $100

To claim your reward, sign up to drive today.
[4] Now , again go to , https://get.uber.com/drive/?invite_code=rlior&signup_source=facebook_timeline
[5] You will be redirected to https://partners.uber.com/join/?invite_code=rlior&signup_source=facebook_timeline
[6] You will see , PHILLIP invited you to make money with your car.

To claim your reward, sign up to drive today.

[7] I didn't claim above reward but it is of $300 value , which can be known , if you search inurl:https://get.uber.com/drive/?invite_code=    in Google.
[8] Now , again go to https://partners.uber.com/join/?invite_code=jjjjzk
[9] You will see , Uber needs partners like you.
[10] Bruteforce is easy ; 

A rule for detection of following text based bruteforce in response can added in burp suite Intruder > Options > Grep Match  .

Valid Codes  - [3]  Conatains <h1 class="flush--bottom"> ... sent you $100</h1>
Invalid Codes - [9] Contains  <h1>Uber needs partners like you.</h1>
Valid but not sure of $ value - Contains <h1 class="flush--bottom"> .... invited you to make money with your car.</h1>

Another devastating thing i have found here is 1680 invite codes are already public in Google , which if an attacker uses he can ride with Uber always for free with invites codes / new account .

Block url invite_code=.... in robots.txt & remove that from Google search results as well .

POC :- Google site:uber.com inurl:?invite_code=

Screenshots uber1 & uber2 attached .

I didn't used any of the invite codes .


## Attachments
- uber2.png
- uber1.png
