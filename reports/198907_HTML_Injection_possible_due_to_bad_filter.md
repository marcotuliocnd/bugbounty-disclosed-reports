# HTML Injection possible due to bad filter

## Report Details
- **Report ID**: 198907
- **URL**: https://hackerone.com/reports/198907
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-17T03:11:25.656Z
- **Disclosed**: 2017-02-10T12:01:31.776Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vkcom

## Vulnerability Information
Hello,

I have found an area where it may be possible to run certain HTML/JS scripts.

TO REPRODUCE:
1. Go to documents

2. Upload anything and edit it

3. On the edit page in tags, enter code without a closing bracket ex. <img src=x

4. Click enter

5. It will be parsed in that area, but after saving it, it won't parse.

POTENTIAL:
I'm still looking into this, as this could be a possible XSS vuln if I can find vectors without closing brackets that have harmful code.

WHY IT WORKS:
The reason this works is because your filter only looks for opening AND closing brackets, when it is possible to run code without closing the brackets.

Thanks,
Kicker


## Attachments
No attachments
