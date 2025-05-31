# [Critical] Insufficient Access Control On Registration Page of Webapps Website Allows Privilege Escalation to Administrator 

## Report Details
- **Report ID**: 796379
- **URL**: https://hackerone.com/reports/796379
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-14T02:36:19.299Z
- **Disclosed**: 2020-05-27T14:20:32.011Z

## Reporter
- **Username**: hunt4p1zza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Hello.

Due to insufficient access controls and poor implementation of the registration at https://████████/████/login.cfm it was possible to register while privilege escalating to an administrator.

**Description:**
It was possible to tamper with the registration request at https://█████████/██████/screen_questions.cfm which is aimed to ███████ applications for education in order to sign-up with administrator privileges. As a result, it was possible to gain access to personally identifiable information (PII) of all the applicants in the system, including SSNs, names, phones and emails.

At this point I stopped digging further and I started writing this report.

**Note:** Please can you liaise with the system's administrator and kindly ask them to remove the below accounts from the system after this has been triaged and resolved:

```
██████
█████████
███
█████████
██████
███
█████████
█████████
```

Apologies for creating all these accounts, most of them are just low privileged applicants, but I was confused as to why this attack worked and it took few attempts to figure it out.

Please let me know when this is resolved and I will remove any evidence that include PII data from my local system which are only kept locally.

## Impact
An attacker can gain administrative access in the system allowing them to expose sensitive PII information, such as including SSNs, names, phones and emails. Having this access, an attacker could completely take over the website and perform further attacks against it from this authenticated viewpoint - however I did not perform this. Attackers may sell this PII information on black-markets for profit.

If this was exploited and published there would be severe reputational and legal ramifications for DoD.

## Step-by-step Reproduction Instructions

1. Initially, enable your web intercepting proxy such as Burp Suite
2. Next, browse to the initial registration page at: https://████/████████/screen_questions.cfm and choose options in the dropdown lists: █████████
3. Next, you will be taken at the actual registration page at https://████/████████/newuser.cfm?loc_class=L (you can probably skip step 2 and come right here)
4. Fill in this form with some information and a legitimate looking SSN number. Keep in mind that if the SSN is registered in the system, the website will error, so you will have to try another one.
5. Intercept the request and modify it so that the `user_type` parameter has value 4, and the `fname` and `lname` parameters have values `Hackerone<%` and `test<%xss`. I believe it is `<%` that is causing this privilege escalate issue, but as I am not 100% positive I am giving you the full values. The request should look like mine: █████
6. If all went well, you should be logged in and prompted with a Privacy page which you need to accept.
7. Notice how this account has administrator access, an example is shown below: █████████

Finally, I created 2 short PoC videos showing how I was able to register as admin and how I was able to access PII data:

Create admin account video: ██████

Access PII data video: {F716040}

## Product, Version, and Configuration (If applicable)
The https://█████████ website is under █████████ which is part of DoD, as shown: █████████

## Suggested Mitigation/Remediation Actions
Unfortunately, I am not 100% positive on what exactly is causing this flaw, but injection of `<%` is required. This could be mitigated by applying strict user input validation in the `fname` and `lname` fields. Please see the link below for more information:

https://owasp.org/www-project-cheat-sheets/cheatsheets/Input_Validation_Cheat_Sheet

I would also recommend that you review the current user access types and levels in accordance with the findings above to ensure that setting the `user_type` to other numbers than the default one when registering (5) does not allow users to gain more privileges than they are authorized to. 

Additionally, review the whole codebase for broken access control, the following cheatsheet from OWASP provides more information:

https://owasp.org/www-project-cheat-sheets/cheatsheets/Access_Control_Cheat_Sheet

Finally, the web application appears to be very susceptible to common web application attacks and I would recommend that this undertakes a full thorough security test if possible or a code review, if of course it is required and cannot be decommissioned. 

PS: I will do my best to submit reports in terms of the rest of flaws I was able to spot while looking at it.

## Impact

An attacker can gain administrative access in the system allowing them to expose sensitive PII information, such as including SSNs, names, phones and emails. Having this access, an attacker could completely take over the website and perform further attacks against it from this authenticated viewpoint - however I did not perform this. Attackers may sell this PII information on black-markets for profit.

If this was exploited and published there would be severe reputational and legal ramifications for DoD.

## Attachments
No attachments
