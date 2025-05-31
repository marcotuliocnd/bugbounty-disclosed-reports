# Read-Only user can delete users

## Report Details
- **Report ID**: 888729
- **URL**: https://hackerone.com/reports/888729
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-01T19:08:51.888Z
- **Disclosed**: 2020-07-10T18:30:21.337Z

## Reporter
- **Username**: amr_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
hello 
this endpoint (DELETE /api/invitations/0ff7e9f9-877a-40cc-b99f-f6b3b1bea3f8 )vulnerable  to Insecure Direct Object Reference
Steps to reproduce the bug
Let's assume that three accounts exist:
admin@helium.com        (role Administrator)
attacker@helium.com   (role Read-Only)
victim@helium.com        (invited user )
all three account in same organization (h1)
attacker@helium.com cant delete victim@helium.com but we can do that 
from admin@helium.com go to delete victim@helium.com 
request like that DELETE /api/invitations/0ff7e9f9-877a-40cc-b99f-f6b3b1bea3f8
take id victim@helium.com 0ff7e9f9-877a-40cc-b99f-f6b3b1bea3f8
go to attacker@helium.com switch another organization (h2)
and go to delete invited user from this organization(h2)
DELETE /api/invitations/a996881d-7177-43fb-be7c-da3a6b005f40
change id (a996881d-7177-43fb-be7c-da3a6b005f40) to id you got from admin@helium.com(0ff7e9f9-877a-40cc-b99f-f6b3b1bea3f8)
respond 
HTTP/1.1 204 No Content
Date: Mon, 01 Jun 2020 18:47:43 GMT
Content-Length: 0
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Message: User removed from organization
Strict-Transport-Security: max-age=31536000
Via: 1.1 vegur
CF-Cache-Status: DYNAMIC
cf-request-id: 0312cf14d40000edeb299e9200000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 59cb1ace2eeaedeb-CDG

now account victim@helium.com deleted from attacker@helium.com
i can make poc 
thanks

## Impact

Read-Only user can delete users

## Attachments
No attachments
