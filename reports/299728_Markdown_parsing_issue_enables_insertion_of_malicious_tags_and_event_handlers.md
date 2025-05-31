# Markdown parsing issue enables insertion of malicious tags and event handlers

## Report Details
- **Report ID**: 299728
- **URL**: https://hackerone.com/reports/299728
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-20T22:09:47.391Z
- **Disclosed**: 2018-01-29T16:37:43.067Z

## Reporter
- **Username**: dr_dragon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
When markdown is being presented as HTML, there seems to be a strange interaction between _ and @ that lets an attacker insert malicious tags.

# Proof of Concept :
```
</http:<marquee>hello
```

is rendered converted to the following HTML:

```
<p><a title="/http:<marquee" href="/http:%3Cmarquee" target="_blank">/http:<marquee>hello</p>
</marquee></a></p>
```
As you can see, the output includes a </http:<marquee tag that I can add arbitrary attributes (including event handlers).

## Impact

When markdown is being presented as HTML, there seems to be a strange interaction between _ and @ that lets an attacker insert malicious tags.

## Attachments
No attachments
