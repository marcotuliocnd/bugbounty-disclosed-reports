# █████████ IDOR leads to disclosure of PHI/PII

## Report Details
- **Report ID**: 1085782
- **URL**: https://hackerone.com/reports/1085782
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-01-24T08:01:48.742Z
- **Disclosed**: 2021-02-18T19:17:50.327Z

## Reporter
- **Username**: nidens
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
████ is designed in a way where there is a vulnerable endpoint that allows a non-medical user to view the ██████████ records of people who are not ████████s of the sponsor. 

**Description:**
I am currently an Active Duty Airman and this vulnerability does require CAC authentication. When browsing the ██████ website with a proxy I noticed that there is a function that allows sponsors (in this case me) to view their █████s shot records in PDF form. After viewing my ██████████'s shot records, I noticed this functionality lives on the following endpoint `https://████=[id]`.  If you increment or decrement the `██████` parameter by 1 the application will throw an HTTP Status Code 302 and redirect you back to the `██████████` endpoint which is a good security practice. The issue with this is, that with the 302 redirect the PDF of the incremented ID will be attached in the body of the 302 requests, you are able to extract this when using a proxy like Burp Suite. Obviously, this is concerning because this would allow a user to pull any shot record without being associated with medical. 

## Step-by-step Reproduction Instructions
### I have redacted the screenshots as best as possible. The screenshots are of my information, the example for validation.

1. Navigate to ████/█████ and login with CAC
2.  Once you are authenticated browse to this endpoint, https://███████=█████████ and you should be redirected to `█████` but the 302 redirect will have the PDF information of my daughter (no actual ██████████ information is loaded).
3. On the 302 redirects, you can utilize the function `Copy to File` in burp suite to save this request as a pdf and you will have a PDF version of my ██████ shot record. 

Please review the attached screenshot, I did not pull use my █████ information for this screenshot because I have authorized to view her information. This request shows me decrementing the `██████` by 1 and showing the PDF is attached to the 302 redirects. 
██████


## Suggested Mitigation/Remediation Actions
Enforce the same permissions that are used for the `██████████` and `████` functions of the application. 

I am more than willing to speak with the developers about this if they want to e-mail my NIPR email. I took care to not go any further than just validating that the vulnerability exists and immediately stopped and started to write this report.

## Impact

PHI/PII disclosure which includes, ████████

## Attachments
No attachments
