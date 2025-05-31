# Leaked DB credentials on https://██████████.mil/███

## Report Details
- **Report ID**: 761790
- **URL**: https://hackerone.com/reports/761790
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-12-19T16:19:47.238Z
- **Disclosed**: 2020-12-03T21:32:20.836Z

## Reporter
- **Username**: al-madjus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Information disclosure with login credentials for ms-sql database exposed. 

**Description:**
I've found a PHP info file disclosed on https://█████.mil/██████ containing login credentials for a database cloud server (███████) as well as information on the host system such as hostname, username and full paths. The database server is up, but I have not tried connecting to it with the credentials, as I feel that would be going too far. 

## Impact
Possible access to database as well as disclosure of sensitive host information. 

## Step-by-step Reproduction Instructions

1. Go to https://██████████.mil/████████
2. Search for 'password', you should see this: 
    `Data Source=tcp:███,█████████;Initial Catalog=██████████;User  Id=████@██████████;Password=███████ `
3. Run `nc -vvv █████████ █████` to confirm database is running and service ms-sql-s is accepting connections: 
`(UNKNOWN) [███████] ████████ (ms-sql-s) open
^C sent 0, rcvd 0
`

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
███████ should not be available on the server.

## Impact

Possible access to database as well as disclosure of sensitive host information.

## Attachments
No attachments
