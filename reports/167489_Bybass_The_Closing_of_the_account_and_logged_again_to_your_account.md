# Bybass The Closing of the account and logged again to your account

## Report Details
- **Report ID**: 167489
- **URL**: https://hackerone.com/reports/167489
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-11T01:31:25.100Z
- **Disclosed**: 2016-10-21T09:24:37.813Z

## Reporter
- **Username**: need_new_username_103
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello
### Details:
All My accounts have been closed i dnot know the reason so i have played around and manged to bypass this mechanism using the last unused password token  

### Steps:
-  go to forget password page and get new password reset token and dnot use it 
-  go  and make anything against the rules lead to close your account [ I dnot know what make it close :D]
- go to your email and using the reset password email you will go to the change password page 
- Enter the new password two times you will get in in your profile
- You can edit your privacy and password ,info but when you try to enter your email page the server will respond with 500 internal error 
- if you try to write review the server will respond with 500 internal server error 
- if you try to edit your profile will respond with 500 server error 


### Fix:
- when you close the account make sure you expire all reset token associted with it

### closed_account_used in test:
````
███
````

## the closed_accounts:
````
████,████████
██████
````
 I hope you open it again 

Thanks

## Attachments
- 500_internal_servar_error.png
- account_view.png
