# Improper parsing of input could lead to future XSS vulnerabilities in Sequences

## Report Details
- **Report ID**: 243138
- **URL**: https://hackerone.com/reports/243138
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-26T06:25:17.755Z
- **Disclosed**: 2017-06-27T19:04:20.126Z

## Reporter
- **Username**: joshualaurencio
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hello,
I understand this probably doesn't qualify as a vulnerability, but I  figured it would be important to bring to your attention regardless. I ask that if you are to close this, you mark it as informative for the sake of signal, reputation, etc. as I mean no harm with this post, and simply wish to inform you of an incorrect handling of data (that definitely classifies as a bug) but might not necessarily be classified as a vulnerability.

URL: https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR

As you can see from, the first screenshot, if this input is entered into the search, the input bar actually only displays the first part, the letter 'a' and the 'POSSIBLEVECTOR' string is truncated. This is because the input is placed into the HTML without quotes, and therefore, chrome automatically places quotes around the first part of the string, 'a', and the next part is parsed as raw HTML.

A good example of this is with the following query.

URL: https://app.mixmax.com/dashboard/sequences?q=a+readonly

Since "readonly" is interpreted as part of the HTML, it disables changing the input box via the browser.

As I said earlier, this is not in itself a vulnerability, as you guys seem to do a pretty good job of sanitizing the input (=, <, >) are all filtered out. But either way, having this the way it is now can be dangerous for the future.


## Attachments
- 2.png
- 1.png
