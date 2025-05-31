# Flash CSRF: Update Ad Frequency %: [cp-ng.pinion.gg]

## Report Details
- **Report ID**: 251918
- **URL**: https://hackerone.com/reports/251918
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-21T01:46:13.074Z
- **Disclosed**: 2017-09-06T06:31:38.932Z

## Reporter
- **Username**: geekboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information

###Description:
-----------
Attacker can update the user's Ad Frequency % using flash + 307 redirect trick by making post request to particular endpoint.

###Step To Reproduce: 
-----------
+ Get logged at: https://cp-ng.pinion.gg
+ Visit: http://geekboy.ninja/poc/freq.swf
+ Ad Frequency should be updated.

*Note: for test i used my account with id `████`, as update request use userid in endpoint, it can be modified as per need.* 

{F205068}





Please let me know if any more info needed !

-------------

__*- Geekboy!*__



## Attachments
No attachments
