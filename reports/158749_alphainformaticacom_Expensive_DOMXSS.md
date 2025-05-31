# [alpha.informatica.com] Expensive DOMXSS

## Report Details
- **Report ID**: 158749
- **URL**: https://hackerone.com/reports/158749
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-08-12T08:58:13.076Z
- **Disclosed**: 2017-07-08T09:25:26.095Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi again,

The page at https://alpha.informatica.com/assessmentBase/assessment.html contains the following JavaScript:

<script>
    var baseHeaderElement = '<base href="'+ window.location.pathname + '" />';
    $('head').append(baseHeaderElement);
</script>

An attacker can exploit this using a protocol-relative URL. In Chrome, open the following URL and either proxy though Burp or look at the network tab in the dev console: https://alpha.informatica.com//assessmentBase/assessment.html

You will see a failed GET request to https://assessmentbase/etc/designs/informatica-com/assessmentform/js/angular.min.js

A sufficiently rich attacker can register assessementbase, and make it serve malicious JavaScript, turning this into a reflected XSS vulnerability.

This issue was passively identified by burp suite's code analysis engine.


## Attachments
No attachments
