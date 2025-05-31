# XSS via Client Side Template Injection on www.███/News/Speeches

## Report Details
- **Report ID**: 1736317
- **URL**: https://hackerone.com/reports/1736317
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-15T18:30:44.042Z
- **Disclosed**: 2023-01-06T18:47:59.553Z

## Reporter
- **Username**: chef_shell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Dear DoD - Team,
I am able to execute javascript code on www.███████/News/Speeches.

This endpoint has a search functionality with the parameter `Search`. The supplied value to this parameter gets embedded into the website.
Furthermore the frontend of the website is presumably created with a template engine. These engines handle user supplied data within double curly braces `{{...}}` for example. If the user input is not sanitized corretly template injection can occur.

When supplying the `Search` parameter with a value inside double curly braces it gets evaluated and the result is then embedded into the web page.

For example the search value `www.███████/News/Speeches?Search={{7*7}}` gets evaluated to `49` and put into the web page (see image_1.png).
Besides simple mathematical equations, javascript code can be put inside those braces too (see image_2.png). This will execute the code as well which results in a XSS vulnerability.

There are some mitigations to this. For example some methods are blacklisted which means alert(1) is not allowed. However this can be bypassed by encoding the payload into a base64 string and call a decode method before evaluating (executing) the code.

I've come up with a simple payload which triggers all javascript code thus bypassing the blacklisting of potential dangerous methods.

`https://www.████/News/Speeches/?Search={{window['eval'](window['atob'](window['decodeURIComponent']('BASE_64_ENCODED_PAYLOAD')))}}`

A poc video is attached.

## Recap

A client side template injection vulnerability is present through the `Search` parameter. This leads to the ability to run arbitrary javascript code on the client side.

## Impact

- run arbitrary javascript code on the victims machine
- Since the javascript code is run within the realm of ██████ CORS bypass on other endpoints could be possible.
- Forgery of information

## System Host(s)
www.█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
- Copy the provided link in the description section
- Replace the `BASE_64_ENCODED_PAYLOAD` with an actual base64 encoded javascript code. For Example `YWxlcnQoMSk=` which is `alert(1)` in base64.
 - Insert the crafted url into the browser.
- done

## Suggested Mitigation/Remediation Actions
Sanitize the user input so double curly braces `{{...}}` won't trigger a client side server injection



## Attachments
No attachments
