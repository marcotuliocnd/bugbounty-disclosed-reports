# Server Side Request Forgery in Uppy npm module

## Report Details
- **Report ID**: 786956
- **URL**: https://hackerone.com/reports/786956
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-31T16:31:11.869Z
- **Disclosed**: 2020-03-02T07:38:09.438Z

## Reporter
- **Username**: 3sl4m-s4l3m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Team,

While we were testing our security engine at Shieldfy (https://shieldfy.io), We found a server side request forgery (SSRF) vulnerability in Uppy npm package.
It allows hacker to easily extract inside information from the server or take control of internal services.

# Module

**module name:**  Uppy
**version:** Latest: 1.8.0
**npm page:** `https://www.npmjs.com/package/uppy`

## Module Description

Uppy is a sleek, modular JavaScript file uploader that integrates seamlessly with any application. It’s fast, easy to use and lets you worry about more important problems than building a file uploader.

## Module Stats

[1] weekly downloads : 23,153

# Vulnerability
Server Side Request Forgery ( SSRF )

## Vulnerability Description

in the source code of the module
file: [packages/@uppy/companion/src/server/controllers/url.js line: 11](https://github.com/transloadit/uppy/blob/746bbcbbc5dc64203390322b28fb380ec67bd94f/packages/%40uppy/companion/src/server/controllers/url.js#L11)


You will find the express is routing the `/get` endpoint to the [function `get` declared in line 43](https://github.com/transloadit/uppy/blob/746bbcbbc5dc64203390322b28fb380ec67bd94f/packages/%40uppy/companion/src/server/controllers/url.js#L43)

Then it calls [`downloadURL` in line`61](https://github.com/transloadit/uppy/blob/746bbcbbc5dc64203390322b28fb380ec67bd94f/packages/%40uppy/companion/src/server/controllers/url.js#L61) and pass `req.body.url` to it as argument


in the function [`downloadURL`  declared in line 80](https://github.com/transloadit/uppy/blob/746bbcbbc5dc64203390322b28fb380ec67bd94f/packages/%40uppy/companion/src/server/controllers/url.js#L80)


It calls the url directly without any kind of sanitization or validation, opens the door to send malicious ssrf attack, allowing the hacker to extract information from any internal resource, or take control of any internal service.


## Steps To Reproduce:

1. deploy the module in live server (ex: digital ocean server)
2. request 'Add More button' then click on` Link button`
3. Submit Link of DigitalOcean metadata api `http://169.254.169.254/metadata/v1/`
4. once done uploading , download the file you should see the content of the server metadata

```
id
hostname
user-data
vendor-data
public-keys
region
interfaces/
dns/
floating_ip/
tags/
features/
```

## Patch

The suggested fix.
1. use whitelist technique in the url protocol ( allow only http & https ), and on the port ( 80 & 443 )
2. use blacklist technique in the host (disable IPs v4 & v6 allowing only domains, disable domains that used as internal routing if any)
3. disable redirection `followAllRedirects` to avoid bypasses

## Supporting Material/References:

More info about ssrf can be found here : https://shieldfy.io/security-wiki/server-side-request-forgery/server-side-request-forgery/

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

- Scan local or external network
- Read files from affected server
- Interact with internal systems
- Remote code execution

## Attachments
No attachments
