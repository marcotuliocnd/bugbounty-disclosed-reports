# Enrolling to a CA that returns an empty response crashes the node process

## Report Details
- **Report ID**: 506412
- **URL**: https://hackerone.com/reports/506412
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-07T20:23:54.652Z
- **Disclosed**: 2022-08-06T17:37:09.974Z

## Reporter
- **Username**: mttrbrts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
If a CA server responds with an empty response during enrollment, an exception is thrown in the event emitter on `end`. This is an uncaughtException and causes the containing node process to exit.

# To replicate:
With the attached files, run:
```
npm install
node badCa.js &
node index.js
```

This starts a simple malicious CA server that provides a response that triggers the exception. The `index.js` script tries 2 different scenarios:
- 1. With a known bad URL, which throws an exception which can be caught by the client application
- 2. With a malicious CA, which throws an exception which cannot be caught by the client application because of the EventEmitted behaviour in node.

> From https://nodejs.org/api/events.html#events_error_events
> If an EventEmitter does not have at least one listener registered for the 'error' event, and an 'error' event is emitted, the error is thrown, a stack trace is printed, and the Node.js process exits.

# Fix

Replace https://github.com/hyperledger/fabric-sdk-node/blob/c10865cfb20d063fdef4c7d96c25c1581f309e84/fabric-ca-client/lib/FabricCAClient.js#L457
`util.format('Enrollment failed with HTTP status code', JSON.parse(data).statusCode)));`
with 
`util.format('Enrollment failed with HTTP status code', response.statusCode)));`

The same issue is present at https://github.com/hyperledger/fabric-sdk-node/blob/0d24cec10f7a3e0153fcf3f0158a89c5eaa0cfab/fabric-ca-client/lib/FabricCAClient.js#L318

## Impact

This attack allows an attacker to cause any node client application using the fabric-ca-node SDK to exit. In scenarios where the SDK is used in a server-side application, this will have the effect of denying the use of that server to other users.

## Attachments
- badCa.js
- index.js
- package.json
