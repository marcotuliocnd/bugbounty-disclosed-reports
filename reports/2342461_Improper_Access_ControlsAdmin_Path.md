# Improper Access Controls(Admin Path)

## Report Details
- **Report ID**: 2342461
- **URL**: https://hackerone.com/reports/2342461
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-02-01T12:00:29.598Z
- **Disclosed**: 2025-01-31T11:10:22.131Z

## Reporter
- **Username**: aliyueka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Go to https://nin.mtn.ng/ then click on "Check your NIN Link Status" then right click and click on "Inpect" and admin path is display at  web browser ../wp-admin/admin-ajax.html

## Steps To Reproduce:
STEP 1:
Go to https://nin.mtn.ng/
{F3021640}

STEP 2:
Click on "Check your NIN Link Status" 
{F3021641}

STEP 3:
Right click at the top of the page(On MTN Yellow Bar) and  then click on "Inspect"
{F3021642}
../wp-admin/admin-ajax.html
Admin Path

## Impact

1.) View Sensitive Information
2.) Steal Customers details
3.) Install backdoor
4.) Access different Components
5.) Alter System

## Attachments
- Nin.PNG
- Nin2.PNG
- Nin3.PNG
