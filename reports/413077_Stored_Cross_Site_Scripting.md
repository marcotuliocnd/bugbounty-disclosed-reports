# Stored Cross Site Scripting.

## Report Details
- **Report ID**: 413077
- **URL**: https://hackerone.com/reports/413077
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-23T12:23:24.011Z
- **Disclosed**: 2020-07-21T17:12:40.995Z

## Reporter
- **Username**: sakhauathr99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
Hellow team 
I got Stored based XSS on your web :D

Here Is Step :

1. Go to https://www.easycontactnow.com/
2. Click "Try For Free" (Sign Up)
3. It will told you "Enter your details to get started". 
   So Enter your full name like : "><script>alert(1)</script>
   Then put all the other details.
4. Then Confirm your id and login.
5. Then Click dashboard and other thing :) 
6. Tada script executed done :D

POC : https://www.youtube.com/watch?v=gYyCAxaB6w0

Sorry for my bad english. 

Thanks :)

## Impact

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS.

## Attachments
No attachments
