# A team member of the program with Report rights can ban the Admin

## Report Details
- **Report ID**: 816143
- **URL**: https://hackerone.com/reports/816143
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-10T17:49:55.074Z
- **Disclosed**: 2020-05-15T17:22:21.766Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Our team has conducted a number of studies (tests) in the field of permission `Report`. We noticed that a team member of the program with such permission can ban a member with `Admin` rights

## Steps To Reproduce:
1) Admin submit new report in program
2) A team member with Report rights can use the 'Ban reporters ' panel via their report

my group - `one_permission` have permission `Report`

{F743466}
█████

3) After `ban` , admin can't create new report in program (it's not logical)

{F743464}

## Impact

Ban the Admin in program

## Attachments
- cant_create_new_report.png
- Ban_admin.png
