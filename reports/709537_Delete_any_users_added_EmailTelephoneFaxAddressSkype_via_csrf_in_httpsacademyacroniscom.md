# Delete any user's added Email,Telephone,Fax,Address,Skype via csrf in (https://academy.acronis.com/)

## Report Details
- **Report ID**: 709537
- **URL**: https://hackerone.com/reports/709537
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-08T07:14:42.829Z
- **Disclosed**: 2023-04-25T09:08:21.029Z

## Reporter
- **Username**: imranhudaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi there,

It is possible to delete anyone's added email,telephone,fax,address,Skype via CSRF in `GET`  method. The action is performed via `GET`method without any CSRF protection.

# Steps to reproduce

-   login to your https://academy.acronis.com account
-   navigate to `https://academy.acronis.com/#/account/edit/account_id/<your_id>`
-   add any email,telphone,fax,addres,skype 
-   try deleting them and capture the request 
-   you'll see the request is performed in `GET` method without any CSRF protection

#POC

```
<html>
  <body>
    <form action="https://academy.acronis.com/account/delete-contact/contact_id/<your_id>">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

#Fix 
 Use X-CSRF token or perform the action in `POST` method with a CSRF token.

## Impact

Delete any user's added  email,telephone,fax,address,Skype with CSRF attack.

## Attachments
No attachments
