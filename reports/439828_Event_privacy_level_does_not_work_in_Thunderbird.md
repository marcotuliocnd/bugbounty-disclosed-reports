# Event privacy level does not work in Thunderbird

## Report Details
- **Report ID**: 439828
- **URL**: https://hackerone.com/reports/439828
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-13T11:04:09.674Z
- **Disclosed**: 2020-03-01T13:55:46.779Z

## Reporter
- **Username**: maksemuz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Events in shared calendar with changed privacy level to any other than public are shown in Thunderbird as public anyway (with all details)
How to reproduce:
1 - create an event in user A's calendar shared to user B
2 - change privacy setting of this event to any other than public
3 - open Thunderbird as user B
4 - connect to user A's calendar
5 - behold the test event show as public with all details, not "Busy" brick for "show only busy"  or nothing for "private"

## Impact

Thunderbird user with read access can see all events with all details despite restrictions and thus can get some private info.

## Attachments
No attachments
