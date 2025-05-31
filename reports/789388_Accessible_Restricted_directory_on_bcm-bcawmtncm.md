# Accessible Restricted directory on [bcm-bcaw.mtn.cm]

## Report Details
- **Report ID**: 789388
- **URL**: https://hackerone.com/reports/789388
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-05T16:24:56.718Z
- **Disclosed**: 2020-07-15T08:54:21.365Z

## Reporter
- **Username**: tounsi_007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
* There are some exposed `directory/files` publicly accessible for anyone, when it should be restricted on the server

## Steps To Reproduce:
* Go to `http://bcm-bcaw.mtn.cm/wp-content/uploads/` and navigate between available folders

==**Poc:**== {F707036}

## Impact

>
* Every uploaded data can be accessible through this directory listing vulnerability
* This might include several private/confidential data
>

## Attachments
- bcm-bcaw.mtn.cm.png
