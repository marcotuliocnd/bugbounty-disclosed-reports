# Subdomain takeover of ███

## Report Details
- **Report ID**: 892667
- **URL**: https://hackerone.com/reports/892667
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-06T11:28:54.726Z
- **Disclosed**: 2021-09-09T19:55:15.327Z

## Reporter
- **Username**: simplyrishabh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Summary:
The subdomain ██████ had an CNAME record pointing to an unclaimed ███████ webservice. This is a high severity security issue because an attacker can register the subdomain on ███ and therefore can own the subdomain  █████████.



#Description:
The dangling CNAME record of █████████  is pointing to █████.███████ which was not claimed by you. I registered a service with this name and therefore was able to takeover the subdomain. Every attacker doing this has afterwards full control over the contents served on this subdomain.



#Subdomain Affected: 
██████████




#Proof Of Concept:
I have uploaded a simple subdomain takeover PoC on http://███████/████████





# Step-by-step Reproduction Instructions
1. Open ██████ and register for web app which is under market place. I have used ██████  (See: ████)

2. After registering, go to Custom Domains which will be available under settings. (See: ████)

3. In here, add custom domain i have used █████████ (See: █████)

4. After that upload any PoC you want to upload. I have used ████ which has my PoC. (See: ███████)





#Suggested Mitigation/Remediation Actions
1. Remove the dangling CNAME record for █████

2. Claim it back in ███████ portal after I release it

#Reference
Some hackerone reports #661751 #325336

#NOTE:
I have claimed the subdomain http://█████████ at the current moment to keep it safe from malicious users. Whenever you want i will release ██████.███. Afterwards you can claim it back.

## Impact

Subdomain takeover is abused for several purposes:

1.	Malware distribution
2.	Phishing / Spear phishing
3.	XSS

## Attachments
No attachments
