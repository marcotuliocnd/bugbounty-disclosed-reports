# Missing captcha and rate limit protection in help form 

## Report Details
- **Report ID**: 1165223
- **URL**: https://hackerone.com/reports/1165223
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-14T20:02:45.110Z
- **Disclosed**: 2021-12-11T13:47:43.795Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
#Hello 
One of your form that you are using to receive help message from users, lack captcha and its backend/server does not  block massive request.
The page is https://mtn.cm/fr/help/

## Steps To Reproduce:
1. Visit https://mtn.cm/fr/help/ and fill all the field and submit.
2. Intercept the request with burp suite and sent to intruder.
3. Clear the payload and select `null payload` then generate 10 payload and click on `start attack` button.
4. Boom! you will see all the response code where `302` means it successfully sent and redirected to success page.   

## Supporting Material/References:
Request
```
POST /handle-forms/help_submit_form.php HTTP/1.1
Host: mtn.cm
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------425351903833406577801167297086
Content-Length: 743
Origin: https://mtn.cm
DNT: 1
Connection: close
Referer: https://mtn.cm/help/
Cookie: qtrans_front_language=en; _fw_crm_v=0279789c-60ed-4e7d-9599-ae776a8b7ddb
Upgrade-Insecure-Requests: 1

-----------------------------425351903833406577801167297086
Content-Disposition: form-data; name="mtn-name"

test
-----------------------------425351903833406577801167297086
Content-Disposition: form-data; name="mtn-contact-number"

test
-----------------------------425351903833406577801167297086
Content-Disposition: form-data; name="mtn-surname"

test
-----------------------------425351903833406577801167297086
Content-Disposition: form-data; name="mtn-email"

security@test.hackerone
-----------------------------425351903833406577801167297086
Content-Disposition: form-data; name="mtn-message"

hello please admin ignore this message it is security test
-----------------------------425351903833406577801167297086--
```

All response code
```
HTTP/1.1 302 Found
Server: nginx
Date: Wed, 14 Apr 2021 19:33:51 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/7.3.27
location: /help/help-success
Content-Length: 0

```

  * [attachment / reference]
F1265670

## Impact

1.Attacker can generate unlimited emails with to you.
2. Email flooding attack.
3. If the your are using your database to receive emails, attack can fill your database with junk emails.

## Attachments
- Screenshot_at_2021-04-14_20-35-58.png
