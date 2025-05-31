# Private data related to program exposed via /reports/<id>.json endpoint to external user participant

## Report Details
- **Report ID**: 2580982
- **URL**: https://hackerone.com/reports/2580982
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-28T12:22:20.281Z
- **Disclosed**: 2024-08-30T03:53:25.223Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary & Impact:**
An organization has the ability to invite external participants not belonging to their organization to a bug report. The invited user is sees partial data and metadata of a bug in the UI after they accept the invitation. However, in this case I have discovered a way that will make a participant view more data that what is allowed. The data consists of program profile picture, twitter handle, website, about and the asset details to which the report belongs.

### Steps To Reproduce
1. Login to your H1 account. 
2. Create a sandbox program .
3. Create a test bug report in your program. (Or there would be already a test report present in the sandbox program)
4. Invite an external participant to the report by providing that person's email address. 

{F3395844}

5. As the participant user accept the invitation and go to the bug detail page and open the program page in new tab. 

{F3395852}
{F3395853}
{F3395854}

6. Observe that you do not have access to this data: 
 * program profile picture
 * twitter handle
 * website
 * about
 * the asset details to which the report belongs
7. Now as the participant user send the following request by replacing your cookies, CSRF token and report id. Observe that you see that details in the response.
```
GET /reports/<the-report-id-here>.json HTTP/2
Host: hackerone.com
Sec-Ch-Ua-Mobile: ?0
X-Datadog-Origin: rum
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36
X-Datadog-Sampling-Priority: 1
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
X-Datadog-Parent-Id: 578794727646244533
X-Datadog-Trace-Id: 180506980422927885
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackerone.com/reports/2542179
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=1, i
Cookie: <your-cookies-here>
Content-Length: 0
Sec-Ch-Ua: "Not(A:Brand";v="24", "Chromium";v="122"
X-Csrf-Token: <your-csrf-token-here>
```
{F3395862}
{F3395864}

## Impact

Private data is exposed to unauthorized users. This affects the confidentiality of the program.

## Attachments
- 2024-06-28_174326.png
- 2024-06-28_174704.png
- 2024-06-28_174534.png
- 2024-06-28_174604.png
- 2024-06-28_174958.png
- 2024-06-28_175033.png
