# Object Level access control leads to reading user's full requests, sessions, and error messages

## Report Details
- **Report ID**: 2891449
- **URL**: https://hackerone.com/reports/2891449
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-12-10T06:16:56.171Z
- **Disclosed**: 2025-01-18T18:10:56.251Z

## Reporter
- **Username**: mester_x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
# Summary:
When you visit the subdomain https://proze.yelp.com/ it'll redirect you to the main domain https://www.yelp.com/, The tests show that the application hosts an internal administration tool called  **Tailored Mail**, you can verify this by visiting the endpoint https://proze.yelp.com/app/login.
Since the application is for the internal Yelp admins, you can't access the API or hit any internal data (should be).

**The bug found is a lack of Object level on the internal API Error and debugging endpoint allows unauthenticated attackers to read the internal admin's full sessions, HTTP requests data, and other internal information.**

* The endpoint retrieves the API logs and you can visit each log details and you can read the entire user HTT request and internal data.
* **An attacker can use the retrieved HTTP request data to hijack the admin's accounts, which leads to full ATO.**


# Platform(s) Affected:
https://proze.yelp.com/


# POC:
* The video below is proof:
███████

# Steps To Reproduce:

  1. Visit the subdomain https://proze.yelp.com to verify that you have no access and will redirected to the main domain.
  1. Now visit the admin tool application login https://proze.yelp.com/app/login to verify the existence of the administration tool application there
  1. Visit the endpoint [/tmwebapi/elmah.axd](https://proze.yelp.com/tmwebapi/elmah.axd?page=1&size=100) to read the first last 100 requests logs.
  1. Press `Details` to read any log full internal data
  1. Now visit the endpoint [5A4E7ED8-28E8-4E39-9017-F55E2C9F5371](https://proze.yelp.com/tmwebapi/elmah.axd/detail?id=5A4E7ED8-28E8-4E39-9017-F55E2C9F5371) to read on of the logs with the user cookie and secrets 
  1. You can read logs up to older dates, like visit the endpoint [First-Of-Dec](https://proze.yelp.com/tmwebapi/elmah.axd?page=100&size=100) and you'll read logs from the first of Dec.

# Recommendations:
Place an access control over the  Error Log for TMWebAPI on M7WEB-07 `/tmwebapi/elmah.axd`

## Impact

Object-level access control leads to reading the user's full requests, sessions, and error messages

## Attachments
No attachments
