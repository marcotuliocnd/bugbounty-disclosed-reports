#  credentials leakage in public lead to view dev websites 

## Report Details
- **Report ID**: 511440
- **URL**: https://hackerone.com/reports/511440
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-18T06:40:10.708Z
- **Disclosed**: 2019-03-18T06:49:52.294Z

## Reporter
- **Username**: xsam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Description:**

Hello Zomato team :) 

So after I found a new OSINT website ████ which fetch results from Pastebin website, I searched for "zdev.net" and I got this interesting result ██████████

{F443315}

I logged in https://gazal.zdev.net/test.php after I decoded Base64 Authorisation

```
███
```

{F443316}

I tried to pass the parameters in POST request to see if the website handle it or not but I didn't get any result, the next step was to brute-force directories, I used a simple wordlist but I didn't get any results, then I found that https://gagandeep.zdev.net is also protected with the same basic access authentication credentials. 
for that reason, I contacted Prateek privately to check with him about this point.

## Impact

There is no big impact to my knowledge,  but since there is kind of credentials leakage and authentication bypass I decided to report it.

## Attachments
- Capture_d_e_cran_2019-03-18_a__12.29.29.png
- Capture_d_e_cran_2019-03-18_a__12.32.11.png
