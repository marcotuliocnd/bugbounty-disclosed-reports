# [featurebook] Specification Server Directory Traversal via Crafted Browser Request

## Report Details
- **Report ID**: 296305
- **URL**: https://hackerone.com/reports/296305
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-08T17:26:43.462Z
- **Disclosed**: 2018-01-10T20:43:30.095Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

A crafted request can be leveraged to traverse the directory structure of a host using the `featurebook` server package, and request arbitrary files outside of the specified web root.

## Module specification
* **Name**: [featurebook](https://www.npmjs.com/package/featurebook)
* **Version**: 0.0.32 (latest release build)

## Verified conditions
* **Test server:** Ubuntu 16.04 LTS

## Proof of concept

Please globally install the `featurebook` package and `cd` to a chosen directory (in this case, `/root`) on your test server. Run `featurebook serve --port 8081` to start serving from this location.

Substituting the `<server-IP>` value as appropriate, please browse to the following URL in Chrome. This will request the target `/etc/passwd` file and echo it line-by-line into an error message:

```
http://<server-IP>:8081/#/viewer/..%2f..%2fetc/passwd
```

{F245294}

Thanks,

Yasin

## Impact

An adversary can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system configuration data.

## Attachments
- featurebook_dirtraversal.png
