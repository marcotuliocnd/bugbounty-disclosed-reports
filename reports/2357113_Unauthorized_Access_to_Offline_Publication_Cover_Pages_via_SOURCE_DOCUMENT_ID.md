# Unauthorized Access to Offline Publication Cover Pages via SOURCE_DOCUMENT_ID

## Report Details
- **Report ID**: 2357113
- **URL**: https://hackerone.com/reports/2357113
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-06T21:29:26.114Z
- **Disclosed**: 2024-03-13T09:12:42.493Z

## Reporter
- **Username**: giwadaoud
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: publitas

## Vulnerability Information
I discovered a vulnerability that is related to accessing publication cover pages via a specific request using **sourceDocumentId**. When sending a request with the **source ID**, the system responds with a URL to the cover page of that publication. However,  the cover page is intended to be offline and not publicly accessible and the offline publication are only accessible by the account users. Beside that in the URL there is also the user id and the main id corresponding to that publication. So, due to a vulnerable endpoint we are able to disclose the cover page of an offline publication that we don't own.

{F3033179}

Vulnerable endpoint: ██████████

* Steps to Reproduce: 
1. Create account on ██████.
2. Create a new offline publication and take the **sourceDocumentId** of it.
3. Send a request to the program's endpoint with a valid **SOURCE_ID** corresponding to a specific publication.
4. Analyze the response to retrieve the URL of the publication's cover page.
5. Access the URL provided in the response, which contains both the user ID and the main ID of the publication.

## Impact

This vulnerability allows unauthorized access to offline publication cover pages, which may contain sensitive information not intended for public viewing. An attacker could potentially view confidential content from the cover pages of unpublished publications.

## Attachments
- image.png
