# Stored XSS in the Custom Logo link (non-Basic plan required)

## Report Details
- **Report ID**: 282209
- **URL**: https://hackerone.com/reports/282209
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-23T20:49:44.789Z
- **Disclosed**: 2017-11-23T12:56:01.220Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
##Description
Hello. Recently i contacted with Infogram, and requested trial of the Business version to test some features, which was unavailable in the Basic version.
I discovered the stored cross-site scripting issue in the Custom Logo link.
{F232084}
There was some URL checks in place, but i was able to bypass them, because position of the `http[s]://` was not checked (string could start with other arbitrary symbols)


##POC
Visit this infographic:
https://infogram.com/your-first-project-title-1ggk269n94yj2n0
Scroll to the end of the page, and click the logo in the borrom-right (green triangle):
{F232086}
The XSS with `document.domain` payload will be executed.

##Reproduction steps
1) You need a Business account.
2) Visit the https://infogram.com/app/#settings/infographic -> `Project Settings`
3) Change the logo link to the
```
javascripT://https://google.com%0aalert(1);//https://google.com
```
4) Create some infographic, make it public, visit and click the logo

##Why it works
The `javascript` string was blacklisted, but using capital letter, i was able to bypass the filter.
`javascript:alert` didn't work (looks like due to the protocol check - `http://` became appended to the payload),
but `javascripT://` successfully bypassed the filter. Now, since it checks for the `http[s]` protocol, we can bypass it using comment:
```
javascripT://https://google.com%0aalert(1);//https://google.com
```
When clicking such link, 
browser sees it as `javascript:` payload with following JS code:
```
//https://google.com
alert(1);
//https://google.com
```

##Suggested fix
The validator should check, that Logo Link string must strictly start with `http[s]://`.


## Attachments
- test.JPG
- c.JPG
