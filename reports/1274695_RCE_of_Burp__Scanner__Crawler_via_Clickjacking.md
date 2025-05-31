# RCE of Burp  Scanner / Crawler via Clickjacking 

## Report Details
- **Report ID**: 1274695
- **URL**: https://hackerone.com/reports/1274695
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-23T04:09:42.135Z
- **Disclosed**: 2023-10-10T08:24:46.196Z

## Reporter
- **Username**: mattaustin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Burp Suite utilizes an embedded Chrome browser for crawling and scanning web applications. The Chrome instance is launched in headless mode, with remote debugging enabled via the remote-debugging websocket port instead of remote-debugging-pipe. As a result, a known XSS vulnerability in Chrome can be leveraged in combination with a JavaScript port sniffing and ClickJacking attack to compromise the WebSocket GUID for the remote debugging channel. Using the provided remote debugging APIs, it’s possible to trigger a file download to the `/Applications/Burp Suite Professional.app/Contents/` directory with a new `user.vmoptions` file. This will provide the `-Xmx5m` and `-XX:OnOutOfMemoryError=open -a Calculator` flags to JVM the next time that Burp Suite is launched. Accordingly, Burp Suite will quickly exhaust the available JVM memory and trigger the supplied OS command.

Based on Google’s security impact guidelines, this issue would typically be considered to have no security impact since Chrome requires additional flags to run (`--remote-debugging` and `--headless`) [1]. Additionally, the XSS vector used in this PoC has been public to Chrome since at least 2016 and reported in multiple tickets [2-6]. As a result, we are reporting this as a Burp Suite vulnerability since the named pipe transport could be utilized to mitigate this issue, which is supported by tools like puppeteer (e.g. `--remote-debugging-pipe`) [7]. 

### POC: 
See attached video. 

### Steps to reproduce:

To confirm this issue, perform the following steps:

1. Download the attached ‘burp.html’ exploit, and host it on a web server (e.g. `python -m http.server`)
2. Launch an instance of Burp Suite, and start a new scan of the web server.
3. Open a Chrome browser and navigate to the hosted exploit page (e.g. http://127.0.0.1:8000/burp.html)
4. Observe that a JavaScript port scanner is determining the randomized port listening for Chrome remote debugging. After the port is identified, a clickjacking payload will be rendered on the page. 
5. After clicking the ‘CLICK ME!!!’ button, restart Burp Suite and observe that the Calculator app has been launched. 

### References:
[1] https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/security-labels.md#TOC-Security_Impact-None
[2] https://bugs.chromium.org/p/chromium/issues/detail?id=607939
[3] https://bugs.chromium.org/p/chromium/issues/detail?id=618333
[4] https://bugs.chromium.org/p/chromium/issues/detail?id=619414
[5] https://bugs.chromium.org/p/chromium/issues/detail?id=775527
[6] https://bugs.chromium.org/p/chromium/issues/detail?id=798163
[7] https://github.com/puppeteer/puppeteer/blob/943477cc1eb4b129870142873b3554737d5ef252/src/node/PipeTransport.ts

## Impact

After successful exploitation an attacker can gain control over victim's computer with the same permissions as the user running the scanner.

## Attachments
- burp_rce.mp4
- burp.zip
