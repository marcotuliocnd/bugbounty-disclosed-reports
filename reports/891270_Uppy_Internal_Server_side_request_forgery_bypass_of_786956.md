# [Uppy] Internal Server side request forgery (bypass of #786956)

## Report Details
- **Report ID**: 891270
- **URL**: https://hackerone.com/reports/891270
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-04T20:42:14.550Z
- **Disclosed**: 2020-06-28T13:50:00.398Z

## Reporter
- **Username**: mahmoud0x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report `Internal Server-side request forgery` in Uppy
It allows the attacker to easily extract information from internal servers

# Module

**module name:** Uppy
**version:**1.15.0
**npm page:** `https://www.npmjs.com/package/uppy`

## Module Description

Uppy is a sleek, modular JavaScript file uploader that integrates seamlessly with any application. It’s fast, easy to use and lets you worry about more important problems than building a file uploader.

## Module Stats

[1] weekly downloads: 37,599

# Vulnerability
Server-Side Request Forgery (SSRF)
## Vulnerability Description

When I checked your fix on #786956, I noticed that you fixed this issue by doing a check on the host 's IP address against a blacklist before passing it to the server to fetch (You can check that [here](https://github.com/transloadit/uppy/blob/7525440229bde28241e34ba3eacf3fad77269c05/packages/%40uppy/companion/src/server/helpers/request.js), But you forgot to stop redirection to these IP addresses, therefore attacker can create a host or file and redirect all requests which are being received to a specific internal host, this will bypass your check, in the first phase, System will check if this host is allowed or no, if it is allowed, Server will pass the request. But it won't be able to verify which host is being redirected to. 

## Steps To Reproduce: 

+ feel free to set up a custom Uppy version on your server and try these steps on

1. Go to https://uppy.io/
2. Choose download file via a link 
3. Pass this link to the system `https://tinyurl.com/gqdv39p` (it redirects to `http://169.254.169.254/metadata/v1/`)
4. Upload fetched file
5. Download that file
6. Open that file and you should see a copy of DigitalOcean 's metadata host response
██████



## Supporting Material/References:
███ 

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Unauthorized access to sensitive info on internal hosts/services.

## Attachments
No attachments
