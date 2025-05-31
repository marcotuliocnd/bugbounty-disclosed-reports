# Weblate |Security Misconfiguration| Method Enumeration Possible on domain 

## Report Details
- **Report ID**: 230648
- **URL**: https://hackerone.com/reports/230648
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-22T12:01:17.539Z
- **Disclosed**: 2017-07-02T09:52:10.142Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team, I have found  an instance in application where application is alllowing OPTIONS method to be processed in  HTTP request  from weblate.org and in response to my request i got the information that these methods are allowed by application server "GET, HEAD, OPTIONS"

Ideally server should not entertain this request in any manner however i am able to get the info that which http methods are enabled here like HEAD,PUT & GET

Please see the below attached screenshots for issue details.


Url on which i found this issue-https://weblate.org/de/  (request triggered on changing the language preference)

Please also refer -https://www.owasp.org/index.php/Test_HTTP_Methods_(OTG-CONFIG-006)


Original request used here is mentioned below 

GET /de/ HTTP/1.1
Host: weblate.org
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
DNT: 1
Referer: https://weblate.org/en/hosting///!!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20
Cookie: _pk_id.12.9077=5a7069a52632bdf8.1495441748.3.1495453361.1495453006.; _pk_ses.12.9077=*
Connection: close




## Attachments
- Request_N_Response-Method_Enumeration_Possible.png
