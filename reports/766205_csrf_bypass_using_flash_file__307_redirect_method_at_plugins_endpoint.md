# csrf bypass using flash file + 307 redirect method at plugins endpoint

## Report Details
- **Report ID**: 766205
- **URL**: https://hackerone.com/reports/766205
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-30T19:59:15.099Z
- **Disclosed**: 2020-02-10T08:38:16.876Z

## Reporter
- **Username**: qotoz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Hi Security team,

i have found that the request sent to https://my.stripo.email/cabinet/stripeapi/v1/plugin/$userid$/plugins     don't have any protection against csrf attacks as the server only validates that the content type is application/json and this can be bypassed using the flash file + 307 redirect technique 


Steps To Reproduce:

  1.  login to your account at https://my.stripo.email
  2.  visit https://thehackerblog.com/crossdomain/
  3.  use this link as php redirector https://testingsubdomain.000webhostapp.com/stripo.php
  4.  in the request headers : Content-Type: application/json;charset=UTF-8
  5. the payload

```
{"email":"attacker@example.com","name":"csrf poc","webUrl":"csrf poc "}
```

 

##Watch the network traffic from the network tab on the Devtools 
##and go back to and refresh the site you'll find all the application data have created


all these steps would be integrated together and performed by the attacker's server

i am attaching a poc video declaring the steps
{F671826}

##Supporting Material/References:
http://www.geekboy.ninja/blog/exploiting-json-cross-site-request-forgery-csrf-using-flash/
http://resources.infosecinstitute.com/bypassing-csrf-protections-fun-profit/#gref
https://blog.cm2.pw/forging-content-type-header-with-flash/

## Impact

attacker can send request to create an application in behalf of user

## Attachments
No attachments
