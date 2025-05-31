# Verification of email addresses possible through https://www.yelp.com/signup/facebook

## Report Details
- **Report ID**: 194721
- **URL**: https://hackerone.com/reports/194721
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-29T23:22:33.676Z
- **Disclosed**: 2017-09-16T19:50:06.460Z

## Reporter
- **Username**: coder13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hi,

There is an issue with the https://www.yelp.com/signup/facebook endpoint which allows an attacker to validate whether a specific email address is registered on Yelp. There seems to be no rate limit nor a validation for already used CSRF tokens.

Steps to reproduce:

1. Go to https://www.yelp.com/login?return_url=%2F and sign up with a facebook account which is not linked to any yelp account yet.
2. After confirming the access on FB, yelp will request to enter an email address and a password, as well as the ZIP code to finish the account creation. Enter any email address/password/zip code.
3. Capture the request to https://www.yelp.com/signup/facebook with a HTTP sniffer.

The request body like this (unvalidated/unimportant parameters are ommited):

```
first_name=<FIRSTNAME>&last_name=<LASTNAME>&fb_access_token=<FB_TOKEN>&email=<EMAIL>&post_csrf=<CSRF>&csrftok=<CSRFTOK>&password=<PASSWORD>&zip=<ZIP>
```

The response if the email address is already used by another user:

```
{
   "errors":[
      "The email address you entered has already been registered."
   ],
   "require_link":false,
   "success":false,
   "error_fields":[
      "email"
   ],
   "show_captcha":false,
   "return_url":"https://www.yelp.com/cookie_bridge/store?dhl=en_US\u0026redir=https%3A%2F%2Fwww.yelp.com%2Ffind_friends%2Ffacebook",
   "associated_email":true
}
```

Should the email address not be used by any user, we get the following response:

```
{
   "errors":[

   ],
   "photo_id":"<PHOTO_ID>",
   "success":true,
   "error_fields":[

   ],
   "show_captcha":false,
   "return_url":"https://www.yelp.com/cookie_bridge/store?dhl=en_US\u0026redir=https%3A%2F%2Fwww.yelp.com%2Ffind_friends%2Ffacebook"
}
```

Knowing how the responses look like and having a valid cookie collection, as well as the values for **post_csrf** and **csrftok** parameters and the FB access token from the captured request, an attacker can test a large list of email addresses against the https://www.yelp.com/signup/facebook endpoint. I could submit hundreds of requests to the given endpoint within a short time with the `hackerone@test.com` email address whch definitely indicates that there is no rate limit.

## Attachments
- Screenshot_3.png
