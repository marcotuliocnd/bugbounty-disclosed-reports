# Log pollution can lead to HTML Injection.

## Report Details
- **Report ID**: 146278
- **URL**: https://hackerone.com/reports/146278
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-21T17:45:54.187Z
- **Disclosed**: 2016-07-19T11:52:30.229Z

## Reporter
- **Username**: apok
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,
I was looking around in your app and on the log part (accessed by the admin), I noticed that the log file is downloaded as an HTML file. Naturally I started trying to inject code I noticed that when HTML code is inserted, a HTML comment start tag is inserted. But I was able to bypass this protection by inserting a comment end tag and then the HTML code, which resulted in HTML injection.

To reproduce this behaviour I started looking where a user is able to inject data onto the log file, and I noticed that when the "Host" header is different from the one configured for the app, a warning is injected onto the app. There likely many other sections that could serve to inject into the log, but I've just started to analyze the app so I couldn't find any yet.

Proof of Concept:
1) Generate the following request to the server:
GET /nextcloud/index.php HTTP/1.1
Host: -->test"<img src=a onerror=alert('xss')>
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.7,es-AR;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
2) Download the log file.
3) Observe that the code is executed properly.

Why is this a vulnerability?
A malicious individual could use this to execute malicious code on an administrator that happened to open the downloaded Log file. 

How to fix?: We can defeat this attack by adding an additional filter on the log file which escapes html special characters.

I'm sending a couple of screenshots. I'll keep digging and if I find anything else I'll send you another report.

Kind Regards,
Apok.

## Attachments
- Request.png
- Executed_code.png
