# previous token seems to work even though it does not verify email

## Report Details
- **Report ID**: 263672
- **URL**: https://hackerone.com/reports/263672
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-26T19:16:57.958Z
- **Disclosed**: 2019-11-27T09:58:07.344Z

## Reporter
- **Username**: rashedhasan007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi there , 

Summery :
---------------------

the same confirmation token can be reused for the email address , wheres the previous token and the new token are not same . while the user tries to confirm his email with previous token , it will be confirmed . which means that token does not expires . 

Proof Of Concept:
--------------------

- Open your wakatime account with email `tester@test.com`. 
- a verification link arrives to your email address looking like this 

```

 https://wakatime.com/confirm_email/9ec1b0e0-6993-4dce-972f-73670d340557/764af9cc-766c-4d1c-ba13-cfaa00bdd9b8/2017-08-27T18:36:48Z/e4c09969934e90ecd2e81a5ea21e047a808a6cd9

```

- verify your email address . 
- Now remove your email address and put any other email address like `h1test@example.com` 
- the system asks for to verify this , but without verifying we can also login . 
- Now if we use the previous email address the system will not let us log in . 
- however now login again with new email  `h1test@example.com` and password . 
- change your email to previous one which is `tester@test.com`.
- System prompts to verify , a new confirmation link arrives looking like this 

```
https://wakatime.com/confirm_email/9ec1b0e0-6993-4dce-972f-73670d340557/764af9cc-766c-4d1c-ba13-cfaa00bdd9b8/2017-08-27T18:51:38Z/2d95b3756346f163507aee82a1324df280a17a39
```


- here we observe the following part is different from our previous token , which shows the time frame and another unique generated part 

```
2017-08-27T18:51:38Z/2d95b3756346f163507aee82a1324df280a17a39
```
- So now instead of using the new token use the previous token and it confirms the email address . 
- This works every time you add your email 
- you can ignore all the new token and use the previous first one arrived at your address . 
- Which should expire after one use as the token are actually not same , they are different 


Possible Remediation:
--------------------

As mentioned a token should expire after single use .  I tested it quite a few times and confirming it works as the PoC . 


 I hope you will look into this . 

Sincerely , 
Rashed 




## Attachments
No attachments
