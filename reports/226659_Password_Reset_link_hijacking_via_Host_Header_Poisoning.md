# Password Reset link hijacking via Host Header Poisoning 

## Report Details
- **Report ID**: 226659
- **URL**: https://hackerone.com/reports/226659
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-07T00:41:10.943Z
- **Disclosed**: 2017-06-06T01:37:41.675Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
## Summary
Concrete5 uses the `Host` header when sending out password reset links. This allows an attacker to insert a malicious host header, leading to password reset link / token leakage.

## Impact
The victim will receive the malicious link in their email, and, when clicked, will leak the user's password reset link / token to the attacker, leading to full account takeover.

## Reproduction
1.) Open up Firefox and Burp Suite.)
2.) Visit the forgot password page `(/index.php/login/concrete/forgot_password)`
3.) Enter the victim's email address and click `Reset and Email Password`
4.) Intercept the HTTP request in Burp Suite & change the `Host` Header to your malicious site / server.

Example:
{F182477}

5.) Forward the request and you'll be redirected to your server.

The victim will then receive a password reset e-mail with your poisoned link.
{F182478}

If the victim clicks the link, the reset token will be leaked and the attacker will be able to find the reset token in the server logs. The attacker can then browse to the reset page with the token and change the password of the victim account!


This can also be reproduced using the **curl** command
```
curl -i -s -k  -X $'POST' \
   -H 'Host:sxcurity.pro' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Referer: http://<TARGET>/index.php/login/callback/concrete/forgot_password' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'<COOKIES>' \
    --data-binary $'ccm_token=1494113992%3A02eb0471b7b6e3a498ba7e6b57573b04&uEmail=hacker1337%40mailinator.com&resetPassword=' \
    $'http://<TARGET>/index.php/login/callback/concrete/forgot_password'
```

## Patch
Use `$_SERVER['SERVER_NAME']` rather than `$_SERVER['HTTP_HOST']`

## References
 http://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html 

Thanks!
-Corben [(@sxcurity)](https://twitter.com/sxcurity)

ps: crayons

## Attachments
- concrete5_poc.png
- poisoned_link.png
