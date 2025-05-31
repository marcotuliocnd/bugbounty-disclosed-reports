# Null pointer dereference regression in parse.y

## Report Details
- **Report ID**: 185387
- **URL**: https://hackerone.com/reports/185387
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-26T05:04:27.125Z
- **Disclosed**: 2016-12-17T20:09:00.506Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
Hi,

Just pulled the latest mruby code, and found that some of my fuzzing test cases now crash. Bisected it to commit `227daa881137d5251e03eea0883b9b574a1f064e`. Reverting this change no longer causes a crash.

The minimised file causing the crash is:

```
f ()
```

Also affects mruby-engine.

Cheers,

Hugh

## Attachments
No attachments
