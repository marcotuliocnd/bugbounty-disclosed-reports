# curl "globbing" can lead to denial of service attacks

## Report Details
- **Report ID**: 1572120
- **URL**: https://hackerone.com/reports/1572120
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-16T15:19:36.897Z
- **Disclosed**: 2022-06-16T15:14:32.454Z

## Reporter
- **Username**: iylz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

The curl "globbing" allows too much scope, which can cause the server to be denied service or used to attack third-party websites. The globbing allow [1-9999999999999999999] to parse in the url. So when curl request for 'http://127.0.0.1/[1-9999999999999999999]', the can cause 300 requests in the server.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Listen 8000 port: python -m SimpleHTTPServer 8000
  2.  command: nohup ./curl -vv 'http://127.0.0.1:8000/[1-9999999999999999999]/' &
  3. Check the server resource process. There are a lot of network requests and CPU consumption. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

With this function, the resources of the server running curl request can be excessively consumed or a large number of URL accesses to other websites can be initiated, resulting in denial of service.

## Attachments
- 1.png
