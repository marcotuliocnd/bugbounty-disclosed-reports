# ClickJacking

## Report Details
- **Report ID**: 947690
- **URL**: https://hackerone.com/reports/947690
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-30T08:40:20.903Z
- **Disclosed**: 2021-03-16T09:44:10.788Z

## Reporter
- **Username**: salna_kuruvi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
I have found the vulnerability called Clickjacking.

Please find the details below:

Description     

Clickjacking is an exploit in which malicious coding is hidden beneath apparently legitimate buttons or other clickable content on a website.

  OWASP Benchmark   A6- Security Misconfiguration  


Steps to Reproduce   

1.Craft an HTML page and add the following 
( https://www.acronis.com/en-in/ ) of the application within an iframe.

2.Save the file as *.html and run the file.

3.Open the HTML page in a browser.

4.The following attached screenshot shows webiste is in frame.

Please find the attached screenshot for your reference. 

High Level Fix Recommendation

Clickjacking attacks can be avoided by setting the X-Frame-Options header or by using frame busting code which check if the current web page is the top web page (not within a frame).

## Impact

Impact 

Multitude of attacks including key logging and stealing user credentials.

## Attachments
No attachments
