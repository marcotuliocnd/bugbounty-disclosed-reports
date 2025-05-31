# Unrestricted File Upload Leads to XSS & Potential RCE

## Report Details
- **Report ID**: 900179
- **URL**: https://hackerone.com/reports/900179
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-17T06:08:54.158Z
- **Disclosed**: 2020-07-08T17:47:54.279Z

## Reporter
- **Username**: 5050thepiguy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Unrestricted file upload at████████/request?openform. When the user wants to upload a file the app allows the user to upload a HTML file leading to stored XSS and creation of a simple php script. A user can upload the HTML file and trigger XSS and trigger potential RCE with php shell. Please go to the ██████ Request that I created at -- ██████████AllOpenOrders/4F4D0C69EA2B33A58525858A001E2B8C?opendocument and select the file at the bottom "unsure1.html" to trigger payload to show XSS and php shell. You can also go directly to the uploaded file at ████0/4f4d0c69ea2b33a58525858a001e2b8c/$FILE/unsure1.html. Please see the attached PoC video as well. Thanks.

## Impact
The unrestricted file upload vulnerability leads to stored XSS and creation of php shell leading to potential RCE, which opens the door to numerous malicious attacks by the attacker. 

## Step-by-step Reproduction Instructions

1. Go to███/request?openform
2. Enter in the details for this page and you will automatically be redirected to the next page. Do the same thing here and enter in all the necessary information
3. Then, towards the bottom you are given the option to upload files so click "browse" and upload your payload
4. Click "submit request" then go back to █████████ModifyRequest.xsp and enter in the 14 digit Document Number. 
5. Scroll down to the bottom of your request and click the HTML payload.
6. Observe that XSS triggers and php shell is seen as well. 

## Product, Version, and Configuration (If applicable)
███
███request?openform

## Suggested Mitigation/Remediation Actions
Restrict file uploads to only necessary business requirements. If possible restrict uploads to JPG, DOC, DOCX, and PDF. Don't allowed upload of executable files.

##References
Please see attached PoC video
Please see attached PoC HTML page as well used for the payload

## Impact

The unrestricted file upload vulnerability leads to stored XSS and creation of php shell leading to potential RCE, which opens the door to numerous malicious attacks by the attacker.

## Attachments
No attachments
