# languagechange event fires simultaneously on all tabs

## Report Details
- **Report ID**: 257942
- **URL**: https://hackerone.com/reports/257942
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-08T17:18:57.475Z
- **Disclosed**: 2017-10-19T13:16:55.023Z

## Reporter
- **Username**: tomvg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
The `languagechange` event, which fires when the user modifies the browser's language settings fires simultaneously on all tabs. This would allow an adversary to link multiple visits to a single user: the adversary (e.g. a malicious ad provider) has a script that listens for this event, and when fired sends a signal to the adversary's server which includes the timestamp of the event. Since this is an event that does not occur very often (only when the user changes the browser's language), so the chances that this event occurs at the exact same millisecond on with multiple users is very small.
I believe this has been a small oversight, since the `online` and `offline` events do seem to be disabled because of this threat.

### PoC

As a proof-of-concept, you can open http://192.31.23.250/_events/get-event-values.html and https://poc.tom.vg/events-session-associate/get-event-values.html in different tabs (these are from different origins), select `onlanguagechange` from the dropdown and press the "Start" button. Next, change the language of the browser in the "Content" tab of the preferences (`about:preferences#content`): just add/remove one of change the order. Afterwards you should see an event logged on both tabs with approximately the same timestamp (the value might slightly differ because of the timer resolution).

## Attachments
No attachments
