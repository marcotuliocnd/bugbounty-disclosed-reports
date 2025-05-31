# Information Disclosure (can access all ███s) within ███████ view █████████ Portal

## Report Details
- **Report ID**: 484377
- **URL**: https://hackerone.com/reports/484377
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-23T01:42:53.755Z
- **Disclosed**: 2019-10-08T18:58:30.363Z

## Reporter
- **Username**: archang31
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:** Once ███████ authenticated (I did not mess around to see if I could reproduce without authentication), any user can view any ██████████ simply by changing the offasgid HTTP GET parameter value in the ██████ view █████████ portal link.

**Description:**
I was looking through my previous ███████s and noticed I was receiving urls like https://█████████/portal/viewrfo.aspx?offasgid=MjAwODAyMTg1Nw== . This url is clearly expecting a HTTP GET parameter offasgid with some base64 encoded value. Decoding this value, you get 2008021857 . The █████ in question was my first █████ from February 2008. From testing several IDs, I determined the format is {year}{██████████ #} so 2008, ████████ # 021857.  I simply incremented this value to 2008021858, base64 encoded this value, and browsed to https://███/portal/viewrfo.aspx?offasgid=MjAwODAyMTg1Ng==  . Here, I was able to see ███████.  I also tested the next value ( https://███/portal/viewrfo.aspx?offasgid=MjAwODAyMTg1NQ== ) and got █████. Finally, I opened a new private browser window (so no cookies) and browsed directly to that last link. I had to reauthenticate, but I then was able to directly assess ██████████. At this point, I stopped interacting with the website to submit this vulnerability. 

NOTE: I did not save any record of these ███████s outside except the single attached screenshot.
NOTE2: I tried a couple more values during this write-up to better understand the ID. I initially thought the 02 from 2008021858 was the month {year}{month}{id} but its just {year}{id}. I used 2018000001 and ended up with an ████████ from 20171001 (the very first day of the 2018 fiscal year). I also tested a couple IDs to see how far back the data goes. I used 1999000001 to pull an ██████ from 19980327. I believe this is the very first █████ in the system. I tried 1997000001 as well, and it simply returned a blank ████ (i.e. the ID does not exist).

## Impact
In a relatively simple and predictable manner (due to the sequential IDs), any user with access to █████ can incrementally view every ███ issued by ████████ dating back to 1998. This data includes SSN last 4, EFMP information, branch, and assignment information. From this data, one can extract all sorts of information about the U.S. █████████ personnel including total ██████████ strength, ████ strength by branch, assignment history, strength by base, etc.

## Step-by-step Reproduction Instructions

1. Log into ██████████ (https://███.██████████.███████.mil/)
2. Browse to any █████████ you want to view like https://████/portal/viewrfo.aspx?offasgid=MjAxOTAxMDg2NQ== if you want to view my most recent ███.
3. Modify offasgid value as desired to view any other ███████ (they seem to be incrementing IDs by year)

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
First, the offasgid needs to be random and not a predictable value. Secondly, there needs to be some access check based on the provided cookie (user credentials) to ensure that user should be able to access that record.

## Impact

In a relatively simple and predictable manner (due to the sequential IDs), any user with access to ████ can incrementally view every ███████ issued by ██████ dating back to 1998. This data includes SSN last 4, EFMP information, branch, and assignment information. From this data, one can extract all sorts of information about U.S. ████ personnel including total ███ strength, ████████ strength by branch, assignment history, strength by base, etc.

## Attachments
No attachments
