# 403 Forbidden Bypass at www.██████.mil

## Report Details
- **Report ID**: 991717
- **URL**: https://hackerone.com/reports/991717
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-26T00:07:46.312Z
- **Disclosed**: 2020-11-02T21:45:33.717Z

## Reporter
- **Username**: sldwn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team,
I managed to bypass 403 forbidden pages in www.████████.mil
#Reproduce
1) Click https://www.████████.mil/███████  (Example Forbidden page). If you click you will redirect to 403 "forbidden" page.
2) But you can bypass this.
3) type this command: `curl -H "Content-Length:0" -X POST https://www.████████.mil/███ `



#Proof-of-Concept
For exploit write this command.
Exploited command: `curl -H "Content-Length:0" -X POST https://www.███████.mil/██████████ `
Denied command: `curl -X GET https://www.███████.mil/██████`
#Questions:
**Why you need  "Content-Length:0" header?**
**Answer:** If you dont use this headersometimes you can get 411 error code.
**Can i reproduce this in burpsuite?**
**Answer:** Yes, you can.But "curl" faster.
**How you did bypass?**
**Answer:**With POST method and Content-Length header.If you send GET or dont use that header you cant bypass.

#Note
I looked for something important in the site. However, I could not find it. But if something important is used within the site and maintained in the same way, it may be possible to bypass it with the same techniques.

## Impact

Attacker can bypass forbidden 403 pages.

## Attachments
No attachments
