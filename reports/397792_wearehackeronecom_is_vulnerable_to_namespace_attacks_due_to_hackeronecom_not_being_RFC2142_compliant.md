# @wearehackerone.com is vulnerable to namespace attacks due to hackerone.com not being RFC2142 compliant.

## Report Details
- **Report ID**: 397792
- **URL**: https://hackerone.com/reports/397792
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-21T15:11:18.461Z
- **Disclosed**: 2019-01-02T10:47:54.504Z

## Reporter
- **Username**: thefrog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hola amigos,

First off, I know RFCs are annoying.
Second of all, namespace attacks are a b*tch.

With that out of the way, here is an Inti-bug that was discovered as a result of reading RFC2142 very carefully.

## Brief summary of RFC2142

RFC2142 defines a standard set of email addresses that cover certain roles and functions. For example, you might be familiar with the `security@` address. This was originally defined in section 4 of RFC2142: https://tools.ietf.org/html/rfc2142#section-4.

```
MAILBOX        AREA                USAGE
-----------    ----------------    ---------------------------
ABUSE          Customer Relations  Inappropriate public behaviour
NOC            Network Operations  Network infrastructure
SECURITY       Network Security    Security bulletins or queries
```

## Ze Bug

The way the new `@wearehackerone.com` email forwarding system works, is that an address is allocated for your HackerOne account based on your username (`<your-h1-handle>@wearehackerone.com`). So hackerone.com/foobar turns into `foobar@wearehackerone.com`. With this in mind, I decided to enumerate all the various email addresses defined in RFC2142 and determine which ones can be registered ultimately resulting in me controlling what should be a reserved email address.

In some cases you do actually prevent people from claiming the handle, such as with `postmaster`.

███

Unfortunately though, after a bit of probing I noticed that not all RFC2142 addresses were blocked. I am now the proud owner of trouble@wearehackerone.com. Please feel free to shoot me an email and I will respond back to demonstrate that this address is under my control.

## How to fix this issue

In order to fix this issue, I advise you to add the following usernames to your exclusion list so that one cannot hijack these important email addresses.

```
abuse
admin
administrator
hostmaster
info
is
it
list
list-request
majordomo
marketing
mis
news
postmaster
root
sales
security
ssl-admin
ssladmin
ssladministrator
sslwebmaster
support
sysadmin
trouble
usenet
uucp
webmaster
```

Have fun fixing this issue and feel free to email me at trouble@wearehackerone.com if you are having any trouble reproducing this issue. ;)

\- @thefrog

## Impact

In some cases, these reserved addresses are used to generate SSL certificates since CAs assume that these are all trusted addresses.

## Attachments
No attachments
