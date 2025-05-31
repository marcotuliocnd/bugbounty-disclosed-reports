# Course Registration Form Allowing an attacker to dump all the candidate name who had enrolled for the course

## Report Details
- **Report ID**: 1100383
- **URL**: https://hackerone.com/reports/1100383
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-10T21:40:09.137Z
- **Disclosed**: 2024-08-16T16:09:19.413Z

## Reporter
- **Username**: steveflex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:** 

The given application has a form to fill in the details of the candidates in order to seek admission to various courses. The application has the functionality to submit the given form and provide a registration confirmation to the candidate with their name on the page. By cycling the parameter we can enumerate all the applicant's names who had applied for the specific courses.

**Description:**
We can cycle the numeric value after the registration process and enumerate all the candidate names.

## Impact
The attacker might carry out targeted attacks against the given organization by exfiltrating details from the candidates. The attacker can also find the candidates easily on social media sites to carry out further attacks.

## Step-by-step Reproduction Instructions

1. Fill in the form in order to apply/register for the courses online  https://www2.█████████/asops/CESET/DotNet/(S(zxfdh3222tuxim4qkyddqkc4))/Register.aspx?s=1&c=SOC-E
2. After the form is filled, the confirmation messaged is displayed in a URL as https://www2.████████/asops/CESET/DotNet/(S(y4xw2rqkzk1zzzej0mu2atng))/RegistrationConfirmation.aspx?stu=490504
3. The attacker can cycle the stu value from the beginning and enumerate thousand of candidates enrolled for the courses. 
4. Here we have automated the attack in order to get user details in a short period of time. Please refer to the screenshot below having the results.


## Suggested Mitigation/Remediation Actions
The application shall generate hashed values instead of numeric values so that the attacker cannot guess the user details.

## Impact

The attacker might carry out targeted attacks against the given organization by exfiltrating details from the candidates. The attacker can also find the candidates easily on social media sites to carry out further attacks.

## System Host(s)
www2.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Fill in the form in order to apply/register for the courses online  https://www2.███████/asops/CESET/DotNet/(S(zxfdh3222tuxim4qkyddqkc4))/Register.aspx?s=1&c=SOC-E
2. After the form is filled, the confirmation messaged is displayed in a URL as https://www2.██████/asops/CESET/DotNet/(S(y4xw2rqkzk1zzzej0mu2atng))/RegistrationConfirmation.aspx?stu=490504
3. The attacker can cycle the stu value from the beginning and enumerate thousand of candidates enrolled for the courses. 
4. Here we have automated the attack in order to get user details in a short period of time. Please refer to the screenshot below having the results.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
