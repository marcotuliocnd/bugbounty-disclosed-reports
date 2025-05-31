# Any one can view collaborater email address via  path /reports/<id>/participants 

## Report Details
- **Report ID**: 1918362
- **URL**: https://hackerone.com/reports/1918362
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-26T13:55:50.375Z
- **Disclosed**: 2023-06-01T10:16:21.044Z

## Reporter
- **Username**: aloneh1_breecher
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello team,

I can able to find while inviting a collaborator to my report i must enter his/her username or mail id but what if the user doesnt have an account in hackerone we need to gave the email so i gave an email to invite a collaborator and i viewed the request in burp below.


Step to reproduce:

1:  select a report of yours 
2: add a user to that report as collaborator with an email of unaccounted user in hackerone
3: now after successfully invited that collaborator view the below request

```
GET /reports/<REPORT ID>/participants HTTP/2
Host: hackerone.com
Cookie: h1_device_id=da6b4e1e-7e67-46fc-85f0-b7eb0ce35f63; __Host-session=b2U1bThJMlVxcGdQM3MvcEw4NDFMRDcyMTY2ejFQTmRUM1BmUWJOZzlOL3liZjllQjlPQjlyekh4QjFVWGtMbDFjQ0JUbFpTUzNIK2ZqSWI4SmR6NmhPY2pCbG0vbFViTVhBdk1IbzYxVDEvdHVBakxPSEZBdndtSVJ3WDVkbTBIR0dXaHgvNWpYTU5GZFhDc2E1aGErVW1DOElUVlNSbklFMkRyWnhyTVJKODIxSERFSm5iZHJDRit5MER5aG5URk9YSy9RSExPNzJwOStkZm04OXhKY2d5V3pqdlkybmdhS2xoQVlpZnVMWFVTMGs0VnY1RlB4dGFkV2JEdTRQemV3WmdoMGtFWVB2a1lnNDBLL3RPSFM3WmJlOWhhNW5ZYW9QL2FNNVFBYTlYNHVjY2g5UmwyT2FrT2VjQU5kZktlQlJ2ZzBLSE1zZXZJTFdQN2hKYXlvT0xhbmpPL09oZXM3OWtqK2xJVy9DWVpkNUx1T0V6NHd5dDYvNStFM1VmUitpMUhzOUFISUx4clpKSDFMbVBFc2hQb2hGbGVQSXRBZFN2Wno5a1BDbVVka09mbUJ2c3gyWDNLTDFMV1dkUTdMNE52U3BCSFQwS0RKUzljZEFLL2lBa0d3SDNPaVZ1WG43Z0ZXRUlMeVVQTWhRbHY0T2lCdkk3elZxNVFjR3o1Q3VTYU9qYmZSNlNpbDR3OXVPN1B2RlNOUlJ2VFozZGdGeHRRa0IzaEJlUmgvcklEaXQxN2NGZkZ2R3Y0alJrYkl5aFdCbzNGS1JNSU5hUTd0RDRWN0grV0N3c1NrT3NuUU5IYXZmN3hxQmwyN05EVlozQlVETVBtMC9TcHcwUUhDeVU2ZElDRXFCZUdMd0ExRE9wSDVKMFRLbHA4RE5CajhJK2JrZndQWEYvU0FMMUxYcmxEc1RzOXBQZWp3RmYtLXdtSUdLcFNUUjN2dUF1aVY4T0NpSFE9PQ%3D%3D--6dc5688902c36c0edb857120e9bd8665e5170af5; cf_clearance=5vpfeLN93oq5Ya6zAU922X6WutTn5zr1K6sJZLcC_vM-1679832536-0-160; AMP_b7cba2c14c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzOWIyMGZkMC1lNzkxLTRmYjYtYmM4Yy01NmZkNTg1NzJhZTclMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhODc0ZDkzMC0wYjhlLTQ4MDAtYTgzNy03ODhhZDBiYmIxOTQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjc5ODMyNTM3NjYyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY3OTgzNzc4OTQyNCU3RA==; _dd_s=rum=0&expire=1679838753537; AMP_MKTG_b7cba2c14c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmhhY2tlcm9uZS5jb20lMkZ1c2VycyUyRnNpZ25faW4lM0ZfX2NmX2NobF90ayUzRHA4cDlfbWFhNmYwVVFGVG9sc2ZPUGdXZ3lITVZhQXhkQ0kyeS42QUtpZ2MtMTY3OTgzMjUzNi0wLWdhTnljR3pORFZBJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMmhhY2tlcm9uZS5jb20lMjIlN0Q=; app_signed_in=true; intercom-session-zlmaz2pu=bzZuM2JDdDhrTnFUWG1uWUJRY1B2M3VUNExvZlpaLzI3MTl3RG54aXdJcjA5MkxaVy9ROCt2NTIwRzl3ek1Jcy0tV0hUSVlYVGdPaVUyTTMzY01MSGxvZz09--38ddd56d970208e627e2c72f0ae8c6324d74baab; intercom-device-id-zlmaz2pu=81f9084c-a95c-4ea3-9bdb-2b9b205066f8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bugs?subject=user&report_id=1916579&view=open&substates%5B%5D=new&substates%5B%5D=needs-more-info&substates%5B%5D=pending-program-review&substates%5B%5D=triaged&substates%5B%5D=pre-submission&substates%5B%5D=retesting&reported_to_team=&text_query=&program_states%5B%5D=2&program_states%5B%5D=3&program_states%5B%5D=4&program_states%5B%5D=5&sort_type=latest_activity&sort_direction=descending&limit=25&page=1
X-Csrf-Token: /0WTxdkHSG7HTBX5Ln0CmyeSJvlbzED1XhCIVR8fj5SxVX925l1OJZp9T/Gs9mnJiZcKSF8uowuLEkgylReFIQ==
X-Requested-With: XMLHttpRequest
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

```

4:  you see a response like this :

```
"participant_type":"ReportParticipants::CollaboratorInvitation","id":4049018,"email":"██████████@gmail.com","bounty_weight":"0.3"},
```

Thanks,
alone_h1

## Impact

impropper access control to view email.

## Attachments
No attachments
