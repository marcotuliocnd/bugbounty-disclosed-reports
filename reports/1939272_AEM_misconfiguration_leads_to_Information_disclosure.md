# AEM misconfiguration leads to Information disclosure

## Report Details
- **Report ID**: 1939272
- **URL**: https://hackerone.com/reports/1939272
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-08T02:40:27.835Z
- **Disclosed**: 2023-05-15T15:05:48.523Z

## Reporter
- **Username**: cametome006
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello Team,

I was able to access sensitive information by appending `/.1.json` to certain URLs on ████Specifically, by visiting the following URL, I was able to obtain a JSON response that contained all the templates and files present in the web root due to AEM misconfiguration:

█████████
██████████

 We can see it disclose system username and templates used by the system. This presents a serious security risk, as an attacker could use this information to gain access to sensitive files or directories that should not be publicly available.

## Impact

* Loss of confidentiality: The disclosure of internal username and webroot directories can result in a loss of confidentiality of sensitive information. This can lead to unauthorized access, manipulation, or exploitation of the disclosed information.

* Social engineering attacks: Internal username can be used in social engineering attacks such as phishing, spear-phishing, or pretexting. Attackers can use this information to craft targeted emails or other communications that appear to come from a trusted source and attempt to deceive the recipient into divulging sensitive information or clicking on malicious links.

* Reputation damage: The disclosure of sensitive information can damage an organization's reputation and erode trust among customers, partners, and stakeholders.

https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit : ███, █████

## Suggested Mitigation/Remediation Actions
https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/



## Attachments
No attachments
