# resetreportedcount & updatetags doesn't verify appid param

## Report Details
- **Report ID**: 351106
- **URL**: https://hackerone.com/reports/351106
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-13T11:05:19.956Z
- **Disclosed**: 2018-07-02T23:49:14.415Z

## Reporter
- **Username**: creekie
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
This **requires** an account that has admin permissions on any community hub & Fiddler (not 100% required, but I'll use it for the demonstration.)

**resetreportedcount**:

Step 1:
Go to any UGC in the hub you have admin access on, open Fiddler if you haven't yet, click Clear Reports and click OK on the dialogbox.

Step 2:
Drag that request over to the composer tab, modify the id param in the body to any UGC (Outside your hub!), and execute the request! You've now reset all reports on that UGC item.

**updatetags**:

Step 1:
Go to any **guide** in the hub you have admin access on, open Fiddler if you haven't yet, click Update Tags and just select a few checkboxes and click Update. 

Step 2: 
Drag that request over to the composer tab, modify the id param in the body to any guide (Outside your hub!), and execute the request! You've now updated that guide's tags.

**Guide before**
{F296857}

**Guide after**
{F296858}

## Impact

An attacker could reset all reports on UGC, and could also change a guide's tags.

## Attachments
- Steam_2018-05-13_12-51-18.png
- Steam_2018-05-13_12-52-22.png
