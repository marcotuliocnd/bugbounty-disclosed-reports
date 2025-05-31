# Hackers can reveal the names of private programs that have an external link

## Report Details
- **Report ID**: 1127455
- **URL**: https://hackerone.com/reports/1127455
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-17T10:01:31.850Z
- **Disclosed**: 2021-08-24T03:20:25.898Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hi team,

Our team has found a way to distinguish between private programs with external links. Due to the ability to select Severity Rating Options, the program can set two options : `Rating or CVSS Score` and `CVSS Score Only`. One of them removes the possibility of setting the severity(directly). Since no one can do this in sandbox programs, and both options are set by default, this difference allows us to understand that the changes were made by the program administrator. This means that the program has control, and therefore a private part

 

## Steps To Reproduce:

1. Create new account( Ideally)
2. Go to https://hackerone.com/hacktivity/publish
3. Input Program - :handle: external program
4. Other fields - **test** and click create report
5. After, You need to click on the severity button 

{F1233314}
6. Looking at a possible variation of the severity setting

7. If we have only one option, then the program has a private part
{F1233318}
 

## Recommendation:

We believe that at the end of the check, for the `severity_options` attribute, we need to create a check for whether the report belongs to the `is_published` attribute, and if it is set to `true`, then always set `severity_options` to the `rating_and_cvss` value

## Impact

Hackers can reveal the names of private programs that have an external link

## Attachments
- button_severity.png
- CVSS_Score_Only.png
