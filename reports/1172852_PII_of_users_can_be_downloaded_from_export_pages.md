# PII of users can be downloaded from export pages

## Report Details
- **Report ID**: 1172852
- **URL**: https://hackerone.com/reports/1172852
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-22T22:09:43.918Z
- **Disclosed**: 2023-05-12T13:02:28.708Z

## Reporter
- **Username**: chip_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:
On the https://doaction.org/ pages can be enumerated via 'p' get parameter, for example:
https://doaction.org/?p=1657 redirects to https://doaction.org/event/ijebu-2019/
https://doaction.org/?p=1320 redirects to https://doaction.org/non-profit/test/
Using it I have enumerated almost 1000 unique endpoints and on some of them I found csv files with PII of users (Name,Email,Phone,Role,Organisation
). I suppose that this is the data of hackathons participants. Links to download pages:
https://doaction.org/do_action-export-1498557984/
https://doaction.org/do_action-export-1498737049/
https://doaction.org/do_action-export-1498745152/
https://doaction.org/do_action-export-1498812322/
https://doaction.org/do_action-export-1500046180/
https://doaction.org/do_action-export-1500469161/
https://doaction.org/do_action-export-1518613217/
https://doaction.org/do_action-export-1519205241/
https://doaction.org/do_action-export-1519327599/
https://doaction.org/do_action-export-1523894240/
https://doaction.org/do_action-export-1529355810/
https://doaction.org/do_action-export-1530608893/
https://doaction.org/do_action-export-1530956399/
https://doaction.org/do_action-export-1530964074/
https://doaction.org/do_action-export-1530964096/
https://doaction.org/do_action-export-1531988106/
https://doaction.org/do_action-export-1532000396/
https://doaction.org/do_action-export-1532075463/
https://doaction.org/do_action-export-1532672117/
https://doaction.org/do_action-export-1535471764/
https://doaction.org/do_action-export-1535751740/
https://doaction.org/do_action-export-1535999159/
https://doaction.org/do_action-export-1536309599/
https://doaction.org/do_action-export-1536389295/
https://doaction.org/do_action-export-1540023637/
https://doaction.org/do_action-export-1552910175/
https://doaction.org/do_action-export-1553260656/
https://doaction.org/do_action-export-1553882619/
https://doaction.org/do_action-export-1554723418/
https://doaction.org/do_action-export-1554815348/
https://doaction.org/do_action-export-1555393513/
https://doaction.org/do_action-export-1555393534/
https://doaction.org/do_action-export-1555393708/
https://doaction.org/do_action-export-1555393762/
https://doaction.org/do_action-export-1556007840/
https://doaction.org/do_action-export-1556007849/
https://doaction.org/do_action-export-1556007854/
https://doaction.org/do_action-export-1556739301/
https://doaction.org/do_action-export-1556903021/
https://doaction.org/do_action-export-1556946934/
https://doaction.org/do_action-export-1559905698/
https://doaction.org/do_action-export-1560342197/
https://doaction.org/do_action-export-1561023007/
https://doaction.org/do_action-export-1561023537/
https://doaction.org/do_action-export-1561023566/
https://doaction.org/do_action-export-1561023592/
https://doaction.org/do_action-export-1561023611/
https://doaction.org/do_action-export-1561023668/
https://doaction.org/do_action-export-1561023675/
https://doaction.org/do_action-export-1561180440/
https://doaction.org/do_action-export-1561973925/
https://doaction.org/do_action-export-1562147045/
https://doaction.org/do_action-export-1562194238/
https://doaction.org/do_action-export-1562194534/
https://doaction.org/do_action-export-1562571037/
https://doaction.org/do_action-export-1562669416/
https://doaction.org/do_action-export-1562930528/
https://doaction.org/do_action-export-1565427972/
https://doaction.org/do_action-export-1565441079/
https://doaction.org/do_action-export-1567233021/
https://doaction.org/do_action-export-1567233029/
https://doaction.org/do_action-export-1567233035/
https://doaction.org/do_action-export-1567233041/
https://doaction.org/do_action-export-1567233047/
https://doaction.org/do_action-export-1567233054/
https://doaction.org/do_action-export-1567827712/
https://doaction.org/do_action-export-1571049910/
https://doaction.org/do_action-export-1571361570/
https://doaction.org/do_action-export-1571421316/
https://doaction.org/do_action-export-1574064498/
https://doaction.org/do_action-export-1575649680/
https://doaction.org/do_action-export-1576268072/
https://doaction.org/do_action-export-1578466099/
https://doaction.org/do_action-export-1578472524/

## Steps To Reproduce:
1. Enumerate endpoints requesting https://doaction.org/?p={id}. I tried [1..10000] ids in my research. You will get 301 response on valid ones, and you can extract full path to page from Location header:  
{F1275174}
2. Research endpoints and on some PII is avaliable

## Recommendations
Restrict access to sensitive files using some form of authentication or delete them.

## Impact

PII data leakage

## Attachments
- 1.PNG
