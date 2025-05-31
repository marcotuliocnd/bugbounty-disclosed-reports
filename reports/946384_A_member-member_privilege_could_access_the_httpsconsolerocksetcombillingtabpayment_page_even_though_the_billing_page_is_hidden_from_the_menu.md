# A member-member privilege could access the https://console.rockset.com/billing?tab=payment page even though the billing page is hidden from the menu. 

## Report Details
- **Report ID**: 946384
- **URL**: https://hackerone.com/reports/946384
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-29T09:36:10.432Z
- **Disclosed**: 2021-11-09T21:15:19.277Z

## Reporter
- **Username**: jhimansh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockset

## Vulnerability Information
## Summary: I am writing to submit a vulnerability found at https://console.rockset.com/. I created an admin account with email himanshujoshitest2018@gmail.com and added a member with email himanshujoshitest2019@gmail.com. I logged in from the member's account and realized that the Billing page is not visible in the menu, it is hidden as per the designed privileges of a member however when I visited https://console.rockset.com/billing?tab=payment page, it did open and I could view beyond a member's privilege. I am attaching screenshots which shows two users, one is an admin and other is a member and the member is able to view the add payment method page and other information. The billing page is kept hidden from the menu but if I directly open the billing URL, i can view the page instead of it being forbidden. 

## Steps To Reproduce:
1. Invite a member with member privileges. 
2. Login at console.rocket.com using member email address.
3. You will see that the billing page is not available in the menu.
4. Directly open https://console.rockset.com/billing?tab=payment page and it will be opened from the member's account however it is hidden from the menu. The access to this page is not yet forbidden. 

Attaching screenshots for your reference. There is one screenshot of admin's page and two screenshots of member's page in which the member has opened the billing page. 

Remediation:
Check the access-control while an URL is opened. 

Thanks!

## Impact

The impact here is medium however this is a access control issue and needs fixing. The billing information is not to be accessed by a someone with a member privilege and therefore the billing page is hidden from the menu however the member can still access the information which is not meant from a member.

## Attachments
- admin-UsersPage.png
- member-card_details_page.png
- member-page.png
