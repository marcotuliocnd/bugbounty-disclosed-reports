# Internal Path Disclosure

## Report Details
- **Report ID**: 979110
- **URL**: https://hackerone.com/reports/979110
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-11T03:33:30.464Z
- **Disclosed**: 2020-09-11T16:12:21.778Z

## Reporter
- **Username**: mr_vrush
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
Hello Team,
       I would like to report internal path disclosure in response. I was trying for Stored XSS but got no luck in that process. I observed the responses, one of the responses showing file path with 500 Internal Server Error. 

## Steps To Reproduce:

1. Go to cs.money and sign in through steam account.
2. Now click on chat support icon
3.  Now try to upload file while uploading capture the request in burp and send it to the repeater.
4.  Edit the request as shown in below. 

------------------------------------------------------------------------------------------------
Content-Disposition: form-data; name="file"; filename="/../../../../../.html"
Content-Type: image   text/html
Content-Type: text/html

-------------------------------------------------------------------------------------------------
 "5. After editing forward the request and observe the response.
   "6. Response is 500 Internal Server Error with these two path in the response.

## Supporting Material/References:
1. Image █████ shows edited part of the request.
2. Image █████ shows the response.
3. Image ███████ shows response in the browser.

## Impact

This issue is not a major threat to security, but this information usually contains sensitive information.

## Attachments
No attachments
