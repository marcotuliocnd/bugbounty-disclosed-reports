# Subdomain takeover on developer.openapi.starbucks.com

## Report Details
- **Report ID**: 275714
- **URL**: https://hackerone.com/reports/275714
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-09T17:46:08.293Z
- **Disclosed**: 2018-02-17T16:34:37.814Z

## Reporter
- **Username**: dpgribkov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi team,

### Summary: 
Subdomain `developer.openapi.starbucks.com` is vulnerable to subdomain takeover via Mashery service. The reason why it's worked unfortunately not fully clear to me.

### Details:
Doing my recent research on starbucks.com subdomains, I stumbled upon http://developer.openapi.starbucks.com/ The server returned 200 response with the following {F227581} The `Server` header of HTTP responce was `Mashery Proxy` so it gave me an idea, that I should go and try register an trial account at https://www.mashery.com/

After registering an account and confirming it, I got access to the dashboard. Under the `Portal Settings` menu there was an option to add your own domain name. I added developer.openapi.starbucks.com as my domain and I get no error. After I went to the http://developer.openapi.starbucks.com/ and saw welcome page {F227586} which gave me understanding that I can serve my own content under developer.openapi.starbucks.com

### PoC:
I added simple js code to the Welcome page `alert(document.domain)` for this proof-of-concept.
To confirm it just click this link http://developer.openapi.starbucks.com/

### Impact:
As I can serve my own content without any restrictions, with this webpage I can set up a campaign to steal user cookie sessions, or use it to steal credentials, or for phishing purposes. 

Please let me know, if you need more information!

Thanks,
Danil

## Attachments
- developers_starbucks_com__216_87_148_114__80.png
- Screenshot_2017-10-09_13.38.41.png
