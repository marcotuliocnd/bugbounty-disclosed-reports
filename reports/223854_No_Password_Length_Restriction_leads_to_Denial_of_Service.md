# No Password Length Restriction leads to Denial of Service

## Report Details
- **Report ID**: 223854
- **URL**: https://hackerone.com/reports/223854
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-25T18:04:39.122Z
- **Disclosed**: 2017-05-17T14:08:18.279Z

## Reporter
- **Username**: ant_pyne
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Weblate,

I am trying to register for an account when I came across a page where the password was required to be set up. The url is https://demo.weblate.org/accounts/password where the password was to be created after one provides his or her initial details.

There is no limit to the length of the password that can be created for this site. Hence, I tried with a big payload and everytime server responded me with a 500 internal server error. But when I registered with Antara007! password, it was accepted gleefully. Password length is something that might sound quite insignificant but is quite important.

You need to decrease password length :There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for Denial Of Service attack.

Normally all sites have a password minimum to maximum length like 72 characters limit or 48 limit to prevent Denial Of Service attack. in my sql but in weblate registration page there are no limitation. Let me know if you need any more details.

I am attaching some screenshots so that it can be understood properly.

Thanks,
Dipmalya Pyne.

## Attachments
- servercrash.jpg
- lengthypassword.jpg
