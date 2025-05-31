# Exposed Cortex API at https://cortex-ingest.shopifycloud.com/

## Report Details
- **Report ID**: 1258871
- **URL**: https://hackerone.com/reports/1258871
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-12T22:00:58.999Z
- **Disclosed**: 2022-12-02T22:25:03.258Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi there, to be honest this is the first time I have seen this type of asset, but I think it is interesting/not supposed to be exposed. There is a Cortex metrics server running without authentication on https://cortex-ingest.shopifycloud.com/. This allows us to see the config for the server, call various Cortex APIs, and also exposes a Golang pprof debugger where we can see all the command-line arguments and DoS the server.

Example URLs:
* Cortex home: https://cortex-ingest.shopifycloud.com/
* Cortex config: https://cortex-ingest.shopifycloud.com/config
* Golang pprof home: https://cortex-ingest.shopifycloud.com/debug/pprof/
* Golang pprof cmdline: https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1

I see that the Cortex API offers many endpoints, some of which work and some of which do not: https://cortexmetrics.io/docs/api/#endpoints. I will take a look and see what impact I can find there.

## Impact

Information disclosure, no authentication

## Attachments
No attachments
