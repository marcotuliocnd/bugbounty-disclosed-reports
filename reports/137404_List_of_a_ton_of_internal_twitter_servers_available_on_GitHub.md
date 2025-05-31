# List of a ton of internal twitter servers available on GitHub

## Report Details
- **Report ID**: 137404
- **URL**: https://hackerone.com/reports/137404
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-10T04:25:19.405Z
- **Disclosed**: 2016-10-17T18:32:15.798Z

## Reporter
- **Username**: a0005
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
The page at https://raw.githubusercontent.com/adi2909/basic-py/0532539f86cbb584aa7bfd8cc357fc9df4c25c03/data/allHostInfo.json

has a ton of internal info about twitter hosts, including MACs, NICs, other hardware info, and hostnames.  This data, albeit a little dated, gives an attacker an excellent view into hardware, patching status, and network topology.

I've uploaded a parsed JSON of this information


## Attachments
- formatted.json
