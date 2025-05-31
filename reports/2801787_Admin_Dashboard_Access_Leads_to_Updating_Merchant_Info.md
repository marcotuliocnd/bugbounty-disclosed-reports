# Admin Dashboard Access Leads to Updating Merchant Info

## Report Details
- **Report ID**: 2801787
- **URL**: https://hackerone.com/reports/2801787
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-10-24T16:17:34.689Z
- **Disclosed**: 2025-03-02T13:53:28.628Z

## Reporter
- **Username**: tinopreter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
The ███████ application provides access to 3(Merchant, Supervisor, Admin) classes of users. Looking at the Admin side, its clear only permitted admins can login to the portal since nothing on the UI indicates a register feature. However I was able to find a registration endpoint to sign up. Now I have access to the Admin dashboard. Based on the functionalities there, it's evident an outsider shouldn't have access to this.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Visit ████████ and signup
  2. Login at ██████ and you will be redirected to the admin dashboard where you can approve or decline transactions.
{F3704827}   
  3. At ███████, you can see a list of registered Merchant accounts in the application.    
{F3704841}  

  You can edit their data, 
`Change their account credentials`
`change their account number to an attacker's: thereby 
  receiving payments made to them`,  
`disable` or `delete` their account, etc.  
{F3704837}    
{F3704907}

##!EDIT

Initially my report focused on the merchants, however it affects, Cashiers, Stations and Supervisors also. You can edit and delete their data also by navigating the the URLs below:  

███████
█████████
█████████   

#IMPORTANT
You can see the passcode for various supervisor accounts at
███   
{F3704923}

## Impact

Direct access to admin functionalities, where an attacker can modify merchant financial account information, disable and delete account of MTN clients. An outsider like myself shouldn't have access to this.

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
