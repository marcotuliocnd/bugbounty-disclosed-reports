# Unrestricted file upload leads to stored xss on https://████████/

## Report Details
- **Report ID**: 854445
- **URL**: https://hackerone.com/reports/854445
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-20T18:36:42.403Z
- **Disclosed**: 2020-05-27T14:24:10.310Z

## Reporter
- **Username**: sensoyard
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

When the user want to upload a "certificate", the web app doesn't check the content-type of the file. A user can upload any kind of file (binary,html,...)

## Step-by-step Reproduction Instructions

1. Create an account at https://██████/████████/app/registration/basic-info

2. When you are connected, click on "certification"

Upload this file as xss.html and save the modifications: 

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Test</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
  </head>
  <body>
    <script>
	alert(document.cookie	)
	</script>
  </body>
</html>
```
3 . Go back to the "certification tab " and open the attachement in a new tab

POC :https://███/████/registration-service/files/███████.html

## Suggested Mitigation/Remediation Actions
Restrict the content-type of the uploaded files

## Impact

The unrestricted file upload vulnerability leads to stored xss.

## Attachments
No attachments
