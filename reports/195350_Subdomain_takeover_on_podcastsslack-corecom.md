# Subdomain takeover on podcasts.slack-core.com

## Report Details
- **Report ID**: 195350
- **URL**: https://hackerone.com/reports/195350
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-02T19:10:40.111Z
- **Disclosed**: 2017-01-04T21:01:06.238Z

## Reporter
- **Username**: michiel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
I noticed `slack-core.com` is used for Slack's call infrastructure. I had never seen that domain before, so I decided to find out what else was running on it. It turned out `podcasts.slack-core.com` was pointing to a Podcast and RSS hosting service called Feed.Press. However, there was no Feed.Press account associated with `podcasts.slack-core.com`, which allowed me to register it and start serving my content from this domain. 

Note that since it is not on Slack's root domain, the impact of this vulnerability seems pretty minimal.

# Proof of Concept
Here we can see `podcasts.slack-core.com` is CNAME'd to `redirect.feedpress.me`:

```plain
michiel@msp ~ $ dig podcasts.slack-core.com                                                                                         [2.1.9]

; <<>> DiG 9.10.3-P4-Ubuntu <<>> podcasts.slack-core.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1307
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;podcasts.slack-core.com.	IN	A

;; ANSWER SECTION:
podcasts.slack-core.com. 299	IN	CNAME	redirect.feedpress.me.
redirect.feedpress.me.	3599	IN	A	5.135.16.40

;; Query time: 253 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Jan 02 14:02:07 EST 2017
;; MSG SIZE  rcvd: 103
```

By creating my own account on [Feed.Press](https://feed.press), I was able to register `podcasts.slack-core.com` as my "custom domain" under my Feed.Press account. After it propagated through Feed.Press' systems, I was able to fully control the contents served as http://podcasts.slack-core.com.

Since the domain was dormant, I decided to redirect `/` to https://hackerone.com as a proof of concept. We can see that happening using this `curl` command (note the `Location` header):

```plain
michiel@msp ~ $ curl -vv http://podcasts.slack-core.com
* Rebuilt URL to: http://podcasts.slack-core.com/
*   Trying 5.135.16.40...
* Connected to podcasts.slack-core.com (5.135.16.40) port 80 (#0)
> GET / HTTP/1.1
> Host: podcasts.slack-core.com
> User-Agent: curl/7.47.0
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
< Server: nginx
< Date: Mon, 02 Jan 2017 19:06:18 GMT
< Content-Type: text/html
< Content-Length: 178
< Location: https://hackerone.com
< X-Backend-Server: 172.16.0.53
<
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx</center>
</body>
</html>
* Connection #0 to host podcasts.slack-core.com left intact
```

# Remediation
Since the domain is not used anymore, it is recommended to remove the CNAME of `podcasts.slack-core.com` to `redirect.feedpress.me`. 

If you need me to release the domain in Feed.Press itself, let me know and I'll remove it from my account.

## Attachments
No attachments
