# Potential pre-auth RCE on Twitter VPN

## Report Details
- **Report ID**: 591295
- **URL**: https://hackerone.com/reports/591295
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-05-28T07:53:44.155Z
- **Disclosed**: 2019-08-10T15:06:45.375Z

## Reporter
- **Username**: orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi, we(Orange Tsai and Meh Chang) are the security research team from DEVCORE. Recently, we are doing a research about SSL VPN security, and found several critical vulnerabilities on Pulse Secure SSL VPN! We have reported to vendor and [patches](https://kb.pulsesecure.net/articles/Pulse_Security_Advisories/SA44101) have been released on `2019/4/25`. Since that, we keep monitoring numerous large corporations using Pulse Secure and we noticed that Twitter haven't patched the SSL VPN server over one month!

These vulnerabilities include a pre-auth file reading(CVSS 10) and a post-auth(admin) command injection(CVSS 8.0) which can be chained into a pre-auth RCE! Here are all vulnerabilities we found:

* CVE-2019-11510 - Pre-auth Arbitrary File Reading
* CVE-2019-11542 - Post-auth Stack Buffer Overflow
* CVE-2019-11539 - Post-auth Command Injection
* CVE-2019-11538 - Post-auth Arbitrary File Reading
* CVE-2019-11508 - Post-auth Arbitrary File Writing
* CVE-2019-11540 - Post-auth Session Hijacking


## Our Steps

First, we download following files with CVE-2019-11510:
1. `/etc/passwd`
2. `/etc/hosts`
3. `/data/runtime/mtmp/system`
4. `/data/runtime/mtmp/lmdb/dataa/data.mdb`
5. `/data/runtime/mtmp/lmdb/dataa/lock.mdb`
6. `/data/runtime/mtmp/lmdb/randomVal/data.mdb`
7. `/data/runtime/mtmp/lmdb/randomVal/lock.mdb`

██████████


The VPN user and hashed passwords are stored in the file `mtmp/system`. However, Pulse Secure caches the plain-text password in the `dataa/data.mdb` once the user log-in. Here, we just grep part of username/plain-text-password for proofs and further actions.

*P.S. we mask the password field for security concerns, and we can send to you if you provide your PGP key.*

```
█████████ / ████
█████████ / ██████
█████ / █████████
██████████ / █████████
███ / ██████
```

Once we log into the SSL VPN, we found the server has enabled the Two-Factor Authentication. Here, we listed two methods to bypass the 2FA:

████

1. We observed Twitter using the 2FA solution from Duo.com. With the file `mtmp/system`, we could obtain the integration key, secret key, and API hostname, which should be protected carefully according to the [Duo documentation](https://duo.com/docs/pulseconnect):

    > Treat your secret key like a password
    The security of your Duo application is tied to the security of your secret key (skey). Secure it as you would any sensitive credential. Don't share it with unauthorized individuals or email it to anyone under any circumstances!

    ```
    # secret-key = ██████████
    ████
    dc=███,dc=duosecurity,dc=com
    cn=<USER>

    # LDAP password = ██████████
    ██████████
    █████
    ███████
    uid=<username>
    ```

2. The Pulse Secure stores the user session in the `randomVal/data.mdb`. Without `Roaming Session` option enabled, we can reuse the session and log into your SSL VPN!

██████████



The next, in order to trigger the command injection(CVE-2019-11542). We leverage the web proxy function to access the admin interface with following URL:

```
https://0/admin/
```

████████

We are now trying to crack the admin hash by GPU. It seems takes a long time, but once we cracked, we can achieve RCE absolutely. Actually, we can simply wait for the admin login and obtain the plain-text password directly!
```
███████
███████
```

Anyway, we decided to report to you first, because it's lethal and critical. If you want, we can provide the RCE PoC in admin interface in order to proof the potential risk!


## Impact:

1. Access Intranet(we have accessed the `███████` for proof) ██████████
2. Plenty of staff plain-text passwords
3. Internal server and passwords(such as the LDAP)
4. Attack back all VPN clients(we will detail the step in [Black Hat USA 2019](https://www.blackhat.com/us-19/briefings/schedule/#infiltrating-corporate-intranet-like-nsa---pre-auth-rce-on-leading-ssl-vpns-15545))
5. Private keys
6. Sensitive cookies in Web VPN(such as okta, salesforce, box.com and google)

## Supporting Material/References:

We attached screenshots to proof our actions. For security concern, we didn't attach the `mtmp/system` and the `dataa/data.mdb`. If you want, we can send to you with your PGP key encrypted!

## Recommend Solution

The only and simplest way to solve this problem is to upgrade your SSL VPN to the [latest version](https://kb.pulsesecure.net/articles/Pulse_Security_Advisories/SA44101)!

## Impact

1. Access Intranet(we have accessed the `████████` for proof) ████
2. Plenty of staff plain-text passwords
3. Internal server and passwords(such as the LDAP)
4. Attack back all VPN clients(we will detail the step in [Black Hat USA 2019](https://www.blackhat.com/us-19/briefings/schedule/#infiltrating-corporate-intranet-like-nsa---pre-auth-rce-on-leading-ssl-vpns-15545))
5. Private keys
6. Sensitive cookies in Web VPN(such as okta, salesforce, box.com and google)

## Attachments
No attachments
