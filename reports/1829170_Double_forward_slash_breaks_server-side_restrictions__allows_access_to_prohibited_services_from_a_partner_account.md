# Double forward slash breaks server-side restrictions & allows access to prohibited services from a partner account

## Report Details
- **Report ID**: 1829170
- **URL**: https://hackerone.com/reports/1829170
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-01-10T15:37:19.887Z
- **Disclosed**: 2023-02-10T11:06:58.384Z

## Reporter
- **Username**: ashwarya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
Hi Team,

There appears to be a weird bug here. Making an API call to the prohibited endpoint appended with double/multiple slash is breaking some server-side restrictions imposed upon a partner account.

**Example** - In the present scenario, Autorebates facility is unavailable to the partners from India. When a direct request is made to the autorebates API endpoint, the application throws `HTTP/2 403 Forbidden`. However, when the similar request is made with double forward slash appended at the beginning, the application successfully processes the request. This effectively gives unrestricted access to the Autorebates facility which otherwise is strictly not available to a partner account from India.


#Steps to Reproduce

The below sample request (appended with double forward slash) attempts to create a client group with set rebate percentage under a partner account which do not have access to the autorebates facility. All requests appended with double forward slash breaks the server-side restriction and easily go through from a partner account with no access to the Autorebates facility.

```
POST //api/v2/autorebates/groups/ HTTP/2
Host: my.exnesstrade.pro
Content-Type: application/json
Authorization: JWT xyz

{
"group_title":"Test"
}
```
#Proof of Concept
███

███

███

## Impact

Making an API call with double/multiple forward slashes breaks the server-side restrictions imposed upon a partner account and allows a partner to have unrestricted access to the autorebates facility.

## Attachments
No attachments
