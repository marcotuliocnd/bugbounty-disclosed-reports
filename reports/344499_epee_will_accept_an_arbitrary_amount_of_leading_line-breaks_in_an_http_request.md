# epee will accept an arbitrary amount of leading line-breaks in an http request

## Report Details
- **Report ID**: 344499
- **URL**: https://hackerone.com/reports/344499
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-30T02:43:31.994Z
- **Disclosed**: 2018-08-02T00:24:46.989Z

## Reporter
- **Username**: ahook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:**
In the epee http protocol handler, as it reads a new request, it first attempts to ignore any leading carriage-returns and line-feeds. It does not have a mechanism to give up if an inordinate number of CrLfs are encountered.

**Description:**
The pertinent block of code is here:
https://github.com/monero-project/monero/blob/master/contrib/epee/include/net/http_protocol_handler.inl#L256

It loops through the data in the request. Before parsing anything of significance, it throws away any leading CrLfs by doing an erase from the from the front of the cache (which itself is expensive as it is a simple string as opposed to a string_view). An attacker could send an arbitrary number of CrLfs to any server with an exposed http port and cause the http server's handler thread to spin forever adding and removing the CrLfs from the cache.

## Releases Affected:

All releases running the epee http framework.

## Steps To Reproduce:

Can simply telnet to a running monero node's http port and send as many carriage-returns and line-feeds and you'd like. The server will remain responsive until additional, non-CrLf data is sent over the connection.

## Impact

An attacker could open multiple such connections across many nodes and tie up the http server threads and cause it to spin indefinitely, wasting resources, and preventing legitimate connections.

## Attachments
No attachments
