# unpermitted user can change the device name of admin account

## Report Details
- **Report ID**: 865115
- **URL**: https://hackerone.com/reports/865115
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-03T06:50:04.504Z
- **Disclosed**: 2020-06-16T14:41:17.183Z

## Reporter
- **Username**: error___404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
Invited user with only the read-only permission can change the device name in admin account

1.create two account 'A 'and 'B ' in  console.helium
2.Invited the account 'B' with 'A' by giving the read-only permission
3.In account 'B' trying to delete the organization created by admin account 'A' and intercept the request then you got the organization id in request
4.Then in account 'B' add the device name and click on it and update the name which you want to display in the admin account(victim account)
5.And intercept the request while clicking the update button
6.In the request add the organization id which you got in step 3
7.then forward the request then the device name in admin account will be changed

## Impact

attacker with only the read-only permission can change the device name in the admin account

## Attachments
- helium_poc_.mp4
