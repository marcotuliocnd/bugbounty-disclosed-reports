# Path paths and file disclosure vulnerabilities at influxdb.quality.gitlab.net

## Report Details
- **Report ID**: 1643962
- **URL**: https://hackerone.com/reports/1643962
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-07-20T16:51:33.750Z
- **Disclosed**: 2022-11-04T03:46:18.591Z

## Reporter
- **Username**: otoyyy_h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please note that initial triage is handled by HackerOne staff. They are identified with a `HackerOne triage` badge and will escalate to the GitLab team any. Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

Path paths and file disclosure vulnerabilities at influxdb.quality.gitlab.net

Hi, I discovered a file disclosure vulnerability within the influxdb.quality.gitlab.net domain This allows attackers to only get arbitrary files from remote servers. Where the file stack trace can be viewed without authentication. A heap file is an unordered set of records, stored on a set of pages. This class provides basic support for inserting, selecting, updating, and deleting records. Temporary heap files are used for external sorting and in other relational operators. A sequential scan of a heap file (via the Scan class) is the most basic access method.

### Steps to reproduce
Vulnerability endpoint:
```
1. https://influxdb.quality.gitlab.net/debug/pprof
2. https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1
3. https://influxdb.quality.gitlab.net/debug/pprof/heap
4. https://influxdb.quality.gitlab.net/debug/pprof/trace
5. https://influxdb.quality.gitlab.net/metrics/
6. https://influxdb.quality.gitlab.net/stats.json
```

## Impact

allows an attacker to read arbitrary files on the server that is running an application. This might include application code and data, credentials for back-end systems, and sensitive operating system files. In some cases, an attacker might be able to write to arbitrary files on the server, allowing them to modify application data or behavior, and ultimately take full control of the server.

## Attachments
- heap
- trace
