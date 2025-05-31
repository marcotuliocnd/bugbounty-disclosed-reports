# Database resource exhaustion for logged-in users via sharee recommendations with circles

## Report Details
- **Report ID**: 1688199
- **URL**: https://hackerone.com/reports/1688199
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-31T21:12:53.530Z
- **Disclosed**: 2022-11-26T06:52:11.016Z

## Reporter
- **Username**: michag86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Registered users can generate massive database load 

## Steps To Reproduce:

  1. create 9 circles and 6 folders (circles * folder > 50)
  2. share all created folders with all created circles
  3. open an other folder and open the share tab, so the URI /ocs/v2.php/apps/files_sharing/api/v1/sharees_recommended is requested
  4. this requests results in a loop that runs as long as the php value max_execution_time is set; the recommended value for this is 3600 seconds (1h)
  5. a small number of these requests will stress even large servers

Tested with Nextcloud 23.0.8

## Impact

Attacker slow down the system by generating a lot of database/cpu load.

## Attachments
No attachments
