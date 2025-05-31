# Window.opener bug at www.coinbase.com

## Report Details
- **Report ID**: 181088
- **URL**: https://hackerone.com/reports/181088
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-09T15:39:09.614Z
- **Disclosed**: 2016-11-28T18:17:31.756Z

## Reporter
- **Username**: punkrock
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
**Window.Opener Bug**

**Description:**

When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

**Browsers Verified In:**

  * Mozilla Firefox

**Steps To Reproduce:**

1. Visit https://www.coinbase.com/
2. In Image F133659, If you notice the links go through `https://www.coinbase.com/external_redirect` except "Bloomberg"

3. Since Bloomberg works on `http`, If you're in the same network you can manipulate the bloomberg page and inject a script which manipulates `window.opener`

`window.opener.location.replace("https://www.notcoinbase.com");`

I understand this is very trivial to exploit and does not have very big impact

## Attachments
- Screen_Shot_2016-11-09_at_8.56.52_PM.png
