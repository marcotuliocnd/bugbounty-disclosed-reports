# Bypassing Digits web authentication's host validation with HPP

## Report Details
- **Report ID**: 114169
- **URL**: https://hackerone.com/reports/114169
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-02T16:44:27.070Z
- **Disclosed**: 2016-08-12T17:30:08.804Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue on Digits web authentication which allows attackers to retrieve the OAuth credential data of an application victims authorized.

#Detail
As described in #108429, the login page has 2 parameters, *consumer_key* and *host*. The former identifies which app a user wants to authenticate, and the latter specifies which domain the OAuth credential data is sent to after authentication. In order to prevent other websites to pretend to be the application, the *host* parameter will be validated to see if it matches the registered domain of the app. Take Periscope as an example:

> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.periscope.tv

host=https://www.periscope.tv matches the registered domain

If we modify it:

> https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fattacker.com

host=https://attacker.com does not match the registered domain, thus the page will show an error.

However, the validation can be bypassed with HPP (HTTP Parameter Pollution). If we supply multiple *host* parameters, the validation will only compare the first one but the last one is used in the transfer step instead.

For example:

>https://www.digits.com/login?consumer_key=9I4iINIyd0R01qEPEwT9IC6RE&host=https%3A%2F%2Fwww.periscope.tv&host=https%3A%2F%2Fattacker.com

The first *host* (host=https://www.periscope.tv) is validated but not the second one. After authentication the second *host* (host=https://attacker.com) is used as the transfer origin.

#Impact

It affects every application that has integrated Digits, and even official application (Periscope). Attacker can abuse the flaw to login to victim's account on the affected applications.

#PoC
1. Prepare a Periscope account which is associated with a phone number
2. Login to Periscope using the phone number with digits web login flow: http://innerht.ml/pocs/digits-host-validation-bypass-hpp/
3. After that your account will be renamed as "Pwn3d"

#Fix
Make sure the validated *host* is the same as the one used as the transfer host, or return error if HPP detected

## Attachments
No attachments
