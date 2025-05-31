# Context isolation bypass via nested unserializable return value

## Report Details
- **Report ID**: 2138080
- **URL**: https://hackerone.com/reports/2138080
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-09-06T16:53:57.205Z
- **Disclosed**: 2023-10-07T19:47:54.905Z

## Reporter
- **Username**: marshallofsound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This issue is exploitable under either of two conditions:

* If an API exposed to the main world via contextBridge can return an object or array that contains a JS object which cannot be serialized, for instance, a canvas rendering context. This would normally result in an exception being thrown `Error: object could not be cloned`.
* If an API exposed to the main world via contextBridge has a return value that throws a user-generated exception while being sent over the bridge, for instance a dynamic getter property on an object that throws an error when being computed.

In both of these cases the context that receives the exception may be able to (via the exception) obtain privileged access to the context on the other side of the bridge.

## Impact

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

## Attachments
No attachments
