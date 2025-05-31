# Missing Rate Limiting protection leading to mass triggering of e-mails

## Report Details
- **Report ID**: 224927
- **URL**: https://hackerone.com/reports/224927
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-29T13:05:35.781Z
- **Disclosed**: 2017-06-05T06:35:55.592Z

## Reporter
- **Username**: giligails
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The issue is that there is a speed bump missing in the subscription of e-mail for a user. This would eventually let the attacker spam to *any* random e-mail resulting in exhaustion of resources on your side and I see that you are using Amazon AWS's SES where you are charged per e-mail.  If a dedicated attacker wants to, he/she create significant loss at his/her whim and fancy. 

The mails can be triggered to a specific user , post his/her confirmation to subscription thereby causing frustration to users due to flooded inbox, consequently forcing users to classify emails from your application as SPAM . 

 This poses a significant threat to the integrity and reputation of your organisation. 

The request which when captured triggers mails.
POST /?p=subscribe&id=1 HTTP/1.1
Host: newsletter.nextcloud.com
Host: google.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Referer: https://newsletter.nextcloud.com/?p=subscribe&id=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 199
Cookie: PHPSESSID=15vcjnijfjq2vlo8ihpkcdk9f3
Connection: close
Upgrade-Insecure-Requests: 1

email=testonhackerone%40gmail.com&emailconfirm=testonhackerone%40gmail.com&htmlemail=1&list%5B3%5D=signup&listname%5B3%5D=Nextcloud+newsletter&VerificationCodeX=&subscribe=Subscribe+to+the+newsletter

Proof of Concept / Steps to reproduce: 

1. Copy the request to the Burp Intruder
2. Now, paste the target and the request and set the options to Null Payloads. 
3. Intrude the request say 10 times to the target email. 
4. You can see the e-mails being spammed to your inbox. 

Attached is the screenshot showing count of mails triggered post confirmation of subscription(61) due to the capture of request.

Also, confirming the e-mail doesn't make that confirmed user immune to this attack. The e-mail spam attack can be performed even if the user has previously confirmed. 

POC: 
1. Confirm the subscription once and try the same again. 

I'd be more than happy to assist you with anything regarding the issue. 

Look forward to hear from you. 

Have a happy day. 


## Attachments
- NextCloud.PNG
