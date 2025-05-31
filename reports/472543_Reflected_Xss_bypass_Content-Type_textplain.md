# Reflected Xss bypass Content-Type: text/plain 

## Report Details
- **Report ID**: 472543
- **URL**: https://hackerone.com/reports/472543
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-27T12:03:40.114Z
- **Disclosed**: 2018-12-28T00:08:33.201Z

## Reporter
- **Username**: ahmed_alwardani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pyca

## Vulnerability Information
Hello Team:
--------------

1 - vulnerable subdomain : ci.cryptography.io
2 - after i tested this subdomain i found many payloads injected by me reflected but not executed
3 - so that i taked alook at the response and i found Content-Type: text/plain 
4 - so i searched about bypass Content-Type: text/plain and i found this book **cure53** page 73 tell me i can bypass it in IE browser before version 10 

POC:
------

- go to https://ci.cryptography.io/adjuncts/20996283/hudsonyfm6u%3Cscript%3Ealert(document.domain)%3C/script%3Epub5j/plugins/favorite/assets.js
- you will see this {F397354}
- so let's try to install IE version 9 to try xss popup
- this is you will see {F397732}

something else ;
what is the java files main ?! {F397734}

## Impact

this method can affect victims that uses the IE browser before version 10 .

## Attachments
- 11.png
- xss.png
- java.png
