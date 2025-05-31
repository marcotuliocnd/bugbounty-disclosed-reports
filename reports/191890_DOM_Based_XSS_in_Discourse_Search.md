# DOM Based XSS in Discourse Search

## Report Details
- **Report ID**: 191890
- **URL**: https://hackerone.com/reports/191890
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-17T07:29:05.576Z
- **Disclosed**: 2017-01-10T00:08:01.948Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
###Steps to Reproduce:

1. Load http://try.discourse.org
2.Now From Top Right Corner Click on Search Button 
3. Enter payload their 

###Payload:

@<script>prompt(1337)</script>gmail.com

4: Now in new windows that opens click on advance search and The XSS will Occur :) 
5: Now copy the link and send to victim there the XSS will Occur To 

Thanks
Khizer Javed 


## Attachments
No attachments
