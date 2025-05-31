# Privilege Escalation - "Analyst" Role Can View Email Domains of a Company - [GET /voyager/api/voyagerOrganizationDashEmailDomainMappings]

## Report Details
- **Report ID**: 1572591
- **URL**: https://hackerone.com/reports/1572591
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-17T03:10:57.629Z
- **Disclosed**: 2022-08-26T18:38:48.205Z

## Reporter
- **Username**: naaash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
## Summary:
Hey team,
During the security assessment, I came across an endpoint - `GET /voyager/api/voyagerOrganizationDashEmailDomainMappings`, which is vulnerable to **privilege escalation**. A lower privileged user can abuse this to view the list of approved domains for email verification even though it can't be accessed directly from the UI.

## Vulnerable HTTP Request:
```
GET /voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0 HTTP/2
Host: www.linkedin.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: application/vnd.linkedin.normalized+json+2.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Restli-Protocol-Version: 2.0.0
Dnt: 1
Referer: https://www.linkedin.com/company/81541206/admin/manage-admins/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Cookie: REDACTED
Csrf-Token: REDACTED
```
## Steps to Reproduce:
* Go to https://www.linkedin.com/ and log in to your test account.
* Go to **"Me"** and click on your company under the **"Manage"** section.

{F1732479}
* Go to **"Admin Tools"** > **"Employee Verification"**

{F1732480}
* Intercept the vulnerable HTTP request.
* Change all the values of the cookie parameters & CSRF token to that of a lower privileged user (**"Analyst"** role). The response will disclose the approved domain for verification.

{F1732484}

# PoC:
* Have a look at the video here:

{F1732486}

## Impact

A lower privileged user can abuse this to view the list of approved domains for email verification even though it can't be accessed directly from the UI.

## Attachments
- Screenshot_2022-05-17_at_8.34.38_AM.png
- Screenshot_2022-05-17_at_8.35.37_AM.png
- Screenshot_2022-05-17_at_8.37.41_AM.png
- Screen_Recording_2022-05-17_at_8.38.36_AM.mov
