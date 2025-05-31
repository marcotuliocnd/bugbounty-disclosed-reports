# Blacklist bypass on Callback URLs

## Report Details
- **Report ID**: 53004
- **URL**: https://hackerone.com/reports/53004
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-03-22T16:26:22.320Z
- **Disclosed**: 2016-09-14T20:38:56.447Z

## Reporter
- **Username**: agarri_fr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
In bug [#47368](https://hackerone.com/reports/47368), I was able to reach private IP addresses via the "Test Now" button of the "Callback URL" feature. Exploiting this flaw allowed me to reach the metadata server of your outbound proxy (which is, afaik, maintained by Proximo). A [comment](https://hackerone.com/reports/47368#activity-329823) by **aianus**  states that callbacks are now restricted *"from hitting any RFC 6890 IP addresses and networks"*. This security measure can be bypassed used DNS rebinding.

 Let's consider what happens where an URL like http://test42.sqli.nicob.net/_hostmanager/healthcheck is submitted via the "Merchants settings":
1) The hostname "test42.sqli.nicob.net" is resolved (twice) by your servers. Then the resulting IP address is checked against a blacklist. If the IP is blacklisted, the message "Invalid callback URL" is printed and processing stops
2) If the IP isn't blacklisted, the request is sent to the outbound proxy managed by Proximo. The proxy will resolve "test42.sqli.nicob.net" too, without applying a strict blacklist. Then the target URL is accessed.

In order to exploit the flaw, we need a custom DNS server. A patched copy of [dnschef](https://thesprawl.org/projects/dnschef/) can be used to send different answers at different times and bypass the filter. The following command will instruct the DNS server to answer with IP #2 twice (an authorized one), then IP #1 (a blacklisted one), then back to the beginning (scheme "221").

```
 # ./rebind.py --ip1=127.0.0.1 --ip2=92.243.29.213 --scheme=221
[17:05:08] 54.144.123.243: cooking the response of type 'A' for test42.sqli.nicob.net to 92.243.29.213 [1]
[17:05:08] 54.82.64.0: cooking the response of type 'A' for test42.sqli.nicob.net to 92.243.29.213 [2]
[17:05:09] 54.162.118.12: cooking the response of type 'A' for test42.sqli.nicob.net to 127.0.0.1 [3]
```

The filters will see "92.243.29.213" and the proxy will see "127.0.0.1". And the Web interface will display the index page of the Web service listening on port TCP/80 of the loopback interface of the proxy server. Several ports were identified on loopback (80, 1080, 8000, 9177, ...)  and I found some unprotected URL like http://127.0.0.1:80/_hostmanager/healthcheck (which simply displays "OK").

Regarding exploitation:
- the metadata server on 169.254.169.254 is unreachable (that's good for you!)
- the pages found (:9177/status, :80/_hostmanager/healthcheck, :80/check, ...) are unproctected but not sensitive
- I may have missed some URL or web servers listening on loopback (brute-force is hard because of rate limitations)

Advice: the outbound proxy should implement a blacklist restricting access to internal and private IP addresses

NB: this kind of DNS blacklist may be 1) used elsewhere by Coinbase2) exploited more easily in a different scenario

## Attachments
No attachments
