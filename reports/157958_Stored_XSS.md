# Stored XSS

## Report Details
- **Report ID**: 157958
- **URL**: https://hackerone.com/reports/157958
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T20:13:55.861Z
- **Disclosed**: 2016-09-09T00:14:59.475Z

## Reporter
- **Username**: s44mux
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
First log in account.

We headed to the "lists and recipes" option

https://www.instacart.com/store/demo/lists


create a new list "add list"

Payload
"></script></title><script>alert(document.domain)</script>


URL pwned.

https://www.instacart.com/lists/izy0w6Q?preview=true

attached a screenshot



## Attachments
- Stored_XSS.PNG
